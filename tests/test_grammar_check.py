from lib.grammar_check import *
import pytest

def test_grammar_check_():
    assert grammar_check

def test_grammar_check_returns_string():
    assert type(grammar_check('text')) == str

def test_grammar_check_no_capital_letter():
    assert grammar_check('text.') == 'Your grammar is bad!'

def test_grammar_check_no_valid_character():
    assert grammar_check('Text') == 'Your grammar is bad!'

def test_grammar_check_valid_capital_and_last_character():
    assert grammar_check('Text.') == 'Your grammar is ok!'

def test_grammar_check_input_none():
    with pytest.raises(Exception) as err:
        grammar_check(None)
    error_message = str(err.value)
    assert error_message == "Please enter a valid text"

def test_grammar_check_input_empty():
    with pytest.raises(Exception) as err:
        grammar_check('')
    error_message = str(err.value)
    assert error_message == "Please enter a valid text"