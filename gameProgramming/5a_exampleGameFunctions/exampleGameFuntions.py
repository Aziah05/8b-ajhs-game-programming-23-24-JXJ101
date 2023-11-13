# Example Game Functions Project, Jahreem Jeffers, v0.0
import random

def functionaone():
    pass

def functionTwo(param1):
    pass

def functionThree(param1 = "Default Value"):
    pass

def functionFour(param1, param2, param3):
    pass
# Example to the funciton
# fighting game genre
# Choosing character

characters = 'aiden jaiden melina blaze virus JXJ JXQ Jack Blackmask Eclipsa'.split()

def genStats():
    aiden = [
	    9, # STRENGTH
	    7, # DEXTERITY
	    8, # CONSITUTION
	    6, # INTELLEGENCE
	    8, # WISDOM
	    7, # CHARISMA
    ]
    jaiden = [
	    5, # STRENGTH
	    9, # AGILITY
	    4, # CONSITUTION
	    4, # INTELLEGENCE
	    6, # WISDOM
	    6, # CHARISMA
    ]
    melina = [
	    8, # DARK MAGIC
	    8, # STAMINA
	    8, # CONSITUTION
	    6, # INTELLEGENCE
	    8, # WISDOM
	    7, # CHARISMA
    ]

def round(playerHealth, roundTime):
    if playerHealth > 0 and roundTime > 0:
        roundEnd = False
    elif playerHealth <= 0 and roundTime <= 0
        roundEnd = True
        
    if roundEnd = True:
        print("K.O") and RoundScore + 1         
    
round(75, 0)
     
    
    
    
    
    
# Example to the funciton
# def catchBall(throwQuality, passCatchScore, weather):
 #   if throwQuality > 5.0 and passCatchScore >= and weather == 'Sunny':
 #       ballCaught = True
 #   elif throwQuality > 4.0 and passCatchScore >= 75 and weather == 'Windy':
 #       ballCaught =  false
 #   else:
 #       print('Oh, no, interception!\n')
 #       ballIntercepted = True
 #       return ballIntercepted
 #   return ballCaught

#catchBall(4.25, 107, 'Rainy')