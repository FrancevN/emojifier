emoji = {"a": "😀", "b": "😉", "c": "😂", "d": "❤", "e": "😍", "f": "🤣", "g": "😊", "h": "🙏", "i": "💕", "j": "🤷",
          "k": "🔥", "l": "😭", "m": "😘", "n": "👍", "o": "🥰", "p": "😎", "q": "😆", "r": "😁", "s": "🤔", "t": "😜",
          "u": "🌟", "v": "💖", "w": "🪐", "x": "🌹", "y": "🎉", "z": "✨"}
def kek(a):
    for key, value in emoji.items():
        if key == a:
            return value
stroka = input()
for a in stroka:
    print(kek(a))

