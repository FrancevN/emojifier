emoji = {"a": "😀", "b": "😉", "c": "😂", "d": "🍪", "e": "😍", "f": "🤣", "g": "😊", "h": "🙏", "i": "💕", "j": "🤷",
         "k": "🔥", "l": "😭", "m": "😘", "n": "👍", "o": "🥰", "p": "😎", "q": "😆", "r": "😁", "s": "🤔", "t": "😜",
         "u": "🌟", "v": "💖", "w": "🪐", "x": "🌹", "y": "🎉", "z": "✨"}
def kek(em):
    for key, value in emoji.items():
        if em == value:
            return key
str = input()
for em in str:
    print(kek(em), end="")
