name = input ('enter your name:')
email = input('enter your email:')
mobile = input('enter your mobile')
city =input("enter your city")

# nested if-else 
if len(name)>1:
    if '@' in email and len (email) > 11:
        if len(mobile)==10 and mobile. isnumeric():
            if city in ["lku",'delhi','noida']:
               print('your data is saved, thankyou')
            else:
                 print('we are not available in your city')
        else:
            print("invalid mobile")
    else:
        print("invalid email address")
else:
    print('yeh kaisa name hai') 
           
        