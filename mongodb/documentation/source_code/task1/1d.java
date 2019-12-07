/*
private void executeTask1d() {
    Bson filter = or(
            gt("votes.funny", 0),
            gt("votes.useful", 0),
            gt("votes.cool", 0)
    );

    AggregateIterable result = userCollection.aggregate(
            asList(
                    match(filter),
                    group("$name"),
                    sort(ascending("_id"))
            ));

    for (Object o : result) {
        System.out.println(o);
    }
}
*/