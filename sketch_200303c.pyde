import math

#1854 AUG - 1855 JuL

zymoticDiseases = [828,788,503,844,1725,2761,2120,1205,477,508,802,382]

woundsInjuries = [1,81,132,287,114,83,42,32,48,49,209,134]

otherCauses = [30,70,128,106,131,324,361,172,57,37,31,33]

totalSoildier = [30246.0,30290.0,30643.0,29736.0,32779.0,32393.0,30919.0,30107.0,32252.0,35473.0,38863.0,42647.0]

zymoticDiseasesProp = []
woundsInjuriesProp = []
otherCausesProp = []

#calculate the color sector value
 
for i in range(12):
    zymoticDiseasesProp.append(zymoticDiseases[i] / totalSoildier[i] * 1000)
    woundsInjuriesProp.append(woundsInjuries[i] / totalSoildier[i] * 1000)
    otherCausesProp.append(otherCauses[i] / totalSoildier[i] * 1000)
    


#this is the angle of each sector representing each month
angle = 360 / 12


#set up the basic attributes
def setup():
    
    #set the size of the canvas
    size(400,400)
    
    #set the background color
    background(255)
    
    stroke(2)
    
def draw():
    global angle
    
    deathList = []
    maxValue = -1
    
    for i in range(12):
        
        deathList = [zymoticDiseasesProp[i],woundsInjuriesProp[i],otherCausesProp[i]]
        
        while deathList:
            maxValue = max(deathList)
            
            if maxValue in zymoticDiseasesProp:
                #blue color
                fill(0,245,255)
            elif maxValue in woundsInjuriesProp:
                #black color
                fill(0,0,0)
            else:
                #purple color
                fill(155,48,255)  
            
            radius = math.sqrt(12 * maxValue / math.pi)
                
            arc(200,200,radius*20,radius*20,radians(angle * i), radians(angle * (i + 1)))

            deathList.remove(maxValue)

    
        
        
        

        
        
