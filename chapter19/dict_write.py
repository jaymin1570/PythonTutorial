from csv import DictWriter

with open('final.csv','w',newline='') as f:
    csv_dictwriter=DictWriter(f,fieldnames=['first_name','last_name','age'])
    csv_dictwriter.writeheader()
    # writerow,writerows
    csv_dictwriter.writerow({
        'first_name':'jaymin',
        'last_name':'makwana',
        'age':20
    })

    # writerows----->[dict,dict,dict]
    csv_dictwriter.writerows([
        {'first_name':'jaymin',
        'last_name':'makwana',
        'age':20},
        {'first_name':'jaymin',
        'last_name':'makwana',
        'age':20},
        {'first_name':'jaymin',
        'last_name':'makwana',
        'age':20}
    ])