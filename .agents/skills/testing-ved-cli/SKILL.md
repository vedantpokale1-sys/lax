---
name: testing-ved-cli
description: How to end-to-end test the ved.py interactive calculator CLI in the lax repo, including stdout/stderr separation, exit codes, EOF and Ctrl-C paths.
---

# Testing `ved.py` (lax repo)

`ved.py` is a dependency-free interactive Python CLI (`python3 ved.py`). There is no web UI and no
pytest suite in the repo, so a screen recording is not meaningful — collect terminal output as text
evidence instead. The blueprint's `pip install -r requirements-dev.txt` maintenance command refers to
a file that may not exist; no install step is needed to run or test the script.

## Prompt order
`main()` prompts: name → first number → second number → operator (`+ - * /`). Drive it by piping a
newline-joined string to stdin, e.g. `printf 'name\n4\n3\n/\n' | python3 ved.py`.

## Test harness pattern (recommended)
Use `subprocess.run([sys.executable, "ved.py"], input=..., capture_output=True, text=True)` and assert
on **three things per case**: `p.stdout`, `p.stderr`, and `p.returncode`. Separate pipes are essential —
piping `2>&1` would hide the main regression risk (error text leaking to stdout). Assert error cases
exit `1`, print the message on stderr only, contain no `Traceback (most recent call last)`, and print
neither a numeric result nor the trailer lines (`this is my calculator`, …).

## Ctrl-C / signal testing
`input()` only raises `KeyboardInterrupt` on a terminal, so use `pexpect` (already installed):
`pexpect.spawn(sys.executable, ["ved.py"], encoding="utf-8")`, `expect_exact("<prompt>")`, then
`send("\x03")`, then `expect(pexpect.EOF)` and check `c.exitstatus`. To prove which stream a message
used on a pty, spawn `bash -c "python3 ved.py > /tmp/out.txt"` so stdout goes to a file while stderr
stays on the pty.

## EOF testing
`python3 ved.py < /dev/null` (EOF at first prompt) and truncated stdin like `printf 'name\n5\n7\n'`
(EOF at the operator prompt) exercise the `EOFError` handlers at each prompt.

## Prove your tests discriminate
Grab the pre-change script with `git show <commit>^:ved.py > /tmp/ved_old.py` and run the same cases
against it as a control; the old version crashed with raw tracebacks, so identical-looking results
would signal a broken test harness.

## Devin Secrets Needed
None.
