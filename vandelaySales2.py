'''
Created on Apr 29, 2018

@author: dilara
'''

#import the url library
import urllib
#the url of the api 
url = "https://my.api.mockaroo.com/dilara-api.json?key=e6ac1da0"
#retrieves the data from the api using the url library 
response = urllib.urlopen(url)
#data = response.read()

#assign the retrieved data from api to data variable
data = response.readlines()

#Declare all the counter variables for the make of the car
dodgeCounter = 0
suzukiCounter = 0
toyotaCounter = 0
fordCounter = 0
subaruCounter = 0
chevCounter = 0
ponCounter = 0
gmcCounter = 0
isuzuCounter = 0
porscheCounter = 0
hondaCounter = 0
oldCounter = 0
jaguarCounter = 0
saabCounter = 0
chryslerCounter = 0
lrCounter = 0
smartCounter = 0
linCounter = 0
mercuryCounter = 0
lexusCounter = 0
lotusCounter = 0
acuraCounter = 0
hummerCounter = 0
volkCounter = 0
cadillacCounter = 0
maseratiCounter = 0
mBenzCounter = 0
bentleyCounter = 0
nissanCounter = 0
infinitiCounter = 0
plyCounter = 0
mitCounter = 0
buickCounter = 0
mazdaCounter = 0
volvoCounter = 0
kiaCounter = 0

#using the for loop, loop through the entire data
for line in data:
    #split each line in the data by a comma and store it in the newVar variable
    newVar = line.split(",")
    
    #using the if/elif statements go through all the types of make of the cars 
    #listed in the array and increment the counter by one if the make is repeated
    if newVar[3] == "Dodge":
        dodgeCounter = dodgeCounter + 1
     #   print newVar[3]
        
    if newVar[3] == "Suzuki":
        suzukiCounter = suzukiCounter + 1
     #   print newVar[3]
    
    if newVar[3] == "Toyota":
        toyotaCounter = toyotaCounter + 1
            
      #   print newVar[3]
    if newVar[3] == "Ford":
        fordCounter = fordCounter + 1
     #   print newVar[3]
    if newVar[3] == "Subaru":
        subaruCounter = subaruCounter + 1
      #   print newVar[3]
    if newVar[3] == "Chevrolet":
        chevCounter = chevCounter + 1
     #   print newVar[3]
    if newVar[3] == "Pontiac":
        ponCounter = ponCounter + 1
    if newVar[3] == "GMC":
        gmcCounter = gmcCounter + 1
    if newVar[3] == "Isuzu":   
        isuzuCounter = isuzuCounter + 1
    if newVar[3] == "Porsche":    
        porsccheCounter = porscheCounter + 1
    if newVar[3] == "Honda":
        hondaCounter = hondaCounter + 1  
    if newVar[3] == "Oldsmobile":    
        oldCounter = oldCounter + 1
    if newVar[3] == "Jaguar":    
        jaguarCounter = jaguarCounter + 1
    if newVar[3] == "Saab":    
        saabCounter = saabCounter + 1
    if newVar[3] == "Chrysler":    
        chryslerCounter = chryslerCounter + 1
    if newVar[3] == "Land Rover":    
        lrCounter = lrCounter + 1
    if newVar[3] == "Smart":    
        smartCounter = smartCounter + 1
    if newVar[3] == "Lincoln":    
        linCounter = linCounter + 1
    if newVar[3] == "Mercury":    
        mercuryCounter = mercuryCounter + 1
    if newVar[3] == "Lexus":    
        lexusCounter = lexusCounter + 1
    if newVar[3] == "Lotus":    
        lotusCounter = lotusCounter + 1
    if newVar[3] == "Acura":    
        acuraCounter = acuraCounter + 1
    if newVar[3] == "Hummer":    
        hummerCounter = hummerCounter + 1
    if newVar[3] == "Volkswagen":    
        volkCounter = volkCounter + 1
    if newVar[3] == "Cadillac":    
        cadillacCounter = cadillacCounter + 1
    if newVar[3] == "Maserati":    
        maseratiCounter = maseratiCounter + 1
    if newVar[3] == "Mercedes-Benz":    
        mBenzCounter = mBenzCounter + 1
    if newVar[3] == "Bentley":    
        bentleyCounter = bentleyCounter + 1
    if newVar[3] == "Nissan":    
        nissanCounter = nissanCounter + 1
    if newVar[3] == "Infiniti":    
        infinitiCounter = infinitiCounter + 1   
    if newVar[3] == "Plymouth":
        plyCounter = plyCounter + 1
    if newVar[3] == "Mitsubishi":
        mitCounter = mitCounter + 1
    if newVar[3] == "Buick":
        buickCounter = buickCounter + 1
    if newVar[3] == "Mazda":
        mazdaCounter = mazdaCounter + 1
    if newVar[3] == "Volvo":
        volvoCounter = volvoCounter + 1
    if newVar[3] == "Kia":
        kiaCounter = kiaCounter + 1



#print each counter
print dodgeCounter
print suzukiCounter
print toyotaCounter
print fordCounter
print subaruCounter
print chevCounter
print ponCounter
print gmcCounter
print isuzuCounter
print hondaCounter
print oldCounter
print jaguarCounter
print saabCounter
print chryslerCounter
print lrCounter
print smartCounter
print linCounter
print mercuryCounter
print lexusCounter
print lotusCounter
print acuraCounter
print hummerCounter
print volkCounter    
print cadillacCounter
print maseratiCounter
print mBenzCounter
print bentleyCounter
print nissanCounter
print infinitiCounter
print plyCounter
print mitCounter
print buickCounter
print mazdaCounter
print volvoCounter
print kiaCounter


 #If had more time, then I would have done this: 
    #calculated the highest price and assigned it into a a highest variable using for loop and nested if/elif statements
    #then compared it to country, model, and the make of the car that has the highest price
    #displayed the highest valued cars as the best markets to go after. 
    
    #I would also calculate the lowest priced cars with the model, make, and country information. 
    #With the that information, the stakeholders could decide what cars to sell and what countries represent the best market.
        
        






#My notes:
#some countries import more model and make
#1. which country represents the best market
#2. what cars to sell the most = ford & nissan
#read, open, write to a file, read by one country at a time
#how to export data to CSV (comma separated version files) file, create another php file,  to import into database
#select, name table, group by country ---Display
#after printing it then write it in csv file
#

