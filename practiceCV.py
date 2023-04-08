# Python program to identify
#color in images

lineHold = ""

def add_element(dict, key, className, time):
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
max = 0
print(len(lineHold))
Day = ""
Time = ""
counter = 0
className = ""
classes = {}
inc = 0
# classes["monday"] = {150 : "systems"}
week = ["Monday ", "Tuesday ", "Wednesday ", "Thursday ", "Friday "]

# add_element(classes, week[0], "hello")
# add_element(classes, week[0], "hello2")
end = lineHold.count("class=\"section-time-details\" href=\"#\">")
while counter < end:
    min = lineHold.find("class=\"section-time-details\" href=\"#\">", min) #finds first instance of the this line 
    print(min) #prints the win
    min += 38
    Day = lineHold[min : lineHold.find(" ", min)]
    print(f"Day:*{Day}*")
    Time = lineHold[lineHold.find(" ", min) + 1: lineHold.find("<", min)]
    print(f"Time:*{Time}*")
    className = lineHold[lineHold.find("</span>", min) + 7 : lineHold.find("</a>", min)]
    print(f"ClassName:*{className}*")
    add_element(classes, Day, className, Time)
    min = lineHold.find("</a>", min)
    counter += 1

print("after run\n")

for i in classes["Monday"]:
    print(i)
# </span>Systems Programming</a>