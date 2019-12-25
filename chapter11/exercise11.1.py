
def to_power(num,*args):
    if args:
        return [i**num for i in args]
    else:
        return 'you diin\'t pass any args'


numbers = [1,2,3]
num=3
print(to_power(num,*numbers))  # unpack