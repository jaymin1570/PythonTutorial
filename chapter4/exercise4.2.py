def is_pelindrom(string):
    # rev = string[::-1]
    if string == string[::-1]:
        return True
    return False

print(is_pelindrom("ravivar"))

# def is_pelindrom(string):
    # return string == string[::-1]
