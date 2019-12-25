# writer , Dictwriter

from csv import writer

with open('file6.csv','w',newline='') as f:
    csv_writer=writer(f)
    # method -writerow,writerows
    # csv_writer.writerow(['name','country'])
    # csv_writer.writerow(['jaymin','INDIA'])
    # csv_writer.writerow(['shakti','INDIA'])

    csv_writer.writerows([['name','country'],['jaymin','INDIA'],['shakti','INDIA']])