def odd_even_list (l):
    l1 =[]
    l2 = []
    for i in l:
        if i%2 == 0:
            l2.append(i)
        else:   
            l1.append(i)
    output = [l1,l2]  
    return output  
number = [1,2,3,4,5,6,7]
print(odd_even_list(number))