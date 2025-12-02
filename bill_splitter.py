"""Bill Splitter for Groups
Splits a bill among a number of people with validation and optional tips.
"""
def split_bill(total: float, people: int, tip_percent: float = 0.0):
    if people <= 0:
        raise ValueError('Number of people must be > 0')
    total_with_tip = total * (1 + tip_percent/100)
    share = total_with_tip / people
    return round(share, 2)

if __name__ == '__main__':
    try:
        total_bill = float(input('Enter total bill amount: '))
        people = int(input('Enter number of people: '))
        tip = input('Tip percentage (press enter for 0): ').strip()
        tip = float(tip) if tip else 0.0
        per_person = split_bill(total_bill, people, tip)
        print(f'Each person should pay: ₹{per_person}')
    except Exception as e:
        print('Error:', e)
