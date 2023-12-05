import re

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

def combine_and_sum_from_file(file_path):
    total_sum = 0

    try:
        with open(file_path, 'r') as file:
            # Iterate over each line in the file
            for line in file:

                # Find all digits in the line using regular expression
                newline = replace_first_last_occurrence(line)
                digits = [int(d) for d in re.findall(r'\d', newline)]

                # Take the first digit (or 0 if none) and the last digit (or use the first if none)
                first_digit = digits[0] if digits else 0
                last_digit = digits[-1] if digits else first_digit

                # Combine them to a two-digit integer
                combined_int = int(str(first_digit) + str(last_digit))
                print(f"{line.strip()}: {combined_int}")
                # Add the combined integer to the total sum
                total_sum += combined_int

        return total_sum
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
file_path = 'input'  # Assuming 'input' is the name of your file
result = combine_and_sum_from_file(file_path)

if result is not None:
    print(f"Sum of combined two-digit integers from the first and last digits in each line: {result}")
