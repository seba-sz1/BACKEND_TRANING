from random import choice


def genPass(length, upperCase, includeDigits, includeSpecjals):
    """Options 0:none; 1:large letters, 2:numbers, 3:specjals"""
    num = 'abcdefghijklmnopqrstuvwxyz'
    if upperCase:
        num += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if includeDigits:
        num += "0123456789"
    if includeSpecjals:
        num += '!"#$%&()*+,-./:;<=>?@'
    return ''.join(choice(num) for _ in range(length + 1))
