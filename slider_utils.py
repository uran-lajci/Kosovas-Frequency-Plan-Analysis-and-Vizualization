def getSliderBounds():
    return """1 Hz &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; 1 KHz &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;
     10 KHz &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;&ensp;
     100 KHz &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;
     1 MHz &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;
     10 MHz &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;
     100 MHz &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;
     1 GHz &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;
     10 GHz &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;
     100 GHz &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;
     1 THz &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; 10 THz"""

def getLowerBoundAndFrequency(start_clr):
    if(start_clr == 0):
        return [0, "1 Hz"]
    elif(start_clr == 10):
        return [10 ** 3, "1 KHz"]
    elif(start_clr == 20):
        return [10 ** 4, "10 KHz"]
    elif(start_clr == 30):
        return [10 ** 5, "100 KHz"]
    elif(start_clr == 40):
        return [10 ** 6, "1 MHz"]
    elif(start_clr == 50):
        return [10 ** 7, "10 MHz"]
    elif(start_clr == 60):
        return [10 ** 8, "100 MHz"]
    elif(start_clr == 70):
        return [ 10 ** 9, "1 GHz"]
    elif(start_clr == 80):
        return [10 ** 10, "10 GHz"]
    elif(start_clr == 90):
        return [10 ** 11, "100 GHz"]
    elif(start_clr == 100):
        return [10 ** 12, "1 THz"]
    elif(start_clr == 110):
        return [10 ** 13, "10 THz"]

def getUpperBoundAndFrequency(end_clr):
    if(end_clr == 0):
        return [0, "1 Hz"]
    elif(end_clr == 10):
        return [10 ** 3, "1 KHz"]
    elif(end_clr == 20):
        return [10 ** 4, "10 KHz"]
    elif(end_clr == 30):
        return [10 ** 5, "100 KHz"]
    elif(end_clr == 40):
        return [10 ** 6, "1 MHz"]
    elif(end_clr == 50):
        return [10 ** 7, "10 MHz"]
    elif(end_clr == 60):
        return [10 ** 8, "100 MHz"]
    elif(end_clr == 70):
        return [10 ** 9, "1 GHz"]
    elif(end_clr == 80):
        return [10 ** 10, "10 GHz"]
    elif(end_clr == 90):
        return [10 ** 11, "100 GHz"]
    elif(end_clr == 100):
        return [10 ** 12, "1 THz"]
    elif(end_clr == 110):
        return [10 ** 13, "10 THz"]

