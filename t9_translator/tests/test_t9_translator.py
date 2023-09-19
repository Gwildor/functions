import pytest

from t9_translator.main import (
    InvalidAlphaString,
    InvalidNumericString,
    translate_alpha_to_numeric,
    translate_numeric_to_alpha,
)


T9_TEST_CASES = [
    ('hello world', "4433555'555666096667775553",),
    ('ban', "22'266",),
    ('hoi', '44666444',),
    ('python is cool', "7999844666'66044477770222666'666555",),
    ('word', '96667773',),
]


@pytest.mark.parametrize('input_string, output', T9_TEST_CASES)
def test_alpha_to_numeric(input_string, output):
    assert translate_alpha_to_numeric(input_string) == output


def test_alpha_to_numeric_non_alpha_raises_exception():
    with pytest.raises(InvalidAlphaString):
        translate_alpha_to_numeric('cool text!')

    with pytest.raises(InvalidAlphaString):
        translate_alpha_to_numeric('some@email')


@pytest.mark.parametrize('output, input_string', T9_TEST_CASES)
def test_numeric_to_alpha(output, input_string):
    assert translate_numeric_to_alpha(input_string) == output


def test_numeric_to_alpha_non_numeric_raises_exception():
    with pytest.raises(InvalidNumericString):
        translate_numeric_to_alpha('cool text!')

    with pytest.raises(InvalidNumericString):
        translate_numeric_to_alpha('1234')

    with pytest.raises(InvalidNumericString):
        # ' is required as pause character
        translate_numeric_to_alpha('22"3')


def test_numeric_to_alpha_rollover():
    """Test if the key rollover works.

    For example, pressing 2 once turns into A, but so should pressing 2 four
    times, as the 2 key has 3 characters.

    For characters in the middle or the end of the key, the start position is
    of course different, and thus the rollover point. For the h key, which is
    in position 2, 5 and 8 are the next positions."""

    input_string = '2' * 4 + '7' * 12 + '3' * 7 + '4' * 5

    output = translate_numeric_to_alpha(input_string)

    assert output == 'asdh'
