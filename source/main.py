import json
import http.client
from termcolor import colored as color

counter = 0
runner = True

while runner:

    try:
        file = open("IDs.txt")
        content = file.readlines()
        content = [x.replace('\n', '') for x in content]
        Id = content[counter]
        counter = counter + 1
    except IndexError:
        runner = False
        print(color('\nConcluded!\n', 'green'))
        break

    # URL connection

    conn = http.client.HTTPSConnection("xxxxx.xxxxxxxxxxxxxx.com")


    # Authorization 

    headers = {
        'Accept': "application/json",
        'Content-Type': "application/json",
        'API-AppKey': "xxxxxxxxxxxxxxxxxxxx",
        'API-AppToken': "xxxxxxxxxxxxxxxxxx"
        }


    # Request

    conn.request("GET", f"/api////{Id}", headers=headers)

    res = conn.getresponse()
    data = res.read()

    product = data.decode("utf-8")

    p_json = json.loads(product)
    p_json["xxx"] = "xxx"
    p_json = json.dumps(p_json)
    print(p_json)


    conn.request("PUT", f"/api////{Id}", p_json, headers)

    conn.close()

    print(color(f'\nRealized({counter})\n', 'cyan'))





