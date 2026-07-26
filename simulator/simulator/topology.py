from bgp_router import BGPNode
import json


AS1 = BGPNode(1)
AS2 = BGPNode(2)
AS3 = BGPNode(3)
AS4 = BGPNode(4)
AS5 = BGPNode(5)



AS1.add_neighbor(AS2)
AS1.add_neighbor(AS3)
AS1.add_neighbor(AS5)

AS1.add_neighbor(AS4)



route = AS1.announce_route(
    "10.20.0.0/16"
)



with open("../data/bgp_updates.json","w") as file:

    json.dump(route,file,indent=4)



print("Normal BGP announcement created")

print(route)
