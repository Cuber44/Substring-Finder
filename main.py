
def StringCounter(string, substring):
    tempString=""
    count = 0
    lenSubString = len(substring)
    lenstring= len(string)
    for i in range(lenstring-lenSubString+1):
        tempString = "".join(string[j] for j in range(i,lenSubString+i))
        if tempString == substring:
            count+=1
        tempString =""
    return count

if __name__ == '__main__':
    string = ""
    substring = ""
    result = StringCounter(string, substring)
