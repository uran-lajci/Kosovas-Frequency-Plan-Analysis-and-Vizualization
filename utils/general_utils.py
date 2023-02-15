import re

def convertValueUnit(value, unit):
    return str(value) + " " + unit

def convertValues(value):
    units = [("THz", 10 ** 12), ("GHz", 10 ** 9), ("MHz", 10 ** 6), ("KHz", 10 ** 3), ("Hz", 1)]
    for unit, factor in units:
        if value >= factor:
            converted_value = value / factor
            return [converted_value, unit]
    return [value, "Hz"]

def convertValuesAsString(value):
    converted_value, unit = convertValues(value)
    return convertValueUnit(converted_value, unit)

def checkWordInFile(file_path, word):
    with open(file_path, 'r') as file:
        file_contents = file.read()
        if re.search(word, file_contents):
            return True
    return False

def convertToHz(frequency, frequency_scale):
    scale_factors = {
        'KHz': 1e3,
        'MHz': 1e6,
        'GHz': 1e9
    }
    return frequency * scale_factors[frequency_scale]

def convertFrequencyToString(frequency):
    if frequency < 1000:
        return f"{frequency:.0f} Hz"
    elif frequency < 1e6:
        return f"{frequency/1e3:.1f} kHz"
    elif frequency < 1e9:
        return f"{frequency/1e6:.3f} MHz"
    else:
        return f"{frequency/1e9:.6f} GHz"
