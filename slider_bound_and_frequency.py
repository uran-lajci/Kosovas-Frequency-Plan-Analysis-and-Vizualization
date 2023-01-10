def getLowerBoundAndFrequency(start_clr):
    if(start_clr == 0):
        lowerBound = 0
        lowerFrequency = "1 Hz"
    elif(start_clr == 10):
        lowerBound = 10 ** 3
        lowerFrequency = "1 KHz"
    elif(start_clr == 20):
        lowerBound = 10 ** 4
        lowerFrequency = "10 KHz"
    elif(start_clr == 30):
        lowerBound = 10 ** 5
        lowerFrequency = "100 KHz"
    elif(start_clr == 40):
        lowerBound = 10 ** 6
        lowerFrequency = "1 MHz"
    elif(start_clr == 50):
        lowerBound = 10 ** 7
        lowerFrequency = "10 MHz"
    elif(start_clr == 60):
        lowerBound = 10 ** 8
        lowerFrequency = "100 MHz"
    elif(start_clr == 70):
        lowerBound = 10 ** 9
        lowerFrequency = "1 GHz"
    elif(start_clr == 80):
        lowerBound = 10 ** 10
        lowerFrequency = "10 GHz"
    elif(start_clr == 90):
        lowerBound = 10 ** 11
        lowerFrequency = "100 GHz"
    elif(start_clr == 100):
        lowerBound = 10 ** 12
        lowerFrequency = "1 THz"
    elif(start_clr == 110):
        lowerBound = 10 ** 13
        lowerFrequency = "10 THz"

    return [lowerBound, lowerFrequency]

def getUpperBoundAndFrequency(end_clr):
    if(end_clr == 0):
        upperBound = 0
        upperFrequency = "1 Hz"
    elif(end_clr == 10):
        upperBound = 10 ** 3
        upperFrequency = "1 KHz"
    elif(end_clr == 20):
        upperBound = 10 ** 4
        upperFrequency = "10 KHz"
    elif(end_clr == 30):
        upperBound = 10 ** 5
        upperFrequency = "100 KHz"
    elif(end_clr == 40):
        upperBound = 10 ** 6
        upperFrequency = "1 MHz"
    elif(end_clr == 50):
        upperBound = 10 ** 7
        upperFrequency = "10 MHz"
    elif(end_clr == 60):
        upperBound = 10 ** 8
        upperFrequency = "100 MHz"
    elif(end_clr == 70):
        upperBound = 10 ** 9
        upperFrequency = "1 GHz"
    elif(end_clr == 80):
        upperBound = 10 ** 10
        upperFrequency = "10 GHz"
    elif(end_clr == 90):
        upperBound = 10 ** 11
        upperFrequency = "100 GHz"
    elif(end_clr == 100):
        upperBound = 10 ** 12
        upperFrequency = "1 THz"
    elif(end_clr == 110):
        upperBound = 10 ** 13
        upperFrequency = "10 THz"

    return [upperBound, upperFrequency]
