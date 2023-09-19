import itertools
import re

# Keys as dict keys, with the values being lists of the characters
# Amount of presses is index of the character + 1
DEFAULT_T9_MAPPING = {
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
    0: [' '],
}
PAUSE_CHARACTER = "'"

# Reverse mapping, where characters are the keys, and the values are tuples
# with the key and the amount of key presses required to get the character.
REVERSE_T9_MAPPING = {}

for key, characters in DEFAULT_T9_MAPPING.items():
    for index, character in enumerate(characters):
        REVERSE_T9_MAPPING[character] = (key, index + 1)


class InvalidAlphaString(Exception):
    def __init__(self, input_string: str):
        self.input_string = input_string

    def __str__(self):
        return (
            '"{}" does not consist of only alphabetic characters '
            '(A-Z and spaces)'.format(self.input_string)
        )


class InvalidNumericString(Exception):
    def __init__(self, input_string: str):
        self.input_string = input_string

    def __str__(self):
        return (
            '"{}" does not consist of only numeric characters '
            '(digits 2-9, digit 0 and the "{}" character for pauses)'.format(
                self.input_string, PAUSE_CHARACTER)
        )


def translate_alpha_to_numeric(input_string: str) -> str:
    """Convert an alpha string to a string representing the T9 presses.

    Characters are looked up in the mapping and a final output string is built.

    If the input string does not match the format, an InvalidInputString
    exception is raised.
    """

    input_string = input_string.lower()

    if not re.match('^[a-z ]+$', input_string):
        raise InvalidAlphaString(input_string)

    output_string = ''
    previous_key = None

    for character in input_string:
        key, press_count = REVERSE_T9_MAPPING[character]

        # We check the previous key to insert a pause character.
        # Otherwise, "c" (222) would give the same output as "ab" (22'2).
        if previous_key == key:
            output_string += PAUSE_CHARACTER

        previous_key = key

        # Multiplying a character gives the required string length
        output_string += str(key) * press_count

    return output_string


def translate_numeric_to_alpha(input_string: str) -> str:
    output_string = ''
    parts = []
    current_part = ''
    current_key = None

    if not re.match("^[0,2-9,{}]+$".format(PAUSE_CHARACTER), input_string):
        raise InvalidNumericString(input_string)

    for key, presses in itertools.groupby(input_string):
        if key == PAUSE_CHARACTER:
            continue

        characters = DEFAULT_T9_MAPPING[int(key)]

        # Using modulo easily deals with the key rollover.
        # For example, if a key contains 3 characters, then 4 turns into 1
        # again.
        press_count = len(list(presses)) % len(characters)

        # If the result of the modulo operation is 0, then the key was pressed
        # the same amount as the amount of characters on that key, so we reset
        # that to that amount. For example, if the key contains 3 characters,
        # and the key was pressed a multiple of 3, the modulo returns 0, but we
        # set it back to 3. It would still work without this though, as we
        # later subtract 1 for the index, and a negative index of -1 also
        # returns the last key. But handling this explicitely is a bit cleaner,
        # in my opinion.
        if press_count == 0:
            press_count = len(characters)

        character = characters[press_count - 1]

        output_string += character

    return output_string
