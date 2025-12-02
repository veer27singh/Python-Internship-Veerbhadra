"""Festival Reminder Bot
Simple date-based reminder that checks upcoming festival dates.
Optional: if `plyer` is installed, desktop notifications can be used.
"""
from datetime import datetime
import json
import os

DEFAULT_FESTIVALS = {
    "Diwali": "2025-10-20",
    "Holi": "2025-03-14",
    "Eid": "2025-04-10",
    "Christmas": "2025-12-25"
}

FESTIVAL_FILE = 'festivals.json'

def load_festivals():
    if os.path.exists(FESTIVAL_FILE):
        with open(FESTIVAL_FILE, 'r') as f:
            return json.load(f)
    return DEFAULT_FESTIVALS.copy()

def save_festivals(data):
    with open(FESTIVAL_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def check_reminders(festivals):
    today = datetime.now().date()
    reminders = []
    for fest, date_str in festivals.items():
        try:
            fest_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            continue
        delta = (fest_date - today).days
        if delta == 0:
            reminders.append((fest, 'today'))
        elif 0 < delta <= 7:
            reminders.append((fest, f'in {delta} day(s)'))
    return reminders

if __name__ == '__main__':
    festivals = load_festivals()
    print("Festival Reminder Bot\n")
    print("Current saved festivals:")
    for k, v in festivals.items():
        print(f"- {k}: {v}")
    print()
    reminders = check_reminders(festivals)
    if reminders:
        for fest, when in reminders:
            print(f"Reminder: {fest} is {when}.")
    else:
        print("No immediate reminders (within 7 days).")

    choice = input('\nWould you like to add a new festival? (yes/no): ').strip().lower()
    if choice in ('yes','y'):
        name = input('Festival name: ').strip()
        date = input('Festival date (YYYY-MM-DD): ').strip()
        festivals[name] = date
        save_festivals(festivals)
        print('Saved. Run the script again to see reminders.')
