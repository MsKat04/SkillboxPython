import re
import doctest

def is_valid_password(password):
    """
    >> > is_valid_password("rtG3FG!Tr^e")
    True
    >> > is_valid_password("aA1!*!1Aa")
    True
    >> > is_valid_password("oF^a1D@y5e6")
    True
    >> > is_valid_password("enroi#$rkdeR#$092uWedchf34tguv394h")
    True
    >> > is_valid_password("пароль")
    False
    >> > is_valid_password("password")
    False
    >> > is_valid_password("qwerty")
    False
    >> > is_valid_password("lOngPa$$$W0Rd")
    False
    """
    reges = (
        r'^(?=.*[a-z].*[a-z])'
        r'(?=.*\d)'
        r'(?=.*[$^%@#&*])' 
        r'(?=.*[$^%@#&*].*[$^%@#&*].*[$^%@#&*])'
        r'[^,.!?]'
        r'[\w$^%@#&*]{8,}$'
    )
    return re.match(reges, password) is not None

doctest.testmod()