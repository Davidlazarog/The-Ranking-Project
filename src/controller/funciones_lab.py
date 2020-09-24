def pull_closed():
    query = {'State':'closed'}
    result = db.student.find(query).count
    return result