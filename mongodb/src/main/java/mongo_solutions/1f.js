db.Business.aggregate([
    {$lookup: {from: "Review", localField: "business_id", foreignField: "business_id", as: "Reviews"}},
    {$unwind: "$Reviews"},
    {$group: {_id: "$name", averageStars: {$avg: "$stars"}}},
    {$sort: {avg: -1}}
]);