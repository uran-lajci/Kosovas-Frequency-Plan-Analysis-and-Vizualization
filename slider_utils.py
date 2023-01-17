def getLowerBoundAndFrequency(start_clr):
    if(start_clr == "1 Hz"):
        return [0, "1 Hz"]
    elif(start_clr == "1 KHz"):
        return [10 ** 3, "1 KHz"]
    elif(start_clr == "10 KHz"):
        return [10 ** 4, "10 KHz"]
    elif(start_clr == "100 KHz"):
        return [10 ** 5, "100 KHz"]
    elif(start_clr == "1 MHz"):
        return [10 ** 6, "1 MHz"]
    elif(start_clr == "10 MHz"):
        return [10 ** 7, "10 MHz"]
    elif(start_clr == "100 MHz"):
        return [10 ** 8, "100 MHz"]
    elif(start_clr == "1 GHz"):
        return [ 10 ** 9, "1 GHz"]
    elif(start_clr == "10 GHz"):
        return [10 ** 10, "10 GHz"]
    elif(start_clr == "100 GHz"):
        return [10 ** 11, "100 GHz"]
    elif(start_clr == "1 THz"):
        return [10 ** 12, "1 THz"]
    elif(start_clr == "10 THz"):
        return [10 ** 13, "10 THz"]

def getUpperBoundAndFrequency(end_clr):
    if(end_clr == "1 Hz"):
        return [0, "1 Hz"]
    elif(end_clr == "1 KHz"):
        return [10 ** 3, "1 KHz"]
    elif(end_clr == "10 KHz"):
        return [10 ** 4, "10 KHz"]
    elif(end_clr == "100 KHz"):
        return [10 ** 5, "100 KHz"]
    elif(end_clr == "1 MHz"):
        return [10 ** 6, "1 MHz"]
    elif(end_clr == "10 MHz"):
        return [10 ** 7, "10 MHz"]
    elif(end_clr == "100 MHz"):
        return [10 ** 8, "100 MHz"]
    elif(end_clr == "1 GHz"):
        return [10 ** 9, "1 GHz"]
    elif(end_clr == "10 GHz"):
        return [10 ** 10, "10 GHz"]
    elif(end_clr == "100 GHz"):
        return [10 ** 11, "100 GHz"]
    elif(end_clr == "1 THz"):
        return [10 ** 12, "1 THz"]
    elif(end_clr == "10 THz"):
        return [10 ** 13, "10 THz"]

