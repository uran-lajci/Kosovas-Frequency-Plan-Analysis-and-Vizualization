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
