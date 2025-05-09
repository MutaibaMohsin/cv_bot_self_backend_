def indiviual_data(achievements):
    return{
        "_id":str(achievements["_id"]),
        "name":achievements["name"],
        "organization":achievements["organization"],
        "description":achievements["description"]
    }
def all_data(achievements):
    return [indiviual_data(achievement) for achievement in achievements]