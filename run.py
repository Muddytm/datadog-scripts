import json
import requests

prefix = "<div class=\"rating_a \" id=\"gradeA\">"
suffix = "</div>"

with open("server_list.json") as f:
    servers = json.load(f.read)

for server in servers["servers"]:
    print (server)

# r = requests.get("https://www.ssllabs.com/ssltest/analyze.html?d=po.cbre.com")
#
# text = r.text[(r.text.find(prefix) + len(prefix)):]
# text = text.split()
#
# grade = text[0].strip()
# print (grade)
