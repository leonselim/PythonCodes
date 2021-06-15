""" 


=========================================       BANDNAME     ===============================================


from typing import Mapping

cityName = input('Welcome to band name maker, please input city name?\n')
petName = input('What is the name of your pet?\n')
print(cityName +" "+ petName) 


=========================================       TIP CALC     ===============================================


### function for tip
stupidCalc()
bmiWeight()
lastDays()
treasureislandStart()

        totalCharList = []
        numList = ['0','1','2','3','4','5','6','7','8','9']
        sybList = ['']
        charSmallList = [string.ascii_uppercase]
        charBigList = [string.ascii_lowercase]
        for x in range(len(charSmallList)):
        totalCharList.extend(charSmallList[x])
        for x in range(len(charBigList)):
            totalCharList.extend(charBigList[x])
        countNum = 0

=========================================       CLS CMD     ================================================
        
from os import system
import random
import string

def cls():
    _ = system("cls")

    
=========================================       HANGMAN     ================================================


import random

def guessRandom():
    guessLists = ['corroded','arduous','unfaith']
    random_word = list(random.choice(guessLists))
    return random_word

def notnotnot(catchMe):
    catchMe += 1
    print(f'Wrong answer! Try again! Current wrong answer: {catchMe} ')
    return catchMe

def removeDupes(clearing):
    newStr = ""
    for ch in clearing:
        if ch not in newStr:
            newStr = newStr + ch
    return newStr

def askUsertoPlayAgain(hehe):
    
    if not hehe or hehe == "":
        print('YOU KILLED YOURSELF!')
        exit()
    elif hehe == 1:
        startHangman()
    elif hehe == 2:
        exit()
    else:
        exit()

        
def startHangman():

    wrongCounter = 0
    innoculation = []
    innoculated = []
    letterCatcher = []
    user_guess = []
    innoculation = guessRandom()
    innoculated = removeDupes(innoculation)
    
    
    try:
        enterkey = input('Guess Word! Press Enter to proceed.')
        while wrongCounter != 5 and len(innoculation) != len(innoculated):
            user_guess = input(f'Press a letter for clues!').lower()
            
            if not user_guess or user_guess == "":
                wrongCounter = notnotnot(wrongCounter)
            elif user_guess in innoculation:
                if user_guess in letterCatcher:
                    print('You already type that letter try again!')
                else:
                    letterCatcher.extend(user_guess)
                    for x in innoculation:
                        if x in letterCatcher:
                            print(f'{x}, ',end="")
                        else:
                            print('-, ',end="")
                    print('\n')
            else:
                wrongCounter = notnotnot(wrongCounter)
                
            if len(letterCatcher) == len(innoculated):
                maronLuis = int(input('You Win! Press 1 to Try Again and 2 for Exit'))
                askUsertoPlayAgain(maronLuis)
                
            if wrongCounter == 5:
                luis = int(input('You Win! Press 1 to Try Again and 2 for Exit'))
                askUsertoPlayAgain(luis)
        
    except:
        print('')
        
        
startHangman()


=========================================       BMI CALC     ================================================


def bmiWeight():
	weightKG = float(input('KG?\n'))
	heightMet = float(input('Meter?\n'))
	
	print(round(weightKG/(heightMet**2),2))

    
=========================================       LASTDAYS     ================================================
    
def lastDays():
		ageIn = 90-(int(input('Age\n')))
		ageDays = ageIn*365
		ageWeeks = ageIn*52
		ageMonths = ageIn*12
		ageSeconds = ageDays*24*60*60
		
		print(f"Remaining days {ageDays}, weeks {ageWeeks}, months {ageMonths}, years {ageIn}, seconds {ageSeconds}")

        
        
=========================================       PRIME FACTOR     ============================================


------------------- FIRST FILE -----------------------------

import custom_module

stopper = 'yes'

while stopper != 'no':

    user_input = int(input('Prime factor checker. Please insert number to check: \t'))
    result = custom_module.primeFactoring(user_input)
    if result == True:
        print(f"The number has a prime factor!")
    elif result == False:
        print(f"The number has no prime factor!")
    stopper = input('Do you want to continue? Type Yes for again, No for stop').lower()
    
------------------- SECOND FILE -----------------------------

def primeFactoring(number):
    primeFactor = False
    for i in range(2,number-1):
        if number % i == 0:
            primeFactor = True
            return primeFactor
        else:
            return primeFactor

+===============================================       MOSH Practice     ===================================================
            
output = ""
mappingIn = {
    '1':'One',
    '2':'Two',
    '3':'Three',
    '4':'Four',
    '5':'Five',
    '6':'Six',
    '7':'Seven',
    '8':'Eight',
    '9':'Nine',
    '10':'Ten'
    }
    
getIn = input('Phone number:')

for l in getIn:
   output += mappingIn.get(l,'!') + " "
   
print(output)

            
            
            
+===============================================       CAESAR CIPHER     ===================================================
            
            
            
            
### most important is to get the two decoders from complete alphabet to shifted letters


def cipherCodeEncode(x): 
### getting the shift number
    estm = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    req = []
    composite = []
    for i in range(x,25):
        req.extend(estm[i])
    for j in range(0,x):
        req.extend(estm[j])
        
### getting user word
    encodeWord = str(input('Enter word to encode')).lower()
    if not encodeWord or encodeWord == "":
        print('Error. Something happened')
    else:
        for k in range(len(encodeWord)):
            if encodeWord[k] == " ":
                composite.extend(" ")
            for l in range(len(estm)):
                if encodeWord[k] == estm[l]:
                    composite.extend(req[l])

### assign user word to cipher and return
    return composite



def cipherCodeDecode(y):
###setting letters
    estm = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    req = []
    composite = []
###changing letter to alphabet order by shift
    for i in range(y,25):
        req.extend(estm[i])
    for j in range(0,y):
        req.extend(estm[j])
###getting word and decipher word
    decodeWord = str(input('Enter word to encode')).lower()
    for k in range(len(decodeWord)):
        if decodeWord[k] == " ":
            composite.extend(" ")
        for l in range(len(req)):
            if decodeWord[k]==req[l]:
                composite.extend(estm[l])
    return composite


def caesarCipher():
    user_allow = 'yes'

    while user_allow == 'yes':

        user_insert = input("Caesar Cipher\nDo you want to 'encode' or 'decode'. Type action: ").lower()
        
        if not user_insert or user_insert == "":
            print("Error now exiting.")
            exit()
        elif user_insert == 'encode':
            shift = int(input('How many shifts? '))
            outmost = cipherCodeEncode(shift)
            print(outmost)
        elif user_insert == 'decode':
            shift = int(input('How many shifts? '))
            inmost = cipherCodeDecode(shift)
            print(inmost)
        else:
            print("Error now exiting.")
            exit()
        
        user_allow = str(input('Do you want to continue? Yes or No?')).lower()
        
        if not user_allow or user_allow == "":
            print("Error now exiting.")
            exit()
        elif user_allow == 'yes':
            caesarCipher()
        else:
            exit()

caesarCipher()
            
"""
