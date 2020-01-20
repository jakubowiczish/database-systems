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

# Result

# These actors have played in at least two movies:
# - Jack Nicholson
# - Keanu Reeves
# - Gene Hackman
# - Charlize Theron
# - Hugo Weaving
# - Laurence Fishburne
# - Carrie-Anne Moss
# - Ben Miles
# - Tom Hanks
# - Rain
# - Rick Yune
# - Liv Tyler
# - Bonnie Hunt
# - Jerry O'Connell
# - Cuba Gooding Jr.
# - Tom Cruise
# - Meg Ryan
# - Kiefer Sutherland
# - Kevin Bacon
# - J.T. Walsh
# - Danny DeVito
# - Helen Hunt
# - Greg Kinnear
# - Bill Paxton
# - Gary Sinise
# - Oliver Platt
# - Sam Rockwell
# - Marshall Bell
# - Max von Sydow
# - Robin Williams
# - Nathan Lane
# - Rosie O'Donnell
# - Steve Zahn
# - James Cromwell
# - Zach Grenier
# - Philip Seymour Hoffman
# - Ian McKellen

# Average number of movies that actors have played in (for actors that have played in at least three movies) 4.4
