# with open('index.html','r') as webpage:
#     with open('output.txt','a') as wf:
#         for line in webpage.readlines():
#             if '<a href=' in line:
#                 pos =line.find('<a href=')
#                 first_quote=line.find('\"',pos)
#                 second_qoute=line.find('\"',first_quote+1)
#                 url=line[first_quote:second_qoute]
#                 wf.write(url+'\n')

with open('index.html','r') as webpage:
    with  open('output2.txt','w') as wf:
        page=webpage.read()
        print(page)
        link_exist=True
        while link_exist:
            pos =page.find('<a href=')
            if pos == -1:
                link_exist =False
            else:
                first_quote=page.find('\"',pos)
                second_qoute=page.find('\"',first_quote+1)
                url=page[first_quote+1:second_qoute]
                wf.write(url+'\n')
                page=page[second_qoute:]
                
                
