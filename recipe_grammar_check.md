# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark

## 2. Design the Function Signature
```python
def grammar_check(text):
    """
    Save the first character
    Save the last character
    If the first character is not capitalised return 'Your grammar is bad!'
    If the last character is !, ? or . and first letter is capitalised 
    return 'Your grammar is ok!'
    If last character is anything else return 'Your grammar is bad!'

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
grammar_check('text') => str

"""
Given a text with no capital letter
Returns 'Your grammar is bad!'
"""
grammar_check('text') => 'Your grammar is bad!'

"""
Given a text with no capital letter and valid end character
Returns 'Your grammar is bad!'
"""
grammar_check('text.') => 'Your grammar is bad!'

"""
Given a text with capital letter, but no valid end character
Returns 'Your grammar is bad!'
"""
grammar_check('Text') => 'Your grammar is bad!'

"""
Given a text with capital letter AND valid end character
Returns 'Your grammar is ok!'
"""
grammar_check('Text.') => 'Your grammar is ok!'

Given a value that isn't a string
It throws an error
"""
grammar_check(0) => throws an error

"""
Given a None value
It throws an error
"""
grammar_check(None) => throws an error

"""
Given an empty string
It throws an error
"""
grammar_check('') => throws an error
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
