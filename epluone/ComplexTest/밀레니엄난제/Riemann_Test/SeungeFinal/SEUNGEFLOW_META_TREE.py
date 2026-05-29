import os
import datetime

def export_meta_tree(target_path, output_filename):
    """
    지정된 경로의 트리를 순회하며 메타데이터를 읽고 .md 파일로 저장하는 커널.
    """
    if not os.path.exists(target_path):
        print(f"⚠️ 경로를 찾을 수 없습니다: {target_path}")
        return

    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(f"# SeungeFlow Node Tree: {target_path}\n")
        f.write(f"Generated at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        for root, dirs, files in os.walk(target_path):
            level = root.replace(target_path, '').count(os.sep)
            indent = '    ' * level
            folder_name = os.path.basename(root) or target_path
            
            # 폴더 메타데이터
            try:
                m_time = os.path.getmtime(root)
                modified = datetime.datetime.fromtimestamp(m_time).strftime('%Y-%m-%d %H:%M')
                f.write(f"{indent}📂 [{folder_name}] (Modified: {modified})\n")
            except:
                f.write(f"{indent}📂 [{folder_name}]\n")

            # 파일 메타데이터
            sub_indent = '    ' * (level + 1)
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    c_time = os.path.getctime(file_path)
                    m_time = os.path.getmtime(file_path)
                    created = datetime.datetime.fromtimestamp(c_time).strftime('%Y-%m-%d %H:%M')
                    modified = datetime.datetime.fromtimestamp(m_time).strftime('%Y-%m-%d %H:%M')
                    
                    # Target Pin 강조 로직 (104, 60~70)
                    highlight = ""
                    name, _ = os.path.splitext(file)
                    num_part = name.split('.')[-1]
                    if num_part.isdigit():
                        num = int(num_part)
                        if num == 104 or 60 <= num <= 70:
                            highlight = " ★[TARGET PIN]"
                    
                    f.write(f"{sub_indent}📄 {file}{highlight} | Created: {created} | Modified: {modified}\n")
                except:
                    f.write(f"{sub_indent}📄 {file} (Error reading meta)\n")

    print(f"✅ 추출 완료: {output_filename}")

# 1. 현상 줄기 (C 드라이브) 추출
export_meta_tree(r"C:\home", "home_tree.md")

# 2. 본질 줄기 (E 드라이브) 추출
export_meta_tree(r"E:\개념정리", "개념정리_tree.md")