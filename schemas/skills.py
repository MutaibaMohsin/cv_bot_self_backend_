def indiviual_data(skills):
    return{
        "_id":str(skills["_id"]),
        "category":skills["category"],
        "items":skills["items"]
    }
def all_data(skills):
    return [indiviual_data(skill) for skill in skills]