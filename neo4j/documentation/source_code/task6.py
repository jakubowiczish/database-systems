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

# Result

# Changing year of birth from 1972 to 1971 for following actors:
# - Noah Wyle
# - Regina King
# - Corey Feldman
# - Wil Wheaton
# - Rick Yune
# - Paul Bettany
# - Sean Astin
#
# Changing year of birth from 1971 to 1972 for following actors:
# - Noah Wyle
# - Regina King
# - Corey Feldman
# - Wil Wheaton
# - Rick Yune
# - Paul Bettany
# - Sean Astin
