import os
import shutil
os.chdir(r'F:\stuff\newstuff')
# print(os.listdir())
fileiter=os.walk(r'F:\stuff\newstuff')
# for current_path,folder_name,file_name in fileiter:
#     print(f'current_path : {current_path}')
#     print(f'folder_name: {folder_name}')
#     print(f'fila_names : {file_name}')

# os.makedirs('new/movie2')
# shutil.rmtree('document')
# shutil.copytree('new','document/new22123')
# shutil.copy('file.txt','document/file2.txt')
# shutil.move('file.txt','new/file2.txt')
shutil.move('new','document/new2')
