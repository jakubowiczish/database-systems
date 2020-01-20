def execute_task3(tx):
    title = "Cloud Atlas"
    print(f"\nDirectors of \"{title}\":")

    for record in tx.run("MATCH (person)-[:DIRECTED]-(movie) WHERE movie.title = $title "
                         "RETURN person.name", title=title, ):
        print(f"- {record['person.name']}")

# Result

# Directors of "Cloud Atlas":
# - Tom Tykwer
# - Andy Wachowski
# - Lana Wachowski
