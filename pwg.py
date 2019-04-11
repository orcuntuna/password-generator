import random

def generate(lenght=16):
    pattern = "1234567890abcdefghijkqlmnoprstuvyzwxABCDEFGHIJKQLMNOPRSTUVYZWX./?-_()&%+#'!*=[]}{^<>€@,;:"
    password = ""
    for i in range(lenght):
        rand = random.randint(0,len(pattern)-1)
        password += pattern[rand]
    return password