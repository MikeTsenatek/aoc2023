replacements = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def replace_first_last_occurrence(input_string):

    first_occurrence = len(input_string)
    last_occurrence = 0
    first_number = 0
    last_number = 0
    first_string = ""
    last_string = ""

    for word, replacement in replacements.items():
        first = input_string.find(word)
        if first >= 0 and first < first_occurrence:
            first_occurrence = input_string.find(word)
            first_number = word
            first_string = replacement

    input_string = input_string[:first_occurrence] + first_string + input_string[first_occurrence+len(str(first_number)):]
    nowordfound = True
    for word, replacement in replacements.items():
        last = input_string.rfind(word)
        if last >= 0 and last > last_occurrence:
            nowordfound = False
            last_occurrence = input_string.rfind(word)
            last_number = word
            last_string = replacement

    if not nowordfound:
        input_string = input_string[:last_occurrence] + last_string + input_string[last_occurrence+len(str(last_number)):]


    return input_string

# Example usage:
input_str = "7pqrstsixteen"
result = replace_first_last_occurrence(input_str)
print(result)
