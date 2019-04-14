import json

def main ():

    def userMode ():
        pass


    def adminMode ():
        pass

    modeChoice = int (input ("""
    Please choose operation mode\n
    1- for Admin mode (to add new rolls top database)\n
    2- for User mode """))

    while True:
        if modeChoice == 1:
            adminMode()
            break
        elif modeChoice == 2:
            userMode()
            break
        else:
            print ("invalid choice, please follow the instructions for choosing mode of operation")


main()