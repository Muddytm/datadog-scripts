import json
import requests
import time

prefix = "id=\"gradeA\">"

with open("server_list.json") as f:
    servers = json.load(f)

grade_list = []

for server in servers["servers"]:
    r = requests.get("https://www.ssllabs.com/ssltest/analyze.html?d={}".format(server))
    count = 0
    print ("Getting grade for server {}...".format(server))
    while "Please wait" in r.text:
        if count > 10:
            break
        else:
            count += 1

        print ("Waiting...")
        time.sleep(10)
        r = requests.get("https://www.ssllabs.com/ssltest/analyze.html?d={}".format(server))

    if count > 10:
        print ("Timed out.")
        grade_list.append({"name": server, "grade": 0})
        continue

    if "Assessment failed" in r.text:
        print ("Failed.")
        grade_list.append({"name": server, "grade": 0})
        continue
    else:
        text = r.text[(r.text.find(prefix) + len(prefix)):]
        text = text.split()

        grade = text[0].strip()
        grade_num = 0

        if grade == "<span class=\"Aplus\">A+</span>":
            grade = "A+"

        print ("The grade was {}!".format(grade))

        if grade == "A+":
            grade_num = 10
        elif grade == "A":
            grade_num = 9
        elif grade == "B":
            grade_num = 8
        elif grade == "C":
            grade_num = 7
        elif grade == "D":
            grade_num = 6
        elif grade == "E":
            grade_num = 5
        elif grade == "F":
            grade_num = 4

        print ("The grade number was {}.".format(str(grade_num)))

        grade_list.append({"name": server, "grade": grade_num})
        continue

for grade in grade_list:
    print ("The grade_num for {} is {}.".format(grade["name"], grade["grade"]))
    # self.set("whatever.the.name.is",
    #          grade["grade"],
    #          tags=['server=' + grade["name"]])
