# 1. Dla zapytania z zadania czwartego:
#
# "MATCH (person:Person)-[:ACTED_IN]->(:Movie {title: $title}) "
# "RETURN person"
#
# mozna wykonac optymalizacje w postaci zwracania tylko potrzebnej wartosci z wezla:
# "MATCH (person:Person)-[:ACTED_IN]->(:Movie {title: $title}) "
# "RETURN person.name"
#
# 2. Dla zapytania z zadania trzeciego:
# "MATCH (person)-[:DIRECTED]-(movie) WHERE movie.title = $title "
# "RETURN person.name"
#
# mozna wykonac optymalizacje w postaci okreslenia typu wezla (etykiety):
# "MATCH (person:Person)-[:DIRECTED]-(movie) WHERE movie.title = $title "
# "RETURN person.name"
