import os
import subprocess
import shutil

cwd = r"c:\Users\User\Documents\BorgesOS_Atualizado"

# 1. Remove .git
git_dir = os.path.join(cwd, ".git")
if os.path.exists(git_dir):
    shutil.rmtree(git_dir)

# 2. Init git
subprocess.run(["git", "init"], cwd=cwd, check=True)

# 3. Remote
subprocess.run(["git", "remote", "add", "origin", "https://github.com/euluanborgess/os_borges_atualizado.git"], cwd=cwd, check=True)

# 4. Add to gitignore
with open(os.path.join(cwd, ".gitignore"), "a") as f:
    f.write("\n.env\n*.env\n*.zip\n")

# 5. Add and commit
subprocess.run(["git", "add", "."], cwd=cwd, check=True)
subprocess.run(["git", "reset", ".env"], cwd=cwd) # Just in case
subprocess.run(["git", "commit", "-m", "Restore from VPS (Base 44)"], cwd=cwd, check=True)

# 6. Push
res = subprocess.run(["git", "branch", "-M", "main"], cwd=cwd)
res = subprocess.run(["git", "push", "--force", "origin", "main"], cwd=cwd, capture_output=True, text=True)
print(res.stdout)
if res.stderr:
    print(res.stderr)
