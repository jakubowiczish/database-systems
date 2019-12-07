/*
public class MongoDB {

    private MongoCollection<Document> businessCollection;
    private MongoCollection<Document> reviewCollection;
    private MongoCollection<Document> userCollection;

    private MongoDB() {
        MongoDatabase database = new MongoClient().getDatabase("plotniko");

        businessCollection = database.getCollection("Business");
        reviewCollection = database.getCollection("Review");
        userCollection = database.getCollection("User");
    }

    public static void main(String[] args) {
        MongoDB mongoDB = new MongoDB();
        mongoDB.executeTask1a();
        mongoDB.executeTask1b();
        mongoDB.executeTask1c();
        mongoDB.executeTask1d();
        mongoDB.executeTask1e();
        mongoDB.executeTask1f();
        mongoDB.executeTask1g();
    }

    private void executeTask1a() {
        DistinctIterable<String> uniqueCities = businessCollection.distinct("city", String.class);

        for (Object city : uniqueCities) {
            System.out.println(city);
        }
    }

    private void executeTask1b() {
        Bson dateRange = and(
                gte("date", "2011-01-01"),
                lte("date", "2012-12-31"));

        long count = reviewCollection.countDocuments(dateRange);

        System.out.println(count);
    }

    private void executeTask1c() {
        FindIterable<Document> result = businessCollection
                .find(eq("open", true))
                .projection(include("_id", "name", "full_address"));

        for (Object o : result) {
            System.out.println(o);
        }
    }

    private void executeTask1d() {
        Bson filter = or(
                gt("votes.funny", 0),
                gt("votes.useful", 0),
                gt("votes.cool", 0)
        );

        AggregateIterable<Document> result = userCollection.aggregate(
                asList(
                        match(filter),
                        group("$name"),
                        sort(ascending("_id"))
                ));

        for (Object o : result) {
            System.out.println(o);
        }
    }

    private void executeTask1e() {
        AggregateIterable<Document> result = businessCollection.aggregate(
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

    private void executeTask1f() {
        AggregateIterable<Document> result = businessCollection.aggregate(
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
}

 */