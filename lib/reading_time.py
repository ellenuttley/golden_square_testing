def reading_time(text):
    if type(text) is not str or text == '':
        raise Exception("Please enter a valid text")

    word_count = len(text.split())
    word_time = 60 / 200
    if word_count < 4:
        return 'Reading this will take less than 1 second'
    elif word_count == 200:
        return f"Reading this will take 1 minute"
    elif word_count < 200:
        return f"Reading this will take {int(word_count * word_time)} seconds"
    
    else:
        total_seconds = word_count * word_time
        minutes = int(total_seconds // 60)
        seconds = int(total_seconds % 60)

        if seconds == 0:
            return f"Reading this will take {minutes} minutes"
        elif minutes == 1:
            return f"Reading this will take {minutes} minute and {seconds} seconds"
        else:
            return f"Reading this will take {minutes} minutes and {seconds} seconds"





sample = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam pharetra nibh vel eros maximus, vitae faucibus nibh vehicula. Proin a eros commodo eros rhoncus fringilla. Maecenas condimentum feugiat arcu quis posuere. Nullam fringilla nibh eu est fermentum tristique. Aliquam erat volutpat. Proin lorem mi, tempor dignissim ornare quis, facilisis nec ex. Nullam fermentum sit amet est at rhoncus. Proin convallis tristique libero, rhoncus dapibus metus accumsan a.

Vestibulum consequat elit in ex tincidunt, quis elementum ante vulputate. Vestibulum dignissim arcu fringilla sem scelerisque, sed ultrices felis sollicitudin. Donec sed ligula eu lacus feugiat lobortis vitae ut ex. Donec in ullamcorper.'''

print(reading_time(f"Lorem ipsum dolor sit sit sit"))

'''Split the text into words
Save 200 / 60 to a variable (3.3r) - this is how long it will take to read each word
Multiply the amount of words by the above 3.3r second variable
If the result of that multiplication is less than sixty, return 'Reading this will take {result} seconds'
If it is more than 60, divide / modulo by 60 to get the minutes and seconds(round to nearest whole second)
Return 'Reading this will take {minute} minutes and {seconds} seconds'''