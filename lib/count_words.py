def count_words(input_string):
    if type(input_string) is not str:
        raise Exception("Please enter a valid string")
    
    words = input_string.split()
    return len(words)