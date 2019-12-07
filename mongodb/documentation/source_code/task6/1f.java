/*
private void executeTask1f() {
    AggregateIterable result = businessCollection.aggregate(
            asList(
                    lookup("Review", "business_id", "business_id", "Reviews"),
                    unwind("$Reviews"),
                    group("$name", avg("averageStars", "$stars")),
                    sort(descending("averageStars"))
            ));

    for (Object o : result) {
        System.out.println(o);
    }
}
*/