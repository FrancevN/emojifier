emoji = {"a": "😀", "b": "😉", "c": "😂", "d": "🍪", "e": "😍", "f": "🤣", "g": "😊", "h": "🙏", "i": "💕", "j": "🤷",
         "k": "🔥", "l": "😭", "m": "😘", "n": "👍", "o": "🥰", "p": "😎", "q": "😆", "r": "😁", "s": "🤔", "t": "😜",
         "u": "🌟", "v": "💖", "w": "🪐", "x": "🌹", "y": "🎉", "z": "✨"}


def kek(em):
    return emoji.get(em)


stroka = input()
for em in stroka:
    print(kek(em), end="")
