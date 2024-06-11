ROMAN_DIGITS = {
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900,
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

def roman_to_int(roman: str) -> int:
    roman = roman.strip().upper()
    res = 0
    while roman:
        two_letters_probe = roman[0:2]
        one_letter_probe = roman[0]

        if two_letters_probe in ROMAN_DIGITS:
            res += ROMAN_DIGITS[two_letters_probe]
            roman = roman.removeprefix(two_letters_probe)
        else:
            res += ROMAN_DIGITS[one_letter_probe]
            roman = roman.removeprefix(one_letter_probe)

    return res
        
# 6 substract cases
assert roman_to_int('IV') == 4
assert roman_to_int('IX') == 9
assert roman_to_int('XL') == 40
assert roman_to_int('XC') == 90
assert roman_to_int('CD') == 400
assert roman_to_int('CM') == 900

# all substracts together
assert roman_to_int('CMCDXCXLIXIV') == 1443

# provided checks
assert roman_to_int('III') == 3
assert roman_to_int('LVIII') == 58
assert roman_to_int('MCMXCIV') == 1994
