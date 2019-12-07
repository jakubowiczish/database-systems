db.Business.find(
    {open: true},
    {_id: 1, name: 1, full_address: 1}
);