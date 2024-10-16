# -*- coding: utf-8 -*-

import json
import jsonschema # pip install jsonschema
from typing import Dict, Any

class Car:
    def __init__(self, marque: str, modele: str, annee: int, couleurs_disponibles: list[str], specifications: dict, prix: float, consommation: float):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.couleurs_disponibles = couleurs_disponibles
        self.specifications = specifications
        self.prix = prix
        self.consommation = consommation

    def fn_to_json(self):
        """Méthode pour convertir un objet Car en un dictionnaire sérialisable en JSON"""
        return {
            "marque": self.marque,
            "modele": self.modele,
            "annee": self.annee,
            "couleurs_disponibles": self.couleurs_disponibles,
            "specifications": self.specifications,
            "prix": self.prix,
            "consommation": self.consommation
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

# Car = json.loads(car_json, cls=CarDecoder)
with open("01_cars.json", "r") as car_json:
    car = json.load(car_json, cls=CarDecoder)
    # print(type(car.specifications))
    # print(car.specifications)
    fn_display_cars_details(car)

# Création d'un objet Car
ma_voiture = Car("Tesla", "Model 3", 2023, ["Noir", "Blanc", "Rouge"],
                {"Puissance": 310, "Autonomie": 500, "Type_moteur": "Électrique"}, 45000, 15)

# Sérialisation en JSON
json_data = json.dumps(ma_voiture.fn_to_json(), indent=4, ensure_ascii=False)
print(json_data)

# Écriture dans un fichier
with open('voiture01.json', 'w', encoding='utf-8') as f:
    json.dump(ma_voiture.fn_to_json(), f, indent=4, ensure_ascii=False)

# Ouvrir un fichier en mode écriture
with open("voiture02.json", "w") as fichier:
    # Écrire le contenu JSON dans le fichier
    fichier.write(json_data)

# Lecture depuis un fichier
with open('voiture01.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    # Création d'un nouvel objet Car à partir des données JSON
    nouvelle_voiture = Car(**data)
    print(nouvelle_voiture.marque)  # Affichera "Tesla"
    print(nouvelle_voiture.specifications)  # Affichera le dictionnaire des spécifications
