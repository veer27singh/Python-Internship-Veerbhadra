"""Emoji Mood Responder
Simple console program that maps moods to emojis and messages.
"""
def respond_mood(mood: str) -> str:
    moods = {
        "happy": ("😊", "Great! Keep smiling!"),
        "sad": ("😢", "It's okay, better days are coming."),
        "angry": ("😡", "Take a deep breath… it will pass."),
        "excited": ("🤩", "Awesome! Enjoy the moment!"),
        "bored": ("😐", "Maybe try something fun or creative!"),
        "tired": ("🥱", "Get some rest, you deserve it!")
    }
    key = mood.strip().lower()
    if key in moods:
        emoji, message = moods[key]
        return f"{emoji}  {message}"
    return "🙂 I may not know that mood, but I hope you have a good day!"

if __name__ == '__main__':
    try:
        mood = input("How are you feeling today? ")
        print(respond_mood(mood))
    except KeyboardInterrupt:
        print('\nGoodbye!')
