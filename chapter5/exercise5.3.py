string = ['abc','tuv','xyz']

def reverse_string(l):
    rev = []
    for i in l:

        rev.append(i[::-1])
    return rev

print(f"reverse string is : {reverse_string(string)}")