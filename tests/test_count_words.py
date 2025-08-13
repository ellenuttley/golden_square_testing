from lib.count_words import *
import pytest

lorem_ipsum = 'Lorem ipsum dolor sit amet consectetur, adipiscing elit. Sed sit amet fermentum diam, non hendrerit erat. '

def test_count_words_functional():
    return count_words('')
    
def test_count_words_output_int():
    assert type(count_words(lorem_ipsum)) == int

def test_count_words_correct_count():
    assert count_words('Lorem ipsum dolor sit amet') == 5

def test_count_words_correct_count_empty_string():
    assert count_words('') == 0

# if the input is not a string - eg. a number, return an error
def test_count_words_input_not_string():
    with pytest.raises(Exception) as err:
        count_words(0)
    error_message = str(err.value)
    assert error_message == "Please enter a valid string"

# if there is no string, return an error
def test_count_words_outputs_error_no_string():
    with pytest.raises(Exception) as err:
        count_words(None)
    error_message = str(err.value)
    assert error_message == "Please enter a valid string"
