import logging

logging.basicConfig(level=logging.DEBUG)

def checkforneighbours(line, prevline, nextline, actpos, actnumber):
    lennumber = len(actnumber)
    startat = actpos -1 if actpos > 1 else actpos
    endat = actpos + lennumber + 1 if actpos + lennumber + 1 < len(line) else len(line)
    if prevline != "":
        for i in range(startat, endat):            
            if not prevline[i].isdigit() and prevline[i] != '.':
                return True
    if nextline != "":
        for i in range(startat, endat):
            if not nextline[i].isdigit() and nextline[i] != '.':
                return True
    if line[actpos-1] != '.':
        return True
    if line[endat-1] != '.' and endat < len(line):
        return True
    return False
        

def checkline(line, prevline, nextline):
    sum = 0
    actnumber = ""
    actpos = -1
    for pos, char in enumerate(line):
        if char.isdigit():
            if actpos == -1:
                actpos = pos
            actnumber += char
        elif actpos != -1:
            if checkforneighbours(line, prevline, nextline, actpos, actnumber):
                sum += int(actnumber)
          
            actpos = -1
            actnumber = ""
    if actpos != -1:
        if checkforneighbours(line, prevline, nextline, actpos, actnumber):
            sum += int(actnumber)        
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
    
