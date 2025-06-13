import os
import subprocess
from pathlib import Path
import re
import codecs
from datetime import datetime
import html

def get_changed_files():
    # git diff에서 한글 경로가 이스케이프되지 않도록 설정
    subprocess.run(['git', 'config', 'core.quotepath', 'false'])
    before = os.environ.get('GITHUB_BASE_SHA')
    after = os.environ.get('GITHUB_SHA')
    if not before or not after:
        before = 'HEAD^'
        after = 'HEAD'
    result = subprocess.run(['git', 'diff', '--name-only', f'{before}', f'{after}'],
                           capture_output=True, text=True, encoding='utf-8')
    files = result.stdout.strip().split('\n')
    # 큰따옴표 제거 및 빈 문자열 필터링
    files = [f.strip('"') for f in files if f.strip()]
    return files

def find_problem_pairs(changed_files):
    for f in changed_files:
        # 유니코드 이스케이프 해제 시도 (필요시)
        try:
            # 만약 경로에 \xxx 형태가 있으면 디코딩
            if '\\' in f:
                f_decoded = codecs.decode(f, 'unicode_escape')
            else:
                f_decoded = f
        except Exception:
            f_decoded = f
        parts = Path(f_decoded).parts
        if len(parts) < 4: continue
        if parts[0] != '백준': continue
        if not f_decoded.endswith('.py'): continue
        level, problem, filename = parts[1], parts[2], parts[3]
        yield Path('백준') / level / problem, filename

def merge_code_to_readme(readme_path, code_path):
    if not readme_path.exists() or not code_path.exists():
        return False
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read().rstrip()
    with open(code_path, 'r', encoding='utf-8') as f:
        code = f.read().rstrip()
    if '### 풀이' in content:
        content = content.split('### 풀이')[0].rstrip()
    # 마크다운 코드 블록으로 변경
    merged = f"{content}\n\n### 풀이\n```python\n{code}\n```\n"
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(merged)
    return True

def convert_html_to_markdown(content):
    # MathJax 관련 태그 제거
    content = re.sub(r'<mjx-container[^>]*>.*?</mjx-container>', '', content, flags=re.DOTALL)
    content = re.sub(r'<mjx-math[^>]*>.*?</mjx-math>', '', content, flags=re.DOTALL)
    content = re.sub(r'<mjx-assistive-mml[^>]*>.*?</mjx-assistive-mml>', '', content, flags=re.DOTALL)
    content = re.sub(r'<span[^>]*class="no-mathjax[^>]*>.*?</span>', '', content, flags=re.DOTALL)
    
    # style 속성이 있는 p 태그에서 이미지 추출
    def replace_image_in_p(match):
        img_tag = match.group(1)
        # 이미지 태그에서 src 추출
        src_match = re.search(r'src="([^"]*)"', img_tag)
        if src_match:
            src = src_match.group(1)
            # alt가 비어있으면 "그림"으로 대체
            alt_match = re.search(r'alt="([^"]*)"', img_tag)
            alt = alt_match.group(1) if alt_match and alt_match.group(1) else "그림"
            return f"\n\n![{alt}]({src})\n\n"
        return ""
    
    # style 속성이 있는 p 태그에서 이미지 처리
    content = re.sub(r'<p[^>]*style="[^"]*"[^>]*>(<img[^>]*>)</p>', replace_image_in_p, content, flags=re.DOTALL)
    
    # 일반 이미지 태그를 마크다운 문법으로 변경 (p 태그 밖에 있는 경우)
    def replace_image(match):
        src = match.group(1)
        alt = match.group(2) if match.group(2) else "그림"
        return f"\n\n![{alt}]({src})\n\n"
    
    content = re.sub(r'<img[^>]*src="([^"]*)"[^>]*(?:alt="([^"]*)")?[^>]*>', replace_image, content)
    
    # 그림 설명을 마크다운 문법으로 변경
    content = re.sub(r'<strong>그림\s*(\d+)</strong>:\s*(.*?)(?=<|$)', r'**그림 \1**: \2', content, flags=re.DOTALL)
    
    # 모든 HTML 태그 제거 (단, 이미지와 그림 설명은 이미 처리됨)
    content = re.sub(r'<[^>]+>', '', content)
    
    # HTML 엔티티 디코딩
    content = html.unescape(content)
    
    # 연속된 빈 줄 제거 (최대 2개로)
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # 앞뒤 공백 제거
    content = content.strip()
    
    return content

def export_readme_to_number_md(readme_path):
    print(f"\n=== Exporting README to number.mdx ===")
    print(f"Reading from: {readme_path}")
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # HTML 태그를 마크다운으로 변환
    content = convert_html_to_markdown(content)
    
    # 첫 줄에서 제목과 문제 번호 추출
    lines = content.splitlines()
    first_line = lines[0]
    title = first_line.replace('# ', '').strip()
    
    # 문제 번호 추출
    m = re.search(r'-\s*(\d+)', first_line)
    if not m:
        print("Could not find problem number in first line")
        return None
    number = m.group(1)
    print(f"Found problem number: {number}")
    
    # 현재 날짜와 시간 가져오기 (YYYY-MM-DD HH:MM:SS 형식)
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # 태그 추출
    tags = []
    for i, line in enumerate(lines):
        if line.startswith('### 분류'):
            if i + 2 < len(lines):  # 분류 다음 줄에 태그가 있다고 가정
                tags_line = lines[i + 2].strip()
                tags = [tag.strip() for tag in tags_line.split(',')]
            break
    
    # 메타데이터 생성
    metadata = f"""export const metadata = {{
  title: '{title}',
  date: '{current_date}',
  tags: {tags},
  description: '{title}',
}};

"""
    
    # md_output 디렉토리 사용
    workspace = os.environ.get('GITHUB_WORKSPACE', '.')
    print(f"GITHUB_WORKSPACE: {workspace}")
    output_dir = Path(workspace) / 'md_output'
    print(f"Output directory: {output_dir}")
    print(f"Output directory exists: {output_dir.exists()}")
    
    output_dir.mkdir(exist_ok=True)
    print(f"Created output directory: {output_dir.exists()}")
    
    # .mdx 확장자로 변경
    md_path = output_dir / f'{number}.mdx'
    print(f"Writing to: {md_path}")
    
    # 메타데이터와 원본 내용을 합쳐서 작성
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(metadata + content)
    print(f"Successfully wrote to {md_path}")
    return md_path

def main():
    print(f"Current working directory: {os.getcwd()}")
    print(f"GITHUB_WORKSPACE: {os.environ.get('GITHUB_WORKSPACE', '.')}")
    
    changed_files = get_changed_files()
    print(f"Changed files: {changed_files}")
    
    for problem_path, code_filename in find_problem_pairs(changed_files):
        print(f"\nProcessing: {problem_path} / {code_filename}")
        readme_path = problem_path / 'README.md'
        code_path = problem_path / code_filename
        print(f"Paths: readme={readme_path}, code={code_path}")
        
        merged = merge_code_to_readme(readme_path, code_path)
        print(f"Merge result: {merged}")
        
        if merged:
            md_path = export_readme_to_number_md(readme_path)
            if md_path:
                print(f"Successfully exported to {md_path}")
            else:
                print("Failed to export README to number.md")

if __name__ == '__main__':
    main()
