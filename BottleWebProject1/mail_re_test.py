import re 
emailpattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z]+\.[a-zA-Z0-9-.]+$"
def is_mail(mail):
    return bool(re.match(emailpattern, mail))
