db.User.aggregate([
    {$match: {$or: [{"votes.funny": {$gt: 0}}, {"votes.useful": {$gt: 0}}, {"votes.cool": {$gt: 0}}]}},
    {$group: {_id: "$name"}},
    {$sort: {"_id": 1}}
]);