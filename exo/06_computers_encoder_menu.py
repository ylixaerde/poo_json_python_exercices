# -*- coding: utf-8 -*-

import json
import jsonschema
from typing import Dict, Any

class Computers:
    def __init__(self, marque: str, modele: str, processeur: str, memoire_ram: str, stockage: str, carte_graphique: str, systeme_exploitation: str, ports:list[str], dimensions: dict, poids: float, applications_installees : list[str]):
        self.marque = marque
        self.modele = modele
        self.processeur = processeur
        self.memoire_ram = memoire_ram
        self.stockage = stockage
        self.carte_graphique = carte_graphique
        self.systeme_exploitation = systeme_exploitation
        self.ports = ports
        self.dimensions = dimensions
        self.poids = poids
        self.applications_installees = applications_installees

    def fn_to_json(self):
        """Méthode pour convertir un objet Computers en un dictionnaire sérialisable en JSON"""
        return {
            "marque": self.marque,
            "modele": self.modele,
            "processeur": self.processeur,
            "memoire_ram": self.memoire_ram,
            "stockage": self.stockage,
            "carte_graphique": self.carte_graphique,
            "systeme_exploitation": self.systeme_exploitation,
            "ports": self.ports,
            "dimensions": self.dimensions,
            "poids": self.poids,
            "applications_installees": self.applications_installees
        }

class ComputersDecoder(json.JSONDecoder):
    def __init__(self, schema=None, *args, **kwargs):
        self.schema = schema
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, json_dict: Dict[str, Any]) -> Any:
        if self.schema:
            jsonschema.validate(instance=json_dict, schema=self.schema)

        if 'marque' in json_dict:
            return Computers(**json_dict)
        return json_dict

def fn_display_computers_details(computer):
    print(
    f"\n"
    f"Marque : {computer.marque}\n" 
    f"Modèle : {computer.modele}\n" 
    f"Année : {computer.processeur}\n"      
    f"Mémoire Ram : {computer.memoire_ram}\n" 
    f"Stockage : {computer.stockage}\n" 
    f"Carte Graphique : {computer.carte_graphique}\n" 
    f"Système d'exploitation : {computer.systeme_exploitation}\n" 
    f"Ports : {", ".join(computer.ports)}\n" 
    f"Dimensions\n" 
    f"Largeur : {computer.dimensions['largeur']}\n"
    f"Profondeur : {computer.dimensions['profondeur']}\n" 
    f"Hauteur : {computer.dimensions['hauteur']}\n"
    f"Poids : {computer.poids}\n" 
    f"Applications installées : {", ".join(computer.applications_installees)}\n" 
    )

def fn_afficher_menu():
    print(f"Menu - Computers Encoder")
    print("1. Ajouter un nouvel ordinateur")
    print("2. Afficher la liste des ordinateurs")
    print("3. Quitter")
    choix = input("Choisissez une option : ")
    return choix

def fn_main():
    script_run = True
    while script_run:
        choix = fn_afficher_menu()
        match choix:
            case '1':
                fn_ajouter_nouvel_ordinateur()
            case '2':
                fn_display_computers_details()
            case '3':
                script_run=False
            case _:
                print("Option invalide, veuillez réessayer.")

# Schéma JSON correspondant à la classe Car
computer_schema = {
    "type": "object",
    "properties": {
        "marque": {"type": "string"},
        "modele": {"type": "string"},
        "processeur": {"type": "string"},
        "memoire_ram": {"type": "string",},
        "stockage": {"type": "string"},
        "carte_graphique": {"type": "string"},
        "systeme_exploitation": {"type": "string"},
        "ports": {"type": "array", "items": {"type": "string"}},
        "dimensions": {"type": "object"},
        "poids": {"type": "number"},
        "applications_installees": {"type": "array", "items": {"type": "string"}}

    },
    "required": ["marque", "modele", "processeur", "memoire_ram", "stockage", "carte_graphique", "systeme_exploitation", "ports", "dimensions", "poids", "applications_installees"]
}

# Car = json.loads(car_json, cls=ComputersDecoder)
with open("05_computers.json", "r") as computer_json:
    computer = json.load(computer_json, cls=ComputersDecoder)
    fn_display_computers_details(computer)

# Création d'un objet Computers
mon_ordinateur = Computers(
    "Dell", "XPS 15", "Intel Core i7", "16GB", "512GB SSD", "RTX 3060", "Windows 11",
    ["USB-C", "HDMI", "Ethernet"], {"hauteur": 15, "largeur": 36, "profondeur": 23}, 1.8,
    ["Office 365", "Photoshop", "Visual Studio Code"]
)

# Sérialisation en JSON
json_data = json.dumps(mon_ordinateur.fn_to_json(), indent=4, ensure_ascii=False)
print(json_data)

# Écriture dans un fichier
with open('ordinateur01.json', 'w', encoding='utf-8') as f:
    json.dump(mon_ordinateur.fn_to_json(), f, indent=4, ensure_ascii=False)

# Ouvrir un fichier en mode écriture
with open("ordinateur02.json", "w") as fichier:
    # Écrire le contenu JSON dans le fichier
    fichier.write(json_data)

# Lecture depuis un fichier
with open('ordinateur01.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    # Création d'un nouvel objet Car à partir des données JSON
    nouvel_ordinateur = Computers(**data)
    print(nouvel_ordinateur.marque)  # Affichera "Dell"
    print(nouvel_ordinateur.modele)  # Affichera le dictionnaire des spécifications
