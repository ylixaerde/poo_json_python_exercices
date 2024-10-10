import json

# car_json = {
#    "marque": "Toyota",
#    "modele": "Corolla",
#    "annee": 2021,
#    "couleurs_disponibles": ["Rouge", "Bleu", "Noir"],
#    "specifications": {
#      "moteur": "1.8L",
#      "puissance": "140 ch"
#    },
#    "prix": 23999.99,
#    "consommation": 6.5
#  }

class Car:
    def __init__(self, marque, modele, annee, couleurs_disponibles, specifications, prix, consommation):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.couleurs_disponibles = couleurs_disponibles
        self.specifications = specifications
        self.prix = prix
        self.consommation = consommation

class CarDecoder(json.JSONDecoder):
    def __init__(self, object_hook=None, *args, **kwargs):
        # set the custom object_hook method
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    # class method containing the
    # custom parsing logic
    def object_hook(self, json_dict):
        # Check if the current object is a Car
        if 'marque' in json_dict:
            new_car = Car(
            json_dict.get('marque'),
            json_dict.get('modele'),
            json_dict.get('annee'),
            json_dict.get('couleurs_disponibles'),
            json_dict.get('specifications'),
            json_dict.get('prix'),
            json_dict.get('consommation')
        )
            return new_car
        # Si ce n'est pas un Car, on renvoie simplement le dictionnaire
        else:
            return json_dict

def fn_display_cars_details(car):
    print(
    f"\n"
    f"Marque : {car.marque}\n" 
    f"Modèle : {car.modele}\n" 
    f"Année : {car.annee}\n"      
    f"couleurs_disponibles : {", ".join(car.couleurs_disponibles)}\n" 
    f"Spécifications\n" 
    f"Moteur : {car.specifications['moteur']}\n"
    f"Puissance : {car.specifications['puissance']}\n" 
    f"Prix : {car.prix}\n" 
    f"Consommation : {car.consommation}\n"
    )


# Car = json.loads(car_json, cls=CarDecoder)
with open("01_cars.json", "r") as car_json:
    car = json.load(car_json, cls=CarDecoder)
    # print(type(car.specifications))
    # print(car.specifications)
    fn_display_cars_details(car)
