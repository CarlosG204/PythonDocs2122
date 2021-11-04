#import the basics module to use its code
import basics

#make a new application objetc from the basics module
app = basics.newProgram()

#use method that belongs to our new application object
app.print('yo momma')

#print a property of our new appplication object
app.print(app.debugging)

#this line won't print if app.debugging is False
app.debug("Hello")

#we'll enable debugging for the application
app.debugging = True
app.debug('Now it works!')

#import a default Python module
import random

#use a method from the random module
randomNumber = random.randint(1, 10)
app.print(randomNumber)
