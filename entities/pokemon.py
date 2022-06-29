class Pokemon:
    def __init__(self, data):
        self.name = data["name"]
        self.types = data["types"]
        self.number = data["number"]
        self.item = data["item"]

    def set_name(self, name):
        self.name = name

    def set_types(self, types):
        self.types = types


    def to_dict(self):
        return {
            "name": self.name,
            "types": self.types,
            "number": self.number,
            "item": self.item
        }
# froakie = Pokemon({
#     "name": "Froakie",
#     "types": ["Water"],
#     "number": 656,
#     "item": "King's Rock"
# })
