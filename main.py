import json

def main ():


    def getRollData():
        with open('RollData.json', 'r') as rolldata:
            global RollData
            RollData = json.load (rolldata)
        return RollData

    def modelsInBrand(Brand):
        for key in RollData[Brand]:
            print(key['model'])

    def modeChoice():
            modeChoice = int(input("""
Please choose operation mode\n
1- for Admin mode (to add new rolls top database)\n
2- for User mode 

input:  """))

            if modeChoice == 1:
                while True:
                    modeContinue = int(input("Would you like to add another roll? If yes, input 1 otherwise input 0 to exit"))
                    if modeContinue == 1:
                        adminMode()
                    elif modeContinue == 0:
                        print("successfully ended admin mode. Bye Bye!")
                        break
                    else:
                        print("Invalid input, please refer to the instructions above.")

            elif modeChoice == 2:
                userMode()
            else:
                print("invalid choice, please follow the instructions for choosing mode of operation")

    def userMode ():
        pass

    def adminMode ():
        pass

        def ISOWrite():
            ISORange = int(input("How many ISO's is the roll available in? (input an integer number)"))
            ISOValues = []
            for i in range(ISORange):
                ISO = input("Please write the ISO values of the roll, in increasing order")
                ISOValues.append(int(ISO))
            return ISOValues

        def typeWrite():

            rollType = int(input("""
Is the film color or black and white?-
input 0 for Black and White
input 1 for color
input:  """))

            while True:
                if rollType == 0:
                    is_Color = False
                    break
                elif rollType == 1:
                    is_Color = True
                    break
                else:
                    print ("Invalid input! please refer to instructions above to select film type")
            return is_Color

        def usageWrite():
            usageValues = []
            while True:
                usage = input("""
Please write the names of any of the following types of photography, where this roll can be used:
Portraits
Street
Landscape
General
Studio
or input 0 to end this process
input:  """)
                if usage.isnumeric() and int(usage) == 0:
                    break
                else:
                    usageValues.append(usage)

            return usageValues

        def highEndWrite():
            highEndArgument = int (input ("Does one roll of the film cost more than 7 USD? If Yes, input 1, if No input 0"))
            while True:
                if highEndArgument == 1:
                    is_HighEnd = True
                    break
                elif highEndArgument == 0:
                    is_HighEnd = False
                    break
                else:
                    print ("Invalid input, please refer to the instructions above")
            return is_HighEnd

        def prodcutionWrite():
            productionMode = int (input("Is this roll currently in production? Input 1 for yes, 0 for no"))

            while True:
                if productionMode == 1 :
                    is_inProduction = True
                    break
                elif productionMode == 0:
                    is_inProduction = False
                    break
                else:
                    print("Invalid input, please refer to the instructions above")
            return is_inProduction

        def negOrPos():
            negorposArg = int (input("""is the roll negative or positive (Slide film)?
Please input:
0 for Negative,
1 for Positive.
input:"""))
            if negorposArg == 0:
                return "Negative"
            elif negorposArg == 1:
                return "Slide"
            else:
                print("Invalid input, please refer to the instructions above")


        print("""
Hello! You are now in Admin mode.
Here you can add new rolls of film that you found are missing from the database.
Below are the list of Brands that already exist in the database. \n""")

        print (("   \n").join(RollData.keys()))

        brandChoice = (input ("\nPlease input the name of the Brand you would like to add a roll to.\n"))

        print ("Here are the models that already exist for the selected brand:\n",)
        modelsInBrand(brandChoice)
        modelName = input ("What is the name of the roll you'd like to add")

        ISOValues = ISOWrite()

        Color = typeWrite()

        usage = usageWrite()

        highend = highEndWrite()

        type = negOrPos()



        production = prodcutionWrite()

        newRoll = {
            "model": modelName,
            "ISO": ISOValues,
            "type": type,
            "Usage": usage,
            "is_HighEnd": highend,
            "is_Color": Color,
            "is_inProduction": production
        }

        RollData[brandChoice].append(newRoll)

        print ("Roll added succefully!!\n Thank you for your contribution.")

        with open('RollData.json', 'w') as writeData:
            json.dump(RollData, writeData, indent=4, separators=(',', ': '))

    getRollData()

    modeChoice()





main()
