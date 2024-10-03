def is_password_secure(password):
    rating,length,upper,lower,num,special_char=0,0,0,0,0,0 #rating system to keep track of each requirement
    if len(password)>=8:
        length=1
    for char in password:
        if str(char) in '1234567890':
            num=1
        elif char.upper() in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if char==char.upper():
                upper=1
            elif char==char.lower():
                lower=1
        elif char in "!@#$%^&*()-_=+{}[]:;<>?,.|`~":
            special_char=1
    rating=length+upper+lower+num+special_char
    if rating==5:
        return True
    else:
        return False
print(is_password_secure('fgjkJKL93 2W3DFJjdks'))