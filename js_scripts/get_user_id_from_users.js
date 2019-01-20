var temp_ids = db.company_users.find({company_id:"561f72fbe419be013b8b468e"}, {_id:false, user_id: true});
var user_ids = [];
while(temp_ids.hasNext()) {
    user_ids.push(ObjectId(temp_ids.next().user_id));
}

printjson(user_ids);

