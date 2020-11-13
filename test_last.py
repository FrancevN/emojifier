from emojifier import emojify, demojify
import pytest


@pytest.mark.parametrize('_input', ['test', 'a'])
def test_demojifier(_input):
    res = demojify(emojify(_input))
    assert _input == res


@pytest.mark.parametrize('_input', [('a', "😀"), ['test', '😜😍🤔😜']])
def test_emojifier(_input):
    res = emojify(_input[0])
    assert _input[1] == res
