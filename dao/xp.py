from config import mongo

# class to acess Xp database on mongo
class XpDao():
    def add_member(data):
        mongo.evolution.xp.insert_one(data)
    def create_member_register(id):
        return mongo.evolution.xp.insert_one({'member_id': id, 'xp': 0, 'level': 0})

    def find_by_member_id(id):
        return mongo.evolution.xp.find_one({'member_id': id})

    def update_xp(data):
        return mongo.evolution.xp.update_one({'member_id': data['member_id']}, {"$set": data})

    def get_all_ordened():
        return mongo.evolution.xp.find().sort([("level", -1), ("xp", -1)])
