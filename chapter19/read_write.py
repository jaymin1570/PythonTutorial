# reader ,Dictreader
# writer, Dictwriter
from csv import DictReader,DictWriter
with open('file3.csv','r') as rf:
    with open('read_write2.csv','w',newline='') as wf:
        csv_reader=DictReader(rf)
        csv_writer=DictWriter(wf,fieldnames=['first_name','last_name','age'])
        csv_writer.writeheader()
        for row in csv_reader:
            fname,lname,age=row['first_name'],row['last_name'],row['age']
            csv_writer.writerow({
                'first_name':fname.upper(),
                'last_name':lname.upper(),
                'age':age
            })