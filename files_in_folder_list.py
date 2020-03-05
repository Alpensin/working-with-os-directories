from os import scandir, path, chdir

result_list = 'logs_list.txt'
logs_dir = r"."
searched_extensions = ('.zip', '.nmf')
chdir(logs_dir)

with open(result_list, 'w') as f:
    for file in scandir():
        ext = path.splitext(file.name)[1]
        if ext in searched_extensions:
            f.write(file.name+'\n')
