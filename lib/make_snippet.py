def make_snippet(input_string):
    if type(input_string) is not str:
            raise Exception("Please enter a valid string")
    
    words = input_string.split()
    if len(words) >=5:
        return f"{' '.join(words[:5])}..."
    else:
        return input_string
