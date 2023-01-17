def convertValues(value):
    # Conversion factors
    MHz = 10**6
    KHz = 10**3
    GHz = 10**9
    THz = 10**12

    # Create empty lists to store the converted values
    data_new = 0

    # print(value)

    if value >= THz:
        data_new = value/THz
        unit = "THz"
    elif value >= GHz:
        data_new = value/GHz
        unit = "GHz"
    elif value >= MHz:
        data_new = value/MHz
        unit = "MHz"
    elif value >= KHz:
        data_new = value/KHz
        unit = "KHz"
    else:
        data_new = value
        unit = "Hz"

    return [data_new, unit]
