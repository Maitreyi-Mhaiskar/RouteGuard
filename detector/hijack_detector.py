import json

from prefix_database import PREFIX_DATABASE



def detect_hijack():


    with open("../data/bgp_updates.json") as file:

        update=json.load(file)



    prefix=update["prefix"]

    received_origin=update["origin"]


    expected_owner = PREFIX_DATABASE[prefix]["owner"]



    if received_origin != expected_owner:


        alert={

        "status":"HIJACKED",

        "prefix":prefix,

        "expected_AS":
        expected_owner,

        "received_AS":
        received_origin

        }


    else:


        alert={

        "status":"SAFE",

        "prefix":prefix

        }



    return alert





if __name__=="__main__":

    result=detect_hijack()

    print(result)
