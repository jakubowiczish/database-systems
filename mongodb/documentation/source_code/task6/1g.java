/*
private void executeTask1g() {
    AggregateIterable<Document> aggregateIterable = businessCollection.aggregate(
            asList(
                    lookup("Review", "business_id", "business_id", "Reviews"),
                    unwind("$Reviews"),
                    group("$name", avg("averageStars", "$stars")),
                    match(lt("averageStars", 3))
            )
    );

    for (Document document : aggregateIterable) {
        Document documentToBeDeleted = new Document(new Document("name", document.getString("_id")));
        DeleteResult deleteResult = businessCollection.deleteMany(documentToBeDeleted);
        System.out.println(deleteResult);
    }
}
*/