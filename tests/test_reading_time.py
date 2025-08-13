from lib.reading_time import *
import pytest

def load_sample():
    with open('100_word_sample.txt', 'r') as file:
        return file.read()
    
sample = str(load_sample())

def test_reading_time_functional():
    assert(reading_time)

def test_reading_time_output_str():
    assert type(reading_time(sample)) == str

def test_reading_time_one_word():
    assert reading_time('text') == 'Reading this will take less than 1 second'

def test_reading_time_one_hundre_words():
    assert reading_time(sample) == 'Reading this will take 30 seconds'

def test_reading_time_two_hundred_words():
    assert reading_time(f"{sample} {sample}") == 'Reading this will take 1 minute'

def test_reading_time_three_hundred_words():
    assert reading_time(f"{sample} {sample} {sample}") == 'Reading this will take 1 minute and 30 seconds'

def test_reading_time_five_hundred_words():
    assert reading_time(f"{sample} {sample} {sample} {sample} {sample}") == 'Reading this will take 2 minutes and 30 seconds'

def test_reading_time_returned_nums_are_ints_not_floats():
    assert '.0' not in reading_time(f"{sample} {sample} {sample}")

def test_reading_time_input_not_string():
    with pytest.raises(Exception) as err:
        reading_time(0)
    error_message = str(err.value)
    assert error_message == "Please enter a valid text"

def test_reading_time_input_none():
    with pytest.raises(Exception) as err:
        reading_time(None)
    error_message = str(err.value)
    assert error_message == "Please enter a valid text"

def test_reading_time_input_empty():
    with pytest.raises(Exception) as err:
        reading_time('')
    error_message = str(err.value)
    assert error_message == "Please enter a valid text"
