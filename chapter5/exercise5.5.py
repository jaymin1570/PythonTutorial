def common_element(l1,l2):
    l = []
    for i in l1:
        for j in l2:    # if i in l2:
            if i == j:  # l.append(i)
                l.append(i) # return l
    return l
num1 = [1,2,5,8]
num2 = [1,2,7,6]
print(f"common element are : {common_element(num1,num2)}")

            

