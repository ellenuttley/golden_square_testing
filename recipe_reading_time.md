# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature
```python
def reading_time(text):
    """
    Split the text into words
    Save 200 / 60 to a variable (3.3r) - this is how long it will take to read each word
    Multiply the amount of words by the above 3.3r second variable
    If the result of that multiplication is less than sixty, return 'Reading this will take {result} seconds'
    If it is more than 60, divide / modulo by 60 to get the minutes and seconds(round to nearest whole second)
    Return 'Reading this will take {minute} minutes and {seconds} seconds'
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

"""
Given valid input
It returns a string
"""
reading_time('text') => str

"""
Given a single word
It returns 1 second 
"""
reading_time('text') => 'Reading this will take less than 1 second'

"""
Given a sample of 200 words
It returns 1 minute and 0 seconds 
"""
reading_time(200_word_text) => 'Reading this will take 1 minute'

"""
Given a sample of 300 words
It returns 1 minute and 30 seconds 
"""
reading_time(300_word_text) => 'Reading this will take 1 minute and 30 seconds'

"""
Given a sample of 500 words
It returns 2 minutes and 30 seconds 
"""
reading_time(500_word_text) => 'Reading this will take 2 minutes and 30 seconds'


"""
Given a valid sample
Returns a string with no decimal numbers (both numbers, for seconds and minutes, are whole)
"""
reading_time(text_sample) => {minute} and {second} numbers are whole

"""
Given a value that isn't a string
It throws an error
"""
reading_time(0) => throws an error

"""
Given a None value
It throws an error
"""
reading_time(None) => throws an error

"""
Given an empty string
It throws an error
"""
reading_time(None) => throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
