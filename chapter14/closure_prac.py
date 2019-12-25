# function returning function (closure) function

# square,cube 

def to_power(x):
    def calc_power(n):
        return n**x
    return calc_power

cube=to_power(3)
print(type(cube))
print(cube.__name__)
print(cube(5))


square= to_power(2)
print(square(6))