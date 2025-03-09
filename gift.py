import pywhatkit

print("happy birthday")
print("Its me your virtual friend for some time")
print("My name is Pikinose\nSmall chat made by patta")
phone = str(input("Please enter ur parents number for reference "))
timehr = int(input("please also enter the time to send msg 'Hour ->not like 03 like only 3' "))
timemin = int(input("please also enter the time to send msg 'min' "))

#small program to automate whatsapp message directly through terminal 
#hehee    
    
    

wish1 = str(input("Enter ur first wish"))
if wish1 == "cadbury dairy milk":
    print("Umm ok chotu cadbury added to the cart")
else:
    print("%s Added to the wishlist!" %wish1)

smallconvo = str(input("Would u like me to tell u a joke? type y/n? "))
if smallconvo == "y":
    print("What is the best way to remember your friend's birthday? Forget it once."
          
          )
elif smallconvo == "n":
    ("u don't have balls to listen a joke? ")

print("sorry just a joke hehe how can we forget someone's B'day")

wish2 = str(input("Enter ur 2nd wish : "))
print("Added")
condi = str(input("would u like me to send ur wishes to ur parents? y/n "))
wish = wish1 + " " + wish2
if condi == "y":
     pywhatkit.sendwhatmsg(phone,
                          wish,
                          timehr, timemin)

elif condi == "n":
    print("Ok it was a sweet adn happy convo with you ")
    print("Happy Birthday by Pikinose")
    



