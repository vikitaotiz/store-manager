def iterate_list(list):
    for i in list:
        if i is None or not i:
            return False


def item_key(key, attr, dict_):
    result = list(filter(lambda obj: obj[key] == attr, dict_))
    if result:
        return result[0]
    return {"message":"{} does not exist in our records".format(key)}


def get_all(list_):
    if not list_:
        return {"message": "There are no records"}
    return list_