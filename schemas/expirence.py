def indiviual_data(experiences):
    return{
        "_id":str(experiences["_id"]),
        "position":experiences["position"],
        "company":experiences["company"],
        "location":experiences["location"],
        "description":experiences["description"],
    }
def all_data(experiences):
    return [indiviual_data(experience) for experience in experiences]