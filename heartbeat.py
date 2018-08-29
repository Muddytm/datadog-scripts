from checks import AgentCheck
import json
import requests

class HeartbeatCheck(AgentCheck):
    def check(self, instance):
        r = requests.get(instance["url"])
        info = r.json()

        self.gauge("mcg.login.heartbeat",
                   instance["RequestDuration"],
                   tags=["server:" + instance["Machine"]])
