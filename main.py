import json

def main ():

    def getRollData():
        with open('RollData.json', 'r') as fp:
            global RollData
            RollData = json.load (fp)


    def userMode ():
        pass


    def adminMode ():
        print("""
        Hello! You are now in Admin mode where you can add new rolls of film that you found are missing from the database,
        Here are the list of Brands that you can add to.""")
        print ("""
        1-Kodak
        2-FujiColor
        3-Lomography
        4-Cinestill
        5-Rollei
        6-Ilford
        7-Kentmere
        8-Foma
        9-Dubblefilm
        10-Streetcandy
        11-JCH
        12-Kosmophoto
        13-Santa
        14-Adox
        15-Revolog
        """)

        brandChoice = int (input ("Please select the number of the corresponding brand that you'd like to add a roll to\n"))

        modelName = input ("What is the name of the roll you'd like to add")
        ISORange = int(input ("How many ISO's is the roll available in? (input an integer number)"))
        ISOValues = ()
        for i in range(ISORange):
            n = input("Please write the ISO values of the roll, in increasing order")
            ISOValues.append(int(n))
        

    getRollData()

    modeChoice = int (input ("""
    Please choose operation mode\n
    1- for Admin mode (to add new rolls top database)\n
    2- for User mode 
    """))

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
