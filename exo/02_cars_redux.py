import json
import jsonschema # pip install jsonschema
from typing import Dict, Any, List

class Car:
    def __init__(self, marque: str, modele: str, annee: int, couleurs_disponibles: list[str], specifications: dict, prix: float, consommation: float):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.couleurs_disponibles = couleurs_disponibles
        self.specifications = specifications
        self.prix = prix
        self.consommation = consommation

# Schéma JSON correspondant à la classe Car
car_schema = {
    "type": "object",
    "properties": {
        "marque": {"type": "string"},
        "modele": {"type": "string"},
        "annee": {"type": "integer"},
        "couleurs_disponibles": {"type": "array", "items": {"type": "string"}},
        "specifications": {"type": "object"},
        "prix": {"type": "number"},
        "consommation": {"type": "number"}
    },
    "required": ["marque", "modele", "annee", "couleurs_disponibles", "specifications", "prix", "consommation"]
}

class CarDecoder(json.JSONDecoder):
    def __init__(self, schema=None, *args, **kwargs):
        self.schema = schema
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, json_dict: Dict[str, Any]) -> Any:
        if self.schema:
            jsonschema.validate(instance=json_dict, schema=self.schema)

        if 'marque' in json_dict:
            return Car(**json_dict)
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
