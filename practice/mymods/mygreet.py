# mygreet.py  

def hello(name, *age):  
    print("Hello there %s" % name)
    print("Age is %d." % age)
    return 'Greetings {} and welcome.'.format(name)