import os
import subprocess
from pathlib import Path
import re

def get_changed_files():
    # github actions에서 제공하는 SHA 환경변수 사용
    before = os.environ.get('GITHUB_BASE_SHA')
    after = os.environ.get('GITHUB_SHA')
    if not before or not after:
        # fallback: HEAD^..HEAD
        before = 'HEAD^'
        after = 'HEAD'
    result = subprocess.run(['git', 'diff', '--name-only', f'{before}', f'{after}'], capture_output=True, text=True)
    files = result.stdout.strip().split('\n')
    return [f for f in files if f]

def find_problem_pairs(changed_files):
    # 문제 폴더별로 README.md, .py가 모두 변경된 경우만 반환
    problem_map = {}
    for f in changed_files:
        parts = Path(f).parts
        if len(parts) < 4: continue
        if parts[0] != '백준': continue
        level, problem, filename = parts[1], parts[2], parts[3]
        key = (level, problem)
        problem_map.setdefault(key, set()).add(filename)
    # README.md와 .py가 모두 있는 문제만
    for (level, problem), files in problem_map.items():
        pyfile = next((f for f in files if f.endswith('.py')), None)
        if 'README.md' in files and pyfile:
            yield Path('백준') / level / problem, pyfile

def log_merge_content(problem_path, code_filename):
    readme_path = problem_path / 'README.md'
    code_path = problem_path / code_filename
    if not readme_path.exists() or not code_path.exists():
        return
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read().rstrip()
    with open(code_path, 'r', encoding='utf-8') as f:
        code = f.read().rstrip()
    # 이미 ### 풀이가 있으면 덮어쓰기
    if '### 풀이' in content:
        content = content.split('### 풀이')[0].rstrip()
    merged = f"{content}\n\n### 풀이\n<code>\n{code}\n</code>\n"
    print(f"[LOG] {problem_path}의 README.md에 {code_filename} 코드가 합쳐집니다.")
    print("--- 합쳐질 내용 ---")
    print(merged)
    print("--- END ---\n")

def make_number_md(readme_path):
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # 첫 줄에서 문제번호 추출
    first_line = content.splitlines()[0]
    m = re.search(r'-\\s*(\\d+)', first_line)
    if not m:
        return None
    number = m.group(1)
    md_path = f'/tmp/{number}.md'
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return md_path

def main():
    changed_files = get_changed_files()
    for problem_path, code_filename in find_problem_pairs(changed_files):
        log_merge_content(problem_path, code_filename)

if __name__ == '__main__':
    main()
