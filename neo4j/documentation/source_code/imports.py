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

# Result

# Movies are being imported...
# Movies have been successfully imported
# Actors are being imported...
# Actors have been successfully imported
# Directors are being imported...
# Directors have been successfully imported
