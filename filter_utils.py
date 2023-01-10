def getLowerBoundAndUpperBound(frequencyBands):
    if frequencyBands == "3 - 30 kHz":
        return [3, 30]
    elif frequencyBands == "30 - 300 kHz":
        return [30, 300]
    elif frequencyBands == "300 kHz - 3 MHz":
        return [300, 30000]
    elif frequencyBands == "3 - 30 MHz":
        return [30000, 300000]
    elif frequencyBands == "30 MHz - 300 MHz":
        return [300000, 3000000]
    elif frequencyBands == "300 MHz - 3 GHz":
        return [300000, 3000000]
    elif frequencyBands == "3 - 30 GHz":
        return [3000000, 30000000]
    elif frequencyBands == "30 - 300 GHz":
        return [30000000, 300000000]


def getAbbreviationForLanguage(languageFromDataset):
    if languageFromDataset == 'English':
        return 'en'
    elif languageFromDataset == 'Albanian':
        return 'sq'
    elif languageFromDataset == 'Afrikaans':
        return 'af'
    elif languageFromDataset == 'Amharic':
        return 'am'
    elif languageFromDataset == 'Arabic':
        return 'ar'
    elif languageFromDataset == 'Armenian':
        return 'hy'
    elif languageFromDataset == 'Azerbaijani':
        return 'az'
    elif languageFromDataset == 'Basque':
        return 'eu'
    elif languageFromDataset == 'Belarusian':
        return 'be'
    elif languageFromDataset == 'Bengali':
        return 'bn'
    elif languageFromDataset == 'Bosnian':
        return 'bs'
    elif languageFromDataset == 'Bulgarian':
        return 'bg'
    elif languageFromDataset == 'Chinese':
        return 'zh-CN'
    elif languageFromDataset == 'Croatian':
        return 'hr'
    elif languageFromDataset == 'Danish':
        return'da'
    elif languageFromDataset == 'Dutch':
        return 'nl'
    elif languageFromDataset == 'Estonian':
        return 'et'
    elif languageFromDataset == 'Filipino':
        return 'tl'
    elif languageFromDataset == 'French':
        return 'fr'
    elif languageFromDataset == 'German':
        return 'de'
    elif languageFromDataset == 'Italian':
        return 'it'
    elif languageFromDataset == 'Japanese':
        return 'ja'
    elif languageFromDataset == 'Korean':
        return 'ko'
    elif languageFromDataset == 'Portuguese':
        return 'pt'
    elif languageFromDataset == 'Russian':
        return 'ru'
    elif languageFromDataset == 'Spanish':
        return 'es'
    elif languageFromDataset == 'Turkish':
        return 'tr'
    elif languageFromDataset == 'Urdu':
        return 'ur'
    
def getFrequencyBounds():
    return [
        '3 - 30 kHz',
                '30 - 300 kHz',
                '300 kHz - 3 MHz',
                '3 - 30 MHz',
                '30 MHz - 300 MHz',
                '300 MHz - 3 GHz',
                '3 - 30 GHz',
                '30 - 300 GHz']

def getLanguages():
    return [
        'English',
        'Albanian', 'Afrikaans','Amharic','Arabic','Armenian','Azerbaijani','Basque','Belarusian'
    ,'Bengali','Bosnian','Bulgarian','Chinese','Croatian','Danish','Dutch','Estonian','Filipino','French'
    ,'German','Italian','Japanese','Korean','Portuguese','Russian','Spanish','Turkish','Urdu'
    ]

def getColors():
    return [
        "aqua",
        "aquamarine",
        "azure",
        "beige",
        "bisque",
        "blanchedalmond",
        "blue",
        "blueviolet",
        "brown",
        "burlywood",
        "cadetblue",
        "chartreuse",
        "chocolate",
        "coral",
        "cornflowerblue",
        "cornsilk",
        "crimson",
        "cyan",
        "darkblue",
        "darkcyan",
        "darkgoldenrod",
        "darkgray",
        "darkgreen",
        "darkkhaki",
        "darkmagenta",
        "darkolivegreen",
        "darkorange",
        "darkorchid",
        "darkred",
        "darksalmon",
        "darkseagreen",
        "darkslateblue",
        "darkslategray",
        "darkturquoise",
        "darkviolet",
        "deeppink",
        "deepskyblue",
        "dimgray",
        "dodgerblue",
        "firebrick",
        "floralwhite",
        "forestgreen",
        "fuchsia",
        "gainsboro",
        "ghostwhite",
        "gold",
        "goldenrod",
        "gray",
        "green",
        "greenyellow",
        "honeydew",
        "hotpink",
        "indianred",
        "indigo",
        "ivory",
        "khaki",
        "lavender",
        "lavenderblush",
        "lawngreen",
        "lemonchiffon",
        "lightblue",
        "lightcoral",
        "lightcyan",
        "lightgoldenrodyellow",
        "lightgreen",
        "lightgrey",
        "lightpink",
        "lightsalmon",
        "lightseagreen",
        "lightskyblue",
        "lightslategray",
        "lightsteelblue",
        "lightyellow",
        "lime",
        "limegreen",
        "linen",
        "magenta",
        "maroon",
        "mediumaquamarine",
        "mediumblue",
        "mediumorchid",
        "mediumpurple",
        "mediumseagreen",
        "mediumslateblue",
        "mediumspringgreen",
        "mediumturquoise",
        "mediumvioletred",
        "midnightblue",
        "mintcream",
        "mistyrose",
        "moccasin",
        "navajowhite",
        "navy",
        "navyblue",
        "oldlace",
        "olive",
        "olivedrab",
        "orange",
        "orangered",
        "orchid",
        "palegoldenrod",
        "palegreen",
        "paleturquoise",
        "palevioletred",
        "papayawhip",
        "peachpuff",
        "peru",
        "pink",
        "plum",
        "powderblue",
        "purple",
        "red",
        "rosybrown",
        "royalblue",
        "saddlebrown",
        "salmon",
        "sandybrown",
        "seagreen",
        "seashell",
        "sienna",
        "silver",
        "skyblue",
        "slateblue",
        "slategray",
        "snow",
        "springgreen",
        "steelblue",
        "tan",
        "teal",
        "thistle",
        "tomato",
        "turquoise",
        "violet",
        "wheat",
        "white",
        "whitesmoke",
        "yellow",
        "yellowgreen",
    ]