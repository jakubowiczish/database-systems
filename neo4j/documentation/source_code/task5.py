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

# Result

# Birthplaces and birthdates of actors playing in "The Lord of The Ring: The Return of the King":
# - Viggo Mortensen: Manhattan, New York, October 20, 1958
# - Elijah Wood: Cedar Rapids, Iowa, January 28, 1981
# - Ian McKellen: Burnley, United Kingdom, May 25, 1939
# - Liv Tyler: New York, New York, July 1, 1977
# - Cate Blanchett: Ivanhoe, Australia, May 14, 1969
