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

#Declare all the counter variables
usCounter = 0
chinaCounter = 0
russiaCounter = 0
franceCounter = 0
finlandCounter = 0
iranCounter = 0
brazilCounter = 0
philCounter = 0
polandCounter = 0
nigeriaCounter = 0
ukraineCounter = 0
boliviaCounter = 0
congoCounter = 0
thailandCounter = 0
greeceCounter = 0
indoCounter = 0
zambiaCounter = 0
croatiaCounter = 0
canadaCounter = 0
germanyCounter = 0
japanCounter = 0
ivCoastCounter = 0
denmarkCounter = 0
palCounter = 0
panamaCounter = 0
portugalCounter = 0
tanCounter = 0
ethiopiaCounter = 0
ukCounter = 0
libyaCounter = 0
vietnamCounter = 0
swedenCounter = 0
comorosCounter = 0
colombiaCounter = 0
zambiaCounter = 0
bangladashCounter = 0
madaCounter = 0
peruCounter = 0


#using the for loop, loop through the entire data
for line in data:
   # print line (notes for myself)

    #split each line in the data by a comma and store it in the newVar variable
    newVar = line.split(",")
    
#    print newVar[0] #when storing in database use different names (notes for myself)
    
#    print newVar[1] (notes for myself)
    
 #   print newVar[2] (notes for myself)
    #using the if/elif statements go through all the countries 
    #listed in the array and increment the counter by one if the countries are repeated.
    if newVar[1] == "United States":
        usCounter = usCounter + 1
     #   print newVar[1]
        
    elif newVar[1] == "China":
        chinaCounter = chinaCounter + 1
     #   print newVar[1]
    
    elif newVar[1] == "Russia":
        russiaCounter = russiaCounter + 1
     #   print newVar[1]
    elif newVar[1] == "France":
        franceCounter = franceCounter + 1
     #   print newVar[1]
    elif newVar[1] == "Finland":
        finlandCounter = finlandCounter + 1
     #   print newVar[1]
    elif newVar[1] == "Iran":
        iranCounter = iranCounter + 1
      #  print newVar[1]
    elif newVar[1] == "Brazil":
        brazilCounter = brazilCounter + 1
      #  print newVar[1]
    elif newVar[1] == "Philippines":
        philCounter = philCounter + 1
     #   print newVar[1]
    elif newVar[1] == "Poland":
        polandCounter = polandCounter + 1
      #  print newVar[1]
    elif newVar[1] == "Nigeria":
        nigeriaCounter = nigeriaCounter + 1
      #  print newVar[1]
    elif newVar[1] == "Ukraine":
        ukraineCounter = ukraineCounter + 1
      #  print newVar[1]
    elif newVar[1] == "Bolivia":
        boliviaCounter = boliviaCounter + 1
      #  print newVar[1]
    elif newVar[1] == "Democratic Republic of the Congo":
        congoCounter = congoCounter + 1
      #  print newVar[1]
    elif newVar[1] == "Thailand":
        thailandCounter = thailandCounter + 1
      #  print newVar[1]
    elif newVar[1] == "Greece":
        greeceCounter = greeceCounter + 1
      #  print newVar[1]
    elif newVar[1] == "Indonesia":
        indoCounter = indoCounter + 1
      #  print newVar[1]
    elif newVar[1] == "Zambia":
        zambiaCounter = zambiaCounter + 1
      #  print newVar[1]
    elif newVar[1] == "Croatia":
        croatiaCounter = croatiaCounter + 1
      #  print newVar[1]
    elif newVar[1] == "Canada":
        canadaCounter = canadaCounter + 1
      #  print newVar[1]
    elif newVar[1] == "Germany":
        germanyCounter = germanyCounter + 1
      #  print newVar[1]
    elif newVar[1] == "Japan":
        japanCounter = japanCounter + 1
      #  print newVar[1]
    elif newVar[1] == "Ivory Coast":
        ivCoastCounter = ivCoastCounter + 1
      #  print newVar[1]
    elif newVar[1] == "Denmark":
        denmarkCounter = denmarkCounter + 1
      #  print newVar[1]
    elif newVar[1] == "Palestinian Territory":
        palCounter = palCounter + 1
      #  print newVar[1]
    elif newVar[1] == "Panama":
        panamaCounter = panamaCounter + 1
      #  print newVar[1]
    elif newVar[1] == "Portugal":
        portugalCounter = portugalCounter + 1
      #  print newVar[1]
    elif newVar[1] == "Tanzania":
        tanCounter = tanCounter + 1
      #  print newVar[1]
    elif newVar[1] == "Ethiopia":
        ethiopiaCounter = ethiopiaCounter + 1
      #  print newVar[1]
    elif newVar[1] == "United Kingdom":
        ukCounter = ukCounter + 1
      #  print newVar[1]
    elif newVar[1] == "Libya":
        libyaCounter = libyaCounter + 1
      #  print newVar[1]
    elif newVar[1] == "Vietnam":
        vietnamCounter = vietnamCounter + 1
      #  print newVar[1]
    elif newVar[1] == "Sweden":
        swedenCounter = swedenCounter + 1
      #  print newVar[1]
    elif newVar[1] == "Comoros":
        comorosCounter = comorosCounter + 1
      #  print newVar[1]
    elif newVar[1] == "Zambia":
        zambiaCounter = zambiaCounter + 1
      #  print newVar[1]
    elif newVar[1] == "Bangladesh":
        polandCounter = bangladashCounter + 1
      #  print newVar[1]
    elif newVar[1] == "Madagascar":
        madaCounter = madaCounter + 1
        #print newVar[1]
    elif newVar[1] == "Peru":
        peruCounter = peruCounter + 1
      #  print newVar[1]

#print each counter
print usCounter
print chinaCounter
print russiaCounter
print franceCounter
print finlandCounter
print iranCounter
print brazilCounter
print philCounter
print polandCounter
print nigeriaCounter
print ukraineCounter
print boliviaCounter
print congoCounter
print thailandCounter
print greeceCounter
print indoCounter
print zambiaCounter
print croatiaCounter
print canadaCounter
print germanyCounter
print japanCounter
print ivCoastCounter
print denmarkCounter
print palCounter
print panamaCounter
print portugalCounter
print tanCounter
print ethiopiaCounter
print ukCounter
print libyaCounter
print vietnamCounter
print swedenCounter
print comorosCounter
print colombiaCounter
print zambiaCounter
print bangladashCounter
print madaCounter
print peruCounter
        
#If I had access to MySQL connector on my Mac, then I would have done this: 
    #read, open, write to a file, read by one country at a time
    #how to export data to CSV (comma separated version files) file, create another python file,  to import into database
    #select, name table, group by country ---Display
    #after printing it then write it in csv file
        
 #If had more time, then I would have done this: 
    #calculated the highest price and assigned it into a a highest variable using for loop and nested if/elif statements
    #then compared it to country, model, and the make of the car that has the highest price
    #displayed the highest valued cars as the best markets to go after. 
    
    #I would also calculate the lowest priced cars with the model, make, and country information. 
    #With the that information, the stakeholders could decide what cars to sell and what countries represent the best market.
        
        
        
        
        
        
        
        
#Notes for myself: 
#dilaraArray = []
#print data.split(",")
#some countries import more model and make
#1. which country represents the best market
#2. what cars to sell the most


