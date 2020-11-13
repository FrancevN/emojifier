from emojifier import kek
from emojifier_inverted import kek1


def test_emojifier():
    emoji = kek(input())
    emoji_inverted = kek1(emoji)
    assert emoji == emoji_inverted
