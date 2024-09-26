import json

class Smartphone:
    def __init__(self, name, colors, price, in_stock):
        self.name = name
        self.colors = colors
        self.price = price
        self.in_stock = in_stock

class SmartphoneDecoder(json.JSONDecoder):
    def __init__(self, object_hook=None, *args, **kwargs):
        # set the custom object_hook method
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    # class method containing the
    # custom parsing logic
    def object_hook(self, json_dict):
        new_smartphone = Smartphone(
            json_dict.get('name'),
            json_dict.get('colors'),
            json_dict.get('price'),
            json_dict.get('inStock'),
        )

        return new_smartphone


# smartphone_json = '{"name": "iPear 23 Plus", "colors": ["black", "white", "gold"], "price": 1299.99, "inStock": false}'

with open("02_smartphone_poo_json.json") as file:
    smartphone = json.load(file, cls=SmartphoneDecoder)
    print(type(smartphone)) # <class '__main__.Smartphone'>
    print(f"Smartphone name : {smartphone.name }")
    print(f"Smartphone colors : {smartphone.colors}")
    print(f"Smartphone price : {smartphone.price}")
    print(f"Smartphone inStock : {smartphone.in_stock}")

#smartphone = json.loads(smartphone_json, cls=SmartphoneDecoder)
