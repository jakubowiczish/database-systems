def execute_task9(tx):
    actor1 = "Val Kilmer"
    actor2 = "Al Pacino"

    nodes = []

    print(f"\nActors on the shortest path between \"{actor1}\" and \"{actor2}\":")
    for record in tx.run("MATCH (a:Person {name: $actor1}), (b:Person {name: $actor2}), "
                         "path = shortestPath((a)-[*..25]-(b)) "
                         "RETURN path", actor1=actor1, actor2=actor2):
        for node in record["path"].nodes:
            if "Person" in node.labels:
                nodes.append(node.id)
                print(f"- {node['name']}")

    print(f"\nAdded is_special parameter for people on the shortest path between \"{actor1}\" and \"{actor2}\":")
    for record in tx.run("MATCH (person:Person) "
                         "WHERE id(person) in $nodes "
                         "SET person.is_special = true "
                         "RETURN person", nodes=nodes):
        print(f"- name: {record['person']['name']}, is_special: {record['person']['is_special']}")

# Result

# Actors on the shortest path between "Val Kilmer" and "Al Pacino":
# - Val Kilmer
# - Meg Ryan
# - Tom Hanks
# - Charlize Theron
# - Al Pacino
#
# Added is_special parameter for people on the shortest path between "Val Kilmer" and "Al Pacino":
# - name: Charlize Theron, is_special: True
# - name: Al Pacino, is_special: True
# - name: Val Kilmer, is_special: True
# - name: Meg Ryan, is_special: True
# - name: Tom Hanks, is_special: True
