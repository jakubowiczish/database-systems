def execute_task4(tx):
    title = "The Lord of the Rings: The Return of the King"
    tagline = "One Ring To Rule Them All."
    released = 2003

    tx.run("MERGE (:Movie {title: $title, tagline: $tagline, released: $released})",
           title=title, tagline=tagline, released=released)

    Person = namedtuple("Person", "name born")
    people = [
        Person("Viggo Mortensen", 1958),
        Person("Elijah Wood", 1981),
        Person("Ian McKellen", 1939),
        Person("Liv Tyler", 1977),
        Person("Cate Blanchett", 1969),
    ]

    for person in people:
        tx.run("MERGE (:Person {name: $name, born: $born})",
               name=person.name, born=person.born)

        tx.run("MATCH (person:Person {name: $name}), (movie:Movie {title: $title}) "
               "MERGE (person)-[:ACTED_IN]->(movie)",
               name=person.name, title=title)

    print(f"\nActors playing in \"{title}\":")
    for record in tx.run("MATCH (person:Person)-[:ACTED_IN]->(:Movie {title: $title}) "
                         "RETURN person", title=title):
        print(f"- {record['person']['name']}")

# Result

# Actors playing in "The Lord of the Rings: The Return of the King":
# - Elijah Wood
# - Cate Blanchett
# - Sean Astin
# - Orlando Bloom
# - John Rhys-Davies
# - Ian McKellen
# - Hugo Weaving
# - Miranda Otto
# - Viggo Mortensen
# - Liv Tyler
