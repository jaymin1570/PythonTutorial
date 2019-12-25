with open('file4.txt','r') as rf:
    with open('file5.txt','w') as wf:
        for line in rf.readlines():
            name,salary=line.split(',')
            wf.write(f"{name}\'s salary is :{salary}")