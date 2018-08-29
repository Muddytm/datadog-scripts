#from checks import AgentCheck
import json
import requests
import time

prefix = "id=\"gradeA\">"
#grade = "F"
#grade_num = 0
name_list = ["testwebhtml01.carewebqi.com", "attach.carewebqi.com",
             "analytics.mcg.com", "access.mcg.com", "api-origin.carewebqi.com",
             "careweb.careguidelines.com", "api.mcg.com", "login.mcg.com"]
for name in name_list:
    r = requests.get("https://www.ssllabs.com/ssltest/analyze.html?d={}".format(name))
    count = 0
    #print ("Getting grade for server {}...".format(server))

    while "Please wait" in r.text:
        if count > 15:
            break
        else:
            count += 1

        #print ("Waiting...")
        time.sleep(10)
        r = requests.get("https://www.ssllabs.com/ssltest/analyze.html?d={}".format(name))

    if count > 15 or "Assessment failed" in r.text:
        #print ("Timed out.")
        grade = 0
    else:
        text = r.text[(r.text.find(prefix) + len(prefix)):]
        text_tokens = text.split()

        if "<span class=\"Aplus\">A+</span>" in text:
            grade = "A+"
        else:
            grade = text_tokens[0].strip()
            grade_num = 0

        print (grade)

        #print ("The grade was {}!".format(grade))

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

        #print ("The grade number was {}.".format(str(grade_num)))

    print ("mcg.security.sslgrade")
    print (grade_num)
    print ("site:" + name)
    #self.gauge("mcg.security.sslgrade",
    #           grade_num,
    #           tags=["server:" + name])
