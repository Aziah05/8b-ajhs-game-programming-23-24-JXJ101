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

character = {'aiden, jaiden, melina, blaze, virus, jxj, jxq, Jack, Blackmask, Eclipsa'}

def genStats():
    aidenStats = [
        healthAiden [120] # HEALTH
        strengthAiden [9] # STRENGTH
	    consitutionAiden [8] # CONSITUTION
	    intellegenceAiden [6] # INTELLEGENCE
	    wisdomAiden = 8, # WISDOM
	    charismaAiden = 7, # CHARISMA
    ]
    jaidenStats = [
	    5, # STRENGTH
	    9, # AGILITY
	    4, # CONSITUTION
	    4, # INTELLEGENCE
	    6, # WISDOM
	    6, # CHARISMA
    ]
    melinaStats = [
	    healthMelina = 120, # HEALTH
	    strengthMelina = 9, # STRENGTH
	    consitutionMelina = 8, # CONSITUTION
	    intellegenceMelina = 6, # INTELLEGENCE
	    wisdomMelina = 8, # WISDOM
	    charismMelina = 7
    ]
    blazeStats = [
	    healthBlaze = 120, # HEALTH
	    strengthBlaze = 9, # STRENGTH
	    consitutionBlaze = 8, # CONSITUTION
	    intellegenceBlaze = 6, # INTELLEGENCE
	    wisdomBlaze = 8, # WISDOM
	    charismaBlaze = 7
    ]
    virusStats = [
	    healthVirus = 120, # HEALTH
	    strengthVirus = 9, # STRENGTH
	    consitutionVirus = 8, # CONSITUTION
	    intellegenceVirus = 6, # INTELLEGENCE
	    wisdomVirus = 8, # WISDOM
	    charismaVirus = 7
    ]
    jxjStats = [
	    healthJxj = 120, # HEALTH
	    strengthJxj = 9, # STRENGTH
	    consitutionJxj = 8, # CONSITUTION
	    intellegenceJxj = 6, # INTELLEGENCE
	    wisdomJxj = 8, # WISDOM
	    charismaJxj = 7
    ]
    JXQStats = [
	    healthJxq = 120, # HEALTH
	    strengthJxq = 9, # STRENGTH
	    consitutionJxq = 8, # CONSITUTION
	    intellegenceJxq = 6, # INTELLEGENCE
	    wisdomJxq = 8, # WISDOM
	    charismaJxq = 7
    ]
    blackmaskStats = [
	    healthBlackmask = 120, # HEALTH
	    strengthBlackmask = 9, # STRENGTH
	    consitutionBlackmask = 8, # CONSITUTION
	    intellegenceBlackmask = 6, # INTELLEGENCE
	    wisdomBlackmask = 8, # WISDOM
	    charismaBlackmask = 7
    ]
    eclipsaStats = [
	    healthEclipsa = 120, # HEALTH
	    strengthEclipsa = 9, # STRENGTH
	    consitutionEclipsa = 8, # CONSITUTION
	    intellegenceEclipsa = 6, # INTELLEGENCE
	    wisdomEclipsa = 8, # WISDOM
	    charismaEclipsa = 7
    ]
    i = 0
    while i < len(playerStats):
	    playerStats[i] = genStats
	    i += 1
	    print(playerStats)

genStats()

print(genStats)

#def round(playerHealth, roundTime):
    #if playerHealth > 0 and roundTime > 0:
        #roundEnd = False
    #elif playerHealth <= 0 and roundTime <= 0
        #roundEnd = True
        
    #if roundEnd = True:
        #print("K.O") and RoundScore + 1         
    
#round(75, 0)
     
    
    
    
    
    
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