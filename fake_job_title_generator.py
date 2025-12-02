"""Fake Job Title Generator
Generates humorous or creative job titles using random selection.
"""
import random

ADJECTIVES = ["Global", "Certified", "Senior", "Dynamic", "Creative", "Master"]
ROLES = ["Meme", "Unicorn", "Vibes", "Innovation", "Dream", "Chaos"]
SUFFIXES = ["Engineer", "Strategist", "Architect", "Director", "Specialist"]

def generate_title():
    return f"{random.choice(ADJECTIVES)} {random.choice(ROLES)} {random.choice(SUFFIXES)}"

if __name__ == '__main__':
    print("Fake Job Title Generator\n")
    while True:
        print("Your Fake Job Title:", generate_title())
        again = input("Generate another? (yes/no): ").strip().lower()
        if again not in ('yes', 'y'):
            print('Goodbye!')
            break
