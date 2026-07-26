def generate_mitigation(prefix, attacker):


    rule=f"""

=================================

BGP MITIGATION RULE


BLOCK ROUTE:

{prefix}


FROM:

AS{attacker}


ACTION:

Reject Announcement


=================================

"""


    return rule




if __name__=="__main__":


    print(
        generate_mitigation(
        "10.20.0.0/16",
        4
        )
    )
