import os

#os.getcwd()
os.chdir(r'F:\new_python\chapter20')
# print(os.getcwd())
# os.mkdir('movies')
# os.mkdir('movies')
# print(os.path.exists('movies2'))
# if os.path.exists('movies'):
#     print("already exists")
# else:
#     os.mkdir('movies')
   
# open('file.txt','a').close()

# os.mkdir(r'F:\stuff\movies')
# print(os.listdir())

for item in os.listdir():
    path=os.path.join(os.getcwd(),item)
    print(path)
    # print(r'F:\stuff' + '\\' +item)
