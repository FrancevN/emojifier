from emojifier import kek
from emojifier_inverted import kek1


def test_emojifier():
    emoji = kek('spotify')
    emoji_inverted = kek1(kek('spotify'))
    assert emoji == emoji_inverted
