mappings = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}
double_checks = {
    "V": "I",
    "X": "I",
    "L": "X",
    "C": "X",
    "D": "C",
    "M": "C"
}
exception_mappings = {
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900
}

def romanToInt(s: str) -> int:
    result = 0
    double_check_char = None
    for char in s[::-1]:
        if double_check_char and double_checks[double_check_char] == char:
            result += exception_mappings[char + double_check_char]
            double_check_char = None
        elif double_check_char:
            result += mappings[double_check_char]
            if char in double_checks:
                double_check_char = char
            else:
                result += mappings[char]
                double_check_char = None
        elif char in double_checks:
            double_check_char = char
        else:
            result += mappings[char]
    if double_check_char:
        result += mappings[double_check_char]
    return result

s = "MCMXCVI"

result = romanToInt(s)
print(result)