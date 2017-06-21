"""
--- NUMBER REGULAR EXPRESSIONS ---
VALID_NUMBER: [MIXED_NUMBER | FRACTION | DECIMAL | PERCENTAGE | INTEGER]
DECIMAL: INTEGER.UNFORMATTED_INT
PERCENTAGE: [DECIMAL | MIXED_NUMBER | FRACTION]%
MIXED_NUMBER: INTEGER FRACTION
FRACTION: INTEGER/NON_ZERO_INT
NON_ZERO_INT: SIGN[NON_ZERO_DIGIT]([DIGIT]{0,2}(,DIGIT{3})*|[UNFORMATTED_INT])?
INTEGER: SIGN[FORMATTED_INT | UNFORMATTED_INT]
FORMATTED_INT: [DIGIT]{1,3}[,DIGIT{3}]+
UNFORMATTED_INT: [DIGIT]*
DIGIT: [0-9]
NON_ZERO_DIGIT: [1-9]
SIGN: -{0,1}
EXPONENT: [DECIMAL | INTEGER]e+{0,1}[INTEGER]

"""
import re

SIGN = r'-?'
DIGIT = r'[0-9]'
NON_ZERO_DIGIT = r'[1-9]'
UNFORMATTED_INT = re.compile("{digit}*".format(digit=DIGIT))
FORMATTED_INT = re.compile("{digit}{{1,3}}(?:,{digit}{{3}})+".format(digit=DIGIT))
INTEGER = re.compile("({sign}(?:{formatted}|{unformatted}))".format(sign=SIGN, formatted=FORMATTED_INT.pattern, unformatted=UNFORMATTED_INT.pattern))
NON_ZERO_INT = re.compile("({sign}{non_zero}(?:{digit}{{0,2}}(?:,{digit}{{3}})+|{unformatted})?)".format(sign=SIGN, non_zero=NON_ZERO_DIGIT, digit=DIGIT, unformatted=UNFORMATTED_INT.pattern))
FRACTION = re.compile("({integer}/{non_zero})".format(integer=INTEGER.pattern, non_zero=NON_ZERO_INT.pattern))
MIXED_NUMBER = re.compile("({integer}) +({fraction})".format(integer=INTEGER.pattern, fraction=FRACTION.pattern))
DECIMAL = re.compile("({integer}\.{unformatted})".format(integer=INTEGER.pattern, unformatted=UNFORMATTED_INT.pattern))
VALID_NUMBER = re.compile("({decimal}|{mixed_number}|{fraction}|{integer})".format(decimal=DECIMAL.pattern, mixed_number=MIXED_NUMBER.pattern, fraction=FRACTION.pattern, integer=INTEGER.pattern))
PERCENTAGE = re.compile("({num})%".format(num=VALID_NUMBER.pattern))
EXPONENT = re.compile("((?:{decimal}|{integer})e\+?{integer})".format(decimal=DECIMAL.pattern, integer=INTEGER.pattern))

def extract_value(text):
    return parse_valid_number(text)

def parse_valid_number(text):
    try:
        return parse_exponent(text) or parse_mixed_number(text) or parse_fraction(text) or parse_percentage(text) or parse_decimal(text) or parse_integer(text)
    except Exception:
        return None

def parse_integer(text):
    match = INTEGER.search(text)
    return match and float(match.group(1).replace(',', ''))

def parse_decimal(text):
    match = DECIMAL.search(text)
    return match and float(match.group(1).replace(',', ''))

def parse_fraction(text):
    match = FRACTION.search(text)
    return match and parse_integer(match.group(2)) / parse_integer(match.group(3))

def parse_mixed_number(text):
    match = MIXED_NUMBER.search(text)
    if(match):
        number = parse_integer(match.group(1))
        return abs(number) + parse_fraction(match.group(3)) * (-1 if number < 0 else 1)
    return None

def parse_percentage(text):
    match = PERCENTAGE.search(text)
    return match and extract_value(match.group(1)) / 100

def parse_exponent(text):
    match = EXPONENT.search(text)
    return match and eval(match.group(1))