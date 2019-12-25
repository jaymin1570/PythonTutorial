# w, a, r+

with open('file.txt','r+') as f:
    # data=f.read()
    f.seek(len(f.read()))
    f.write('please do it')
    # data=f.read()
    # print(data)