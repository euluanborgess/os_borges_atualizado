import subprocess

cmds = [
    ["git", "add", "."],
    ["git", "reset", ".env"],
    ["git", "commit", "-m", "Base 44 from VPS without secrets"],
    ["git", "push", "--force", "origin", "main"]
]

for cmd in cmds:
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)
