import os

start_dir = "."

for dirname, dir_list, file_list in os.walk(start_dir):
    if ".git" in dir_list:
        dir_list.remove(".git")
    print("visiting", dirname)
    for file_name in file_list:
        if file_name.endswith('.py'):
            file_path = os.path.join(dirname, file_name)
            file_size = os.path.getsize(file_path)
            print(f"   {file_size:6d}   {file_name}")