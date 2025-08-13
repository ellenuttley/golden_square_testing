from lib.make_snippet import *
import pytest

lorem_ipsum = 'Lorem ipsum dolor sit amet consectetur, adipiscing elit. Sed sit amet fermentum diam, non hendrerit erat. '

def test_make_snippet_functional():
    assert(make_snippet)

def test_make_snippet_output_string():
    assert type(make_snippet(lorem_ipsum)) == str

def test_make_snippet_output_format_contains_ellipses():
    assert '...' in make_snippet(lorem_ipsum)

def test_make_snippet_output_format_contains_five_words():
    assert len(make_snippet(lorem_ipsum).split()) == 5

def test_make_snippet_short_input_no_ellipses():
    assert '...' not in make_snippet('Lorem ipsum dolor sit')

# if the input is not a string - eg. a number, return an error
def test_make_snippet_input_not_string():
    with pytest.raises(Exception) as err:
        make_snippet(4)
    error_message = str(err.value)
    assert error_message == "Please enter a valid string"

# if there is no string, return an error
def test_make_snippet_outputs_error_no_string():
    with pytest.raises(Exception) as err:
        make_snippet(None)
    error_message = str(err.value)
    assert error_message == "Please enter a valid string"


# test that the format is right, that the output contains five words, and then '...'
# test that there is no '...' if the string given is less than five words. 
# test that it still works, at any length of words (short words, etc)



# def test_make_snippet_():
#     pass

# def test_make_snippet_():
#     pass