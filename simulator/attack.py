import json


def prefix_hijack():

    malicious_route = {

        "prefix":
        "10.20.0.0/16",

        "origin":
        4,

        "path":
        [4]

    }


    with open("../data/bgp_updates.json","w") as file:

        json.dump(
            malicious_route,
            file,
            indent=4
        )


    print("ATTACK STARTED")
    print(malicious_route)



prefix_hijack()
