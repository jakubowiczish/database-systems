var map = function () {
    emit(this.user_id, 1);
};

var reduce = function (user_id, reviews) {
    return Array.sum(reviews);
};

db.Review.mapReduce(
    map,
    reduce,
    {out: "Reviews"}
);

db.Reviews.aggregate([
    {$group: {_id: null, avg: {$avg: "$value"}}}
]);