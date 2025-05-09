def indiviual_data(projects):
    return{
        "_id":str(projects["_id"]),
        "name":projects["name"],
        "description":projects["description"],
        "technologies":projects["technologies"]
    }
def all_data(projects):
    return [indiviual_data(project) for project in projects]