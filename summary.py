import os

def should_exclude(file_path):
    # Files and directories to exclude
    exclude_names = ['.gitignore', '.env', '__pycache__', 'README.md', 'README.txt', '.git', 'poetry.lock', 'summary.py']
    exclude_extensions = ['.gitignore', '.env']
    base_name = os.path.basename(file_path)
    
    if base_name in exclude_names:
        return True
    if os.path.splitext(base_name)[1] in exclude_extensions:
        return True
    if os.path.isdir(file_path) and base_name in exclude_names:
        return True
    return False

def get_file_info(root_dir):
    file_list = []
    
    for root, dirs, files in os.walk(root_dir):
        # Exclude directories from being walked
        dirs[:] = [d for d in dirs if not should_exclude(os.path.join(root, d))]
        
        for file in files:
            file_path = os.path.join(root, file)
            if should_exclude(file_path):
                continue
            
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            file_info = {
                'path': file_path,
                'name': file,
                'content': content
            }
            file_list.append(file_info)
    
    return file_list

def write_file_info(file_list, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for file in file_list:
            f.write(f"Path: {file['path']}\n")
            f.write(f"Name: {file['name']}\n")
            f.write(f"Content:\n{file['content']}\n")
            f.write("\n" + "="*80 + "\n\n")

def main():
    project_folder = os.getcwd()
    output_file = 'data-manager-api.txt'
    file_list = get_file_info(project_folder)
    write_file_info(file_list, output_file)
    print(f"File list with contents written to {output_file}")

if __name__ == "__main__":
    main()
