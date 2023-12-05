import re 

def getnumber(line, asteriskpos):
    returnlist = []
    numbers = re.finditer(r'\b\d+\b', line)
    for number in numbers:
        pos = number.start()
        if asteriskpos >= pos -1 and asteriskpos < number.end() + 1:
            returnlist.append(int(number.group()))
    return returnlist    



def checkline(line, prevline, nextline):
    sum = 0
    for pos, char in enumerate(line):
        if char == '*':
            numbers = []
            if prevline != "":
                numbers = numbers + getnumber(prevline, pos)                
            if nextline != "":
                numbers = numbers + getnumber(nextline, pos)                
            numbers = numbers + getnumber(line, pos)
            print(numbers)
            if len(numbers) == 2:
                sum += numbers[0] * numbers[1]    
    return sum
                       


def checklines(lines):
    sum = 0
    for nr, line in enumerate(lines):
        if nr == 0:
            prevline = ""
            nextline = lines[nr+1]
        elif nr == len(lines)-1:
            prevline = lines[nr-1]
            nextline = ""
        else:
            prevline = lines[nr-1]
            nextline = lines[nr+1]
        sum += checkline(line, prevline, nextline)
    return sum


if __name__ == "__main__":
    with open("input") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    print(checklines(lines))
    