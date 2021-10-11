def helloWorld(x):
    for z in range (x):
        z += 1
        print (str(z) + ' Hello World' ) #Dit is opdracht 1
                                            #Ik heb hello world 7 keer geprint 
helloWorld(7)


print ('=================')
#Opdracht 2
#Plus som
def addition(number1, number2):
    return  number1 + number2

print(addition(10,12))


#Min som

def subtraction(number1, number2):
    return number1 - number2

print(subtraction(58,34))

#Keer som
def multiplication(number1, number2):
    return number1 * number2

print(multiplication(6,7))

def division(number1, number2):
    return number1 // number2

print (division(144,12 ))

def increment(number):
    return number + 1

print(increment(12))

def decrement(number):
    return number - 1

print(decrement(34))
<<<<<<< Updated upstream
=======

print ('============================')

def vraag(leeftijd , naam):
    print ('Hallo' + naam + ' uw leeftijd is ' + leeftijd )
    return leeftijd, naam
    

while True:
    naam = input ("Hallo wat is uw naam?: ")
    leeftijd = input ("Wat is uw leeftijd?: ")
    if naam and leeftijd == "":
        print ('Hallo' + naam + ' uw leeftijd is ' + leeftijd )
    elif naam and leeftijd == "stop":
        print ("Fijn dat u er was")
        break



>>>>>>> Stashed changes
