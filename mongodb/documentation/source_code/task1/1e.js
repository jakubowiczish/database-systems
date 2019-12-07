db.Business.aggregate([
    {$lookup: {from: "Tip", localField: "business_id", foreignField: "business_id", as: "Tips"}},
    {$unwind: "$Tips"},
    {$match: {"Tips.date": {$gte: "2013-01-01", $lte: "2013-12-31"}}},
    {$group: {_id: "$name", amountOfTips: {$sum: 1}}},
    {$sort: {_id: 1}}
]);