import re
users="test1;test2;test3"
if users.__contains__(";"):
    splitString=users.split(";")
    for x in range (len(splitString)):
         print(splitString[x])
else:
    print("No")

stringtext="Users (82)"
textToReplace=re.findall("\(\)",stringtext)
print(textToReplace)
testString=stringtext.strip().replace("Users","").replace(")","").replace("(","").strip()
print(testString)