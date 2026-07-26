class BGPNode:

    def __init__(self, as_number):
        self.as_number = as_number
        self.neighbors = []
        self.routing_table = {}


    def add_neighbor(self, node):
        self.neighbors.append(node)


    def announce_route(self, prefix):

        route = {
            "prefix": prefix,
            "origin": self.as_number,
            "path": [self.as_number]
        }

        self.routing_table[prefix] = route

        return route



    def receive_route(self, route):

        new_path = route["path"] + [self.as_number]

        self.routing_table[route["prefix"]] = {

            "prefix": route["prefix"],

            "origin": route["origin"],

            "path": new_path

        }
