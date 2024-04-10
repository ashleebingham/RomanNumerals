# Ashlee Bingham
# This program translates roman numerals into decimal numbers and decimal numbers into roman numerals

# Get input from user to know which conversion to run
iProgramNum = int(input("If you would like to convert roman numerals to decimal numbers type \"1\". If you would like to convert decimal numbers to roman numerals type \"2\": "))

# Convert roman numeral to Decimal Number
if (iProgramNum == 1) :

    # Get roman numeral
    sRomanNum = input("Please input a Roman Numeral: ")

    # Declare variables to hold decimal number, hold the last used value, and see if subtraction was done in the previous iteration of the loop
    iDecimalNum = 0
    iLastVal = 0
    bSub = False

    # Run loop for each char in the user roman numeral input
    for iCount in range(0, len(sRomanNum)) :

        # interate through chars in user input
        cCurrLetter = sRomanNum[iCount]

        # check for which value to add
        if (cCurrLetter == "M") :
            iValue = 1000
        elif(cCurrLetter == "D") :
            iValue = 500
        elif(cCurrLetter == "C") :
            iValue = 100
        elif(cCurrLetter == "L") :
            iValue = 50
        elif(cCurrLetter == "X") :
            iValue = 10
        elif(cCurrLetter == "V") :
            iValue = 5
        elif(cCurrLetter == "I") :
            iValue = 1
        else :
            # print user error and end program
            print("Invalid response. Only letters M, D, C, L, X, V, and I may be entered as part of a roman numeral. Please enter response again.")
            exit()

        # check if subtraction needs to be done
        if (iCount == 0) :
            # no subtraction needed in first iteration
            iDecimalNum += iValue
        elif (bSub == True) :
            # if subtraction was done in the previous iteration it can't be done this iteration
            bSub = False
            iDecimalNum += iValue
        elif (iLastVal < iValue) :
            # if the last used value is less than the current value then subtraction should be done
            iValue -= iLastVal
            # iLastVal is subtracted again because it was added in the previous iteration and needs to be removed
            iDecimalNum += iValue - iLastVal
            # subtraction was done so set bSub to True so it isn't repeated in the next iteration
            bSub = True
        else :
            # doesn't qualify for subtraction so add
            iDecimalNum += iValue

        # remember value from this iteration in the next in order to check if subtraction is needed
        iLastVal = iValue

    # print result
    print("The decimal number of the Roman Numeral " + sRomanNum + " is " + str(iDecimalNum))

# Convert decimal number to roman numeral
elif (iProgramNum == 2) :

    # test for user input errors
    bContinue = True
    try:
        # Get input and set as new variable so that original response is retained
        iNum = int(input("Please input a Decimal Numeral: "))
        iDecNum = iNum
        bContinue = False
    except:
        print("\nPlease enter a numeric whole number\n")

    # make lists of the values and chars of roman numerals as well as a list of numbers that indicate a need for subtraction
    lstRomVals = [1000, 500, 100, 50, 10, 5, 1]
    lstRomChar = ["M", "D", "C", "L", "X", "V", "I"]
    lstSubVals = [900, 400, 90, 40, 9, 4]

    # create string variable to hold the roman numeral
    sRomanNum = ""
    
    # iterate through all possible values/chars
    for iCount in range(0, len(lstRomVals)) :

        # check if subtraction is needed
        for i in range(0, len(lstSubVals)) :
            if (iDecNum >= lstSubVals[i] and iDecNum < lstRomVals[i]) :
                # if iDecNum is within this range a value should be subtracted
                if (i == 0 or i == 1) :
                    # first 2 numbers in lstSubVals are the results of subtracting a roman numeral value by 100
                    sRomanNum +=  "C" + lstRomChar[i]
                    iDecNum -= lstSubVals[i]
                elif (i == 2 or i == 3) :
                    # subtraction by 10 is needed
                    sRomanNum +=  "X" + lstRomChar[i]
                    iDecNum -= lstSubVals[i]
                else :
                    # subtraction by 1 is needed
                    sRomanNum +=  "I" + lstRomChar[i]
                    iDecNum -= lstSubVals[i]

        # if no subtraction is needed then replace roman numeral value with its equivalant roman numeral char
        while (iDecNum >= lstRomVals[iCount]) :
            sRomanNum += lstRomChar[iCount]
            iDecNum -= lstRomVals[iCount]

    # print result
    print("The Roman Numeral of " + str(iNum) + " is " + sRomanNum)

else :
    print("Invalid response. Please enter \"1\" or \"2\".")

