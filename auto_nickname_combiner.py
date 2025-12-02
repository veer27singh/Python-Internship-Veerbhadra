"""Auto Nickname Combiner
Generates multiple nickname options by combining parts of two names.
"""
import random

def generate_nicknames(first: str, last: str):
    first = first.strip()
    last = last.strip()
    nick1 = (first[:3] + last[-3:]) if len(first)>=3 and len(last)>=3 else first+last
    nick2 = (last[:3] + first[-3:]) if len(first)>=3 and len(last)>=3 else last+first
    nick3 = (first[:2] + last[:2] + 'X') if len(first)>=2 and len(last)>=2 else first+last+'X'
    nick4 = random.choice([nick1, nick2, nick3])
    return [nick1, nick2, nick3, nick4]

if __name__ == '__main__':
    first = input('Enter your first name: ')
    last = input('Enter your last name: ')
    print('\nGenerated Nicknames:')
    for n in generate_nicknames(first, last):
        print('-', n)
