import json

with open("lab4/json/data.json", "r") as file:
    data = json.load(file)

print("""Interface Status
================================================================================""")
print("DN                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  ------  ------")
for i in range(3):
   print(data["imdata"][i]["l1PhysIf"]["attributes"]["dn"], "                            ", data["imdata"][i]["l1PhysIf"]["attributes"]["speed"], " ", data["imdata"][i]["l1PhysIf"]["attributes"]["mtu"])
#done