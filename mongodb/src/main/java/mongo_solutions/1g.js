var businesses = db.Business.aggregate([
    {$lookup: {from: "Review", localField: "business_id", foreignField: "business_id", as: "Reviews"}},
    {$unwind: "$Reviews"},
    {$group: {_id: "$name", averageStars: {$avg: "$stars"}}},
    {$sort: {averageStars: -1}}
]);

businesses.forEach(function (business) {
    if (business.avg < 3) {
        db.Business.remove({"name": business._id});
    }
});