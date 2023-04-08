# Python program to identify
#color in images

def timeConverter(time):
    timeHold = 0
    if Time[1].isdigit():#convert american time to military 
        print(Time[0:2])
    if Time[0] == '1' or  Time[0] == '2' or  Time[0] == '3' or  Time[0] == '4' or  Time[0] == '5' or  Time[0] == '6' or  Time[0] == '6':
        timeHold = int(Time[0]) + 12
        print(timeHold)

def addVal(dict, key, className, time):
    if key not in dict:
        dict[key] = []
    dict[key].append(className)
    dict[key].append(time)

classLine = ""
semLine = ""

with open("Registration.html", "r") as f:
    for line in f.readlines():
        if "id=\"calendar\"" in line:
            # print(line,"\n")
            classLine = line
        if "class=\"schedule-list-view-title-text\">" in line:
        # print(line,"\n")
            semLine = line

# print(semLine)
# ---------------------------------------- var declarations below ----------------------------------------
semester = ""
min = 0
Day = ""
Time = ""
counter = 0
className = ""
classes = {}
# ---------------------------------------- var declarations above ----------------------------------------

semester = semLine[semLine.find(">") + 1 : semLine.find("</span>")]

week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
end = classLine.count("class=\"section-time-details\" href=\"#\">")

while counter < end:
    min = classLine.find("class=\"section-time-details\" href=\"#\">", min) #finds first instance of the this line 
    # print(min) #prints the win
    min += 38
    Day = classLine[min : classLine.find(" ", min)]
    # print(f"Day:*{Day}*")
    Time = classLine[classLine.find(" ", min) + 1: classLine.find("<", min)]
    # print(f"Time:*{Time}*")
    timeConverter(Time)

    className = classLine[classLine.find("</span>", min) + 7 : classLine.find("</a>", min)]
    # print(f"ClassName:*{className}*")
    addVal(classes, Day, className, Time)
    min = classLine.find("</a>", min)
    counter += 1

print("after run\n")

print(f"Semmy:*{semester}*\n")

for i in week:
    for j in classes[i]:
        print(j)
