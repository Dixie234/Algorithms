thou_mapping = {
    "1": "M",
    "2": "MM",
    "3": "MMM"
}
hund_mapping = {
    "0": "",
    "1": "C",
    "2": "CC",
    "3": "CCC",
    "4": "CD",
    "5": "D",
    "6": "DC",
    "7": "DCC",
    "8": "DCCC",
    "9": "CM"
}
tens_mapping = {
    "0": "",
    "1": "X",
    "2": "XX",
    "3": "XXX",
    "4": "XL",
    "5": "L",
    "6": "LX",
    "7": "LXX",
    "8": "LXXX",
    "9": "XC"
}
sing_mapping = {
    "0": "",
    "1": "I",
    "2": "II",
    "3": "III",
    "4": "IV",
    "5": "V",
    "6": "VI",
    "7": "VII",
    "8": "VIII",
    "9": "IX"
}
symbol_mapping = {
    4: thou_mapping,
    3: hund_mapping,
    2: tens_mapping,
    1: sing_mapping
}

def intToRoman(num: int) -> str:
    num_str = str(num)
    start = len(num_str)
    result = ""
    for char in num_str:
        result += symbol_mapping[start][char]
        start -= 1
    return result

def intToRoman_simple(num: int) -> str:
    roman_numerals = [
    ("M", 1000),
    ("CM", 900),
    ("D", 500),
    ("CD", 400),
    ("C", 100),
    ("XC", 90),
    ("L", 50),
    ("XL", 40),
    ("X", 10),
    ("IX", 9),
    ("V", 5),
    ("IV", 4),
    ("I", 1)
] 
    result = ""
    for symbol, value in roman_numerals:
        while num >= value:
            result += symbol
            num -= value
            
    return result

num = 10
result = intToRoman(num)
print(result)
