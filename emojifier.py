emoji = {"a": "😀", "b": "😉", "c": "😂", "d": "🍪", "e": "😍", "f": "🤣", "g": "😊", "h": "🙏", "i": "💕", "j": "🤷",
         "k": "🔥", "l": "😭", "m": "😘", "n": "👍", "o": "🥰", "p": "😎", "q": "😆", "r": "😁", "s": "🤔", "t": "😜",
         "u": "🌟", "v": "💖", "w": "🪐", "x": "🌹", "y": "🎉", "z": "✨"}


def demojify(emoji_text):
    res1 = ''
    for i in emoji_text:
        for key, value in emoji.items():
            if i == value:
                res1 += key
    return res1


def emojify(text):
    res = ''
    for y in text:
        res += emoji.get(y)
    return res
