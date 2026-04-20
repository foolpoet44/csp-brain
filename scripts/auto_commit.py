import subprocess
import os
from datetime import datetime

# CSP Brain Auto-Commit - v1.0
# 변경된 지식을 감지하여 의미 있는 커밋 메시지와 함께 Push합니다.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def run_git_command(args):
    try:
        result = subprocess.run(
            ["git"] + args,
            cwd=BASE_DIR,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Git Error: {e.stderr}")
        return None

def sync_knowledge():
    # 1. 상태 확인
    status = run_git_command(["status", "--porcelain"])
    if not status:
        print("No changes detected in knowledge base.")
        return

    print("Knowledge changes detected. Syncing...")

    # 2. Add
    run_git_command(["add", "."])

    # 3. Commit 메시지 생성
    # 변경된 폴더를 기반으로 간략한 메시지 생성
    lines = status.split("\n")
    modified_paths = set()
    for line in lines:
        if len(line) > 3:
            path = line[3:].split("/")[0]
            modified_paths.add(path)
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    summary = ", ".join(modified_paths)
    commit_msg = f"knowledge: sync - {summary} ({timestamp})"

    # 4. Commit
    run_git_command(["commit", "-m", commit_msg])

    # 5. Push
    print(f"Pushing to origin main: {commit_msg}")
    push_result = run_git_command(["push", "origin", "main"])
    if push_result is not None:
        print("Knowledge sync complete.")
    else:
        print("Push failed. Check remote connectivity.")

if __name__ == "__main__":
    sync_knowledge()
