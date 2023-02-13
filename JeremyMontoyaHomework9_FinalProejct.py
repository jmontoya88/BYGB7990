#Jeremy Montoya Final Project

#created file for destination
destinationFile = 'C:\\Users\\Jeremy Montoya\\OneDrive\\Desktop\\Python\\KreweStylistsChart.csv'


def stylistEvalPay(colorScore,cutScore,specLevel1,specLevel2):
    #base values for starting the calculation
    basePay = 10
    ccIncrease = 4 #cut and color increase per level
    extensionIncrease = 6 #speciality indcrease per extensionLevel
    updoIncrease = 3
    #cut and color evaluation and salary calculation
    baseFloat = float(basePay)
    ccEvalTotal = float(colorScore) + float(cutScore)
    ccPay = ccEvalTotal * float(ccIncrease)
    spec1 = float(specLevel1) * float(extensionIncrease)
    spec2 = float(specLevel2) * float(updoIncrease)
    specPay = spec1 + spec2
    totalPay = baseFloat + ccPay + specPay
    return totalPay

with open(destinationFile, 'a', encoding='utf8') as newFile:
    #written as an append to continue adding new information
    header = ('Stylist,ColorScore,CutScore,ExtensionLevel,UpdoLevel,HourlyPay') + '\n'
    newFile.write(header)
    #dictionary to store the keys which are the stylist and the evaluations which are the values
    stylistScoreDict = {}

    stylistName = str(input('Please enter the stylist name:>>\n'))
        
    colorEval = input('Imput color level score (0-5):>>\n')
    cutEval = input('Imput cut level score(0-5):>>\n')
    spec1Eval = input('Imput extension specialist score(0-5):>>\n')
    spec2Eval = input('Imput Updo score(0-5):>>\n')

    evalScores = colorEval + ',' + cutEval + ',' + spec1Eval + ',' + spec2Eval
    stylistScoreDict[stylistName] = evalScores
    
    for stylist in stylistScoreDict:
            #we are retreiving the values fromt he dictionary by using the keys
            #key of stylist pulls the evalScores
            values = evalScores #split the line values for module calculation
            #taken from lab7
            valuesList = values.split(',')
            colorScore = valuesList[0]
            cutScore = valuesList[1]
            specLevel1 = valuesList[2]
            specLevel2 = valuesList[3]
            sysPay = stylistEvalPay(colorScore,cutScore,specLevel1,specLevel2)
            stylistOutput = stylist + ',' +colorScore + ',' + cutScore + ',' + specLevel1 + ',' +  specLevel2 + ',' + str(sysPay) + '\n' 
            newFile.write(stylistOutput)
    print('Done')


#view all stylist with evaluation scores and compensation in a dataframe
import pandas as pd

df = pd.read_csv('KreweStylistsChart.csv')
print(df)
