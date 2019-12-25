# practice

is_even = lambda a:a%2==0
print(is_even(4))

last_char = lambda s : s[-1]
print(last_char('jaymin'))

# lambda with if else

def func(s):
    if len(s)>5:
        return True
    return False

func=lambda s:True if len(s)>5 else False
print(func('abc'))

    