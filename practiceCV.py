# Python program to identify
#color in images

lineHold = ""

def addVal(dict, key, className, time):
    if key not in dict:
        dict[key] = []
    dict[key].append(className)
    dict[key].append(time)

with open("Registration.html", "r") as f:
    for line in f.readlines():
        if "id=\"calendar\"" in line:
            # print(line,"\n")
            lineHold = line
            break
min = 0
Day = ""
Time = ""
counter = 0
className = ""
classes = {}
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
end = lineHold.count("class=\"section-time-details\" href=\"#\">")

while counter < end:
    min = lineHold.find("class=\"section-time-details\" href=\"#\">", min) #finds first instance of the this line 
    # print(min) #prints the win
    min += 38
    Day = lineHold[min : lineHold.find(" ", min)]
    # print(f"Day:*{Day}*")
    Time = lineHold[lineHold.find(" ", min) + 1: lineHold.find("<", min)]
    # print(f"Time:*{Time}*")
    className = lineHold[lineHold.find("</span>", min) + 7 : lineHold.find("</a>", min)]
    # print(f"ClassName:*{className}*")
    addVal(classes, Day, className, Time)
    min = lineHold.find("</a>", min)
    counter += 1

print("after run\n")

for i in week:
    for j in classes[i]:
        print(j)
