def getFrequencyBounds():
    return {
        "1 Hz": 0,
        "1 KHz": 10 ** 3,
        "10 KHz": 10 ** 4,
        "100 KHz": 10 ** 5,
        "1 MHz": 10 ** 6,
        "10 MHz": 10 ** 7,
        "100 MHz": 10 ** 8,
        "1 GHz": 10 ** 9,
        "10 GHz": 10 ** 10,
        "100 GHz": 10 ** 11,
        "1 THz": 10 ** 12,
        "10 THz": 10 ** 13
    }

def getLowerBoundAndFrequency(start_clr):
    freq_bounds = getFrequencyBounds()
    if start_clr in freq_bounds:
        return [freq_bounds[start_clr], start_clr]

def getUpperBoundAndFrequency(end_clr):
    freq_bounds = getFrequencyBounds()
    if end_clr in freq_bounds:
        return [freq_bounds[end_clr], end_clr]