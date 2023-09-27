### Random password generator ###
### CodeClause Internship Task 1 ###


import string      #string is imported
import random      #random characters can be obtained

#Specify our points according to length
#password basically consists of upper letters, lower letters, digits, symbols

upper_len=int(input("Enter how many upper characters do you need in a Password :"))
lower_len=int(input("Enter how many lower characters do you need in a Password :"))
digit_len=int(input("Enter how many digits do you need in a Password :"))
symbols_len=int(input("Enter how many symbols do you need in a Password :"))

#these upper, lower, digit, symbols altogether comprises of password

pwd_len=upper_len+lower_len+digit_len+symbols_len

upper=string.ascii_uppercase         #ascii=american standard code for information interchange
lower=string.ascii_lowercase
digit=string.digits
symbols=string.punctuation

str=upper+lower+digit+symbols

#this helps in the choice of characters in a sample 

str=random.sample(lower,k=lower_len)+random.sample(upper,k=upper_len)+random.sample(digit,k=digit_len)+random.sample(symbols,k=symbols_len)
#above shows in a list

random.shuffle(str)
password="".join(str)     #joins the characters in a list

print("password is :",password)