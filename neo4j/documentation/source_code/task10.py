def execute_task10(tx):
    print(f"\nNodes on the second place on path of size 4 between actor: \"Jack Nicholson\" and movie: \"Hoffa\":")

    for record in tx.run(
            """
            MATCH p = (:Person {name: "Jack Nicholson"})-[*3]-(:Movie {title: "Hoffa"})
            RETURN nodes(p)[1] as node
            """):
        print(f"- {record['node']}")

# Result
#
# Nodes on the second place on path of size 4 between actor: "Jack Nicholson" and movie: "Hoffa":
# - <Node id=14 labels={'Movie'} properties={'title': 'A Few Good Men', 'tagline': "In the heart of the nation's capital, in a courthouse of the U.S. government, one man will stop at nothing to keep his honor, and one will stop at nothing to find the truth.", 'released': 1992}>
# - <Node id=15 labels={'Movie'} properties={'title': "One Flew Over the Cuckoo's Nest", 'tagline': "If he's crazy, what does that make you?", 'released': 1975}>
# - <Node id=16 labels={'Movie'} properties={'title': 'Hoffa', 'tagline': "He didn't want law. He wanted justice.", 'released': 1992}>
# - <Node id=16 labels={'Movie'} properties={'title': 'Hoffa', 'tagline': "He didn't want law. He wanted justice.", 'released': 1992}>
# - <Node id=15 labels={'Movie'} properties={'title': "One Flew Over the Cuckoo's Nest", 'tagline': "If he's crazy, what does that make you?", 'released': 1975}>
