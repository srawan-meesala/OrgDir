import re
import os
import shutil

regex = r'.*\.(\w+)$'
folders = set()
files = []

parent_dir = os.path.abspath('.')

working_dir = os.path.join(parent_dir, 'sample')

for name in os.listdir(working_dir):
    result = re.search(regex, name)
    if result:
        files.append((name, result.groups()[0]))
    else: 
        folders.add(name)

for file in files:
    file_path = os.path.join(working_dir, file[0])
    if file[1] in folders:
        shutil.move(file_path, os.path.join(working_dir, file[1]))
    else:
        new_dir = os.path.join(working_dir, file[1])
        os.mkdir(new_dir)
        shutil.move(file_path, new_dir)
        folders.add(file[1])