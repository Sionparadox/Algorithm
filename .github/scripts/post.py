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

def merge_code_to_readme(readme_path, code_path):
    if not readme_path.exists() or not code_path.exists():
        return False
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read().rstrip()
    with open(code_path, 'r', encoding='utf-8') as f:
        code = f.read().rstrip()
    if '### 풀이' in content:
        content = content.split('### 풀이')[0].rstrip()
    merged = f"{content}\n\n### 풀이\n<code>\n{code}\n</code>\n"
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(merged)
    return True

def export_readme_to_number_md(readme_path):
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    first_line = content.splitlines()[0]
    m = re.search(r'-\s*(\d+)', first_line)
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
        readme_path = problem_path / 'README.md'
        code_path = problem_path / code_filename
        merged = merge_code_to_readme(readme_path, code_path)
        if merged:
            export_readme_to_number_md(readme_path)

if __name__ == '__main__':
    main()
