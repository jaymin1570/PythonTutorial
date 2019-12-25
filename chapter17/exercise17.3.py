def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        print(err)
     
    except TypeError as err:
        print(err)
    except:
        print("unexcepted erro !!!")
    else:
        return result

print(divide(10,5.2))

