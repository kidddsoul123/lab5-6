from bottle import datetime, post, request, run
import re

@post('/home', method='post')
def my_form():
    mail = request.forms.get('ADRESS')
    return "Thanks! The answer will be sent to the mail %s" % mail

@post('/home', method='post')
def check():
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d %H:%M:%S")
    
    emailpattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z]+\.[a-zA-Z0-9-.]+$"
    namepattern = r"^[a-zA-Z]$"
    
    mail = request.forms.get('ADRESS')
    name = request.forms.get('USERNAME')
    quest = request.forms.get('QUESTS')
    
    if mail and name and quest:
        if not len(quest) < 10:
            if not re.match(namepattern, name) and len(name) < 2:
                return "Name field has an incorrect value or an invalid length "
            else:
                if re.match(emailpattern, mail):
                    return f"Thank you for contacting us {name} <br> Access date: {current_date}"
                else:
                    return "You have entered an invalid email address"
        else:
             return "The question field cannot be shorter than 10 characters"
    else:
        return "One or more fields are not filled in"
