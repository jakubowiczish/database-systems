from collections import namedtuple

from neo4j import GraphDatabase


def import_database(tx):
    print("Movies are being imported...")

    tx.run(
        """ 
        LOAD CSV WITH HEADERS FROM
        'https://neo4j.com/docs/cypher-manual/3.5/csv/query-tuning/movies.csv' AS line
        MERGE (m:Movie { title: line.title })
        ON CREATE SET m.released = toInteger(line.released), m.tagline = line.tagline
        """)

    print("Movies have been successfully imported")

    print("Actors are being imported...")

    tx.run(
        """
        LOAD CSV WITH HEADERS FROM
        'https://neo4j.com/docs/cypher-manual/3.5/csv/query-tuning/actors.csv' AS line
        MATCH (m:Movie { title: line.title })
        MERGE (p:Person { name: line.name })
        ON CREATE SET p.born = toInteger(line.born)
        MERGE (p)-[:ACTED_IN { roles:split(line.roles, ';')}]->(m)
        """)

    print("Actors have been successfully imported")

    print("Directors are being imported...")

    tx.run(
        """
        LOAD CSV WITH HEADERS FROM
        'https://neo4j.com/docs/cypher-manual/3.5/csv/query-tuning/directors.csv' AS line
        MATCH (m:Movie { title: line.title })
        MERGE (p:Person { name: line.name })
        ON CREATE SET p.born = toInteger(line.born)
        MERGE (p)-[:DIRECTED]->(m)
        """)

    print("Directors have been successfully imported")


def execute_task3(tx):
    title = "Cloud Atlas"
    print(f"\nDirectors of \"{title}\":")

    for record in tx.run("MATCH (person)-[:DIRECTED]-(movie) WHERE movie.title = $title "
                         "RETURN person.name", title=title, ):
        print(f"- {record['person.name']}")


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


def execute_task5(tx):
    Person = namedtuple("Person", "name birthdate birthplace")
    people = [
        Person("Viggo Mortensen", "October 20, 1958", "Manhattan, New York"),
        Person("Elijah Wood", "January 28, 1981", "Cedar Rapids, Iowa"),
        Person("Ian McKellen", "May 25, 1939", "Burnley, United Kingdom"),
        Person("Liv Tyler", "July 1, 1977", "New York, New York"),
        Person("Cate Blanchett", "May 14, 1969", "Ivanhoe, Australia"),
    ]

    for person in people:
        tx.run("MATCH (person:Person {name: $name}) "
               "SET person.birthdate = $birthdate, person.birthplace = $birthplace",
               name=person.name,
               birthdate=person.birthdate, birthplace=person.birthplace)

    print("\nBirthplaces and birthdates of actors playing in \"The Lord of The Ring: The Return of the King\":")
    for person in people:
        record = tx.run("MATCH (person:Person {name: $name}) "
                        "RETURN person",
                        name=person.name).single()
        print(f"- {record['person']['name']}: {record['person']['birthplace']}, {record['person']['birthdate']}")


def execute_task6(tx):
    print("\nChanging year of birth from 1972 to 1971 for following actors:")
    for record in tx.run("MATCH (person:Person) "
                         "WHERE person.born = 1972 "
                         "SET person.born = 1971 "
                         "RETURN person.name"):
        print(f"- {record['person.name']}")

    print("\nChanging year of birth from 1971 to 1972 for following actors:")
    for record in tx.run("MATCH (person:Person) "
                         "WHERE person.born = 1971 "
                         "SET person.born = 1972 "
                         "RETURN person.name"):
        print(f"- {record['person.name']}")


def execute_task7(tx):
    print("\nThese actors have played in at least two movies:")
    for record in tx.run("MATCH (person:Person)-[:ACTED_IN]->(movie:Movie) "
                         "WITH person, size(collect(movie)) as movies_played_in "
                         "WHERE movies_played_in >= 2 "
                         "RETURN person.name"):
        print(f"- {record['person.name']}")

    print("\nAverage number of movies that actors have played in "
          "(for actors that have played in at least three movies)",
          end=" ")
    record = tx.run("MATCH (person:Person)-[:ACTED_IN]->(movie:Movie) "
                    "WITH person, size(collect(movie)) as movies "
                    "WHERE movies >= 3 "
                    "RETURN avg(movies) as average_number_of_movies").single()
    print(record["average_number_of_movies"])


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


def execute_task10(tx):
    print(f"\nNodes on the second place on path of size 4 between actor: \"Jack Nicholson\" and movie: \"Hoffa\":")

    for record in tx.run(
            """
            MATCH p = (:Person {name: "Jack Nicholson"})-[*3]-(:Movie {title: "Hoffa"})
            RETURN nodes(p)[1] as node
            """):
        print(f"- {record['node']}")


if __name__ == "__main__":
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "essa"))

    with driver.session() as session:
        session.write_transaction(import_database)
        session.read_transaction(execute_task3)
        session.write_transaction(execute_task4)
        session.write_transaction(execute_task5)
        session.write_transaction(execute_task6)
        session.read_transaction(execute_task7)
        session.read_transaction(execute_task9)
        session.read_transaction(execute_task10)

    driver.close()
