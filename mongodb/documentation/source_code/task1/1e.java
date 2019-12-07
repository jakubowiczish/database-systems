/*
private void executeTask1e() {
    AggregateIterable result = businessCollection.aggregate(
            asList(
                    lookup("Tip", "business_id", "business_id", "Tips"),
                    unwind("$Tips"),
                    match(and(
                            gte("Tips.date", "2013-01-01"),
                            lte("Tips.date", "2013-12-31")
                    )),
                    group("$name", sum("amountOfTips", 1)),
                    sort(ascending("_id"))
            ));

    for (Object o : result) {
        System.out.println(o);
    }
}
*/