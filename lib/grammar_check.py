def grammar_check(text):
    if type(text) is not str or text == '':
        raise Exception("Please enter a valid text")

    first_letter_valid = text[0].isupper()
    last_character_valid = text[-1] in '!?.'
    if first_letter_valid and last_character_valid:
        return 'Your grammar is ok!'
    else:
        return 'Your grammar is bad!'
