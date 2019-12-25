# function practice

#def last_ch(a):
#    return name[len(a)-1] # name[-1]

#name = input("enter a name : ")
#print("last character of name : " + last_ch(name) )

def odd_even(num):
    if num%2 == 0:
        return "even " + str(num)

    return "odd " + str(num)

print(odd_even(3))

def is_even(num):
    if num%2 == 0:
        return True
    return False

print(is_even(6))

def is_even_2(num):
    return num%2 == 0
print(is_even_2(5))

def song():
    return "happy birthday song"
print(song())
