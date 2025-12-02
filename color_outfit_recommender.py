"""Color Psychology Outfit Recommender
Recommends outfit colors based on user's mood using a simple rule-set.
"""
MOOD_TO_COLOR = {
    "happy": "Yellow",
    "sad": "Blue",
    "angry": "Red",
    "relaxed": "Green",
    "energetic": "Orange",
    "stressed": "Light Blue"
}

COLOR_TO_OUTFIT = {
    "Yellow": "a bright yellow t-shirt",
    "Blue": "a calming blue hoodie",
    "Red": "a bold red jacket",
    "Green": "a soothing green shirt",
    "Orange": "an energetic orange jersey",
    "Light Blue": "a peaceful sky-blue kurta"
}

def recommend(mood: str):
    key = mood.strip().lower()
    color = MOOD_TO_COLOR.get(key)
    if color:
        outfit = COLOR_TO_OUTFIT.get(color, 'an item in that color')
        return color, outfit
    return None, None

if __name__ == '__main__':
    mood = input('Enter your mood: ')
    color, outfit = recommend(mood)
    if color:
        print(f"\nRecommended Color: {color}")
        print(f"Suggested Outfit: Wear {outfit} today!")
    else:
        print("Mood not recognized, try 'happy', 'sad', 'relaxed', etc.")
