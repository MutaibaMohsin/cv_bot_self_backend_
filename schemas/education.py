def indiviual_data(education):
    return{
        "_id":str(education["_id"]),
        "degree":education["degree"],
        "university":education["university"]
    }
def all_data(edu):
    return [indiviual_data(education) for education in edu]