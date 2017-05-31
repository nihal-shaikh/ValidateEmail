import re
def validateEmail(email):
    pattern= re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    if re.match(pattern,email):
        return True
    else:
        return False







email = "macantosh@gmail.com"
print("The email address is valid:",validateEmail(email))