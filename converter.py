import json
import sys


def to_unicode(code: int) -> str:
    """
    Convert a number to the corresponding unicode character.

    @params
        code: numeric corresponding to unicode hex code

    @return
        the unicode symbol corresponding to @code
    """
    MIN = 0
    MAX = 16^4 - 1
    assert 0 <= code <= MAX: "Number out of range"

    return chr(code)

def to_int(num: str) -> int:
    """
    Convert hexadecimal numeric string to a base 10 integer.

    @params
        num: hexadecimal string

    @return
        the base 10 integer corresponding to @num
    """
    return int(num, base=16)

def substitute(text: str, conversions: dict) -> str:
    """
    Replace all keys in @conversions in @text with the values in @conversions.

    @params
        conversions: dictionary of words to be replaced and words to replace them

    @return
        @text with desired substitutions made
    """
    for key, value in conversions.items():
        text = text.replace(key, value)

    return text


if __name__=='__main__':
    with open('conversions.json', 'r') as f:
        conversions = json.load(f)


