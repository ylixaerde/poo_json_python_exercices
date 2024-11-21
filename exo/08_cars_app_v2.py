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

    def fn_to_dict(self):
        # """Méthode pour convertir un objet Car en un dictionnaire sérialisable en JSON"""
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

    def object_hook(self, json_dict: Dict[str, Any]):
        if self.schema:
            if 'marque' in json_dict:
                jsonschema.validate(instance=json_dict, schema=self.schema)            
                return Car(**json_dict)
            return json_dict
        else:
            print(f"Erreur le schéma du fichier json est incorrect")
    
    # Schéma JSON correspondant à la classe Car
    schema = {
                "type": "object",
                "properties": {
                "marque": { "type": "string" },
                "modele": { "type": "string" },
                "annee": { "type": "integer" },
                "couleurs_disponibles": {
                    "type": "array",
                    "items": { "type": "string" }
                },
                "specifications": {
                    "type": "object",
                    "properties": {
                    "moteur": { "type": "string" },
                    "puissance": { "type": "number" }
                    },
                    "required": ["moteur", "puissance"]
                },
                "prix": { "type": "number" },
                "consommation": { "type": "number" }
                },
                "required": ["marque", "modele", "annee", "couleurs_disponibles", "specifications", "prix", "consommation"]
            }

class App:    
    def fn_afficher_menu(self):
        print(f"\nMenu - Computers Encoder")
        print("1. Ajouter un nouvel voiture")
        print("2. Afficher la liste des voitures")
        print("3. Quitter")
        choix = input("Choisissez une option : ")
        return choix
    
    def fn_load_cars_obj_list(self, json_file):
        with open(json_file, "r") as car_json:
            car_list = json.load(car_json, cls=CarDecoder, schema=CarDecoder.schema)
            return car_list
        
    def fn_display_cars_obj_list(self, car_list):
        for count, car in enumerate(car_list, 100):
            print(f"\nVoiture ID : {count}")
            self.fn_display_cars_details(car)
    
    def fn_display_cars_details(self, car):   
        print(
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

    def fn_enter_value(self, prompt, type_valeur, message_erreur):
        # Fonction utilitaire pour saisir une valeur et la valider.
        while True:
            valeur = input(prompt)
            try:
                valeur = type_valeur(valeur)
                if isinstance(valeur, (int, float)) and valeur <= 0:
                    print(f"Erreur: {message_erreur}")
                elif isinstance(valeur, str) and not valeur:
                    print(f"Erreur: {message_erreur}")
                else:
                    return valeur
            except ValueError:
                print(f"Erreur: {message_erreur} (type {type_valeur.__name__} attendu).")

    def fn_encode_car_to_obj(self):
        # Fonction pour encoder un nouvel objet Car à partir des données saisies au clavier.   
        marque = self.fn_enter_value("Saisir la marque : ", str, "La marque ne peut être vide.")
        modele = self.fn_enter_value("Saisir le modèle : ", str, "Le modèle ne peut être vide.")
        annee = self.fn_enter_value("Saisir l'année : ", int, "L'année doit être positive.")
        couleurs = self.fn_enter_value("Saisir les couleurs disponibles (séparées par des virgules) : ", str, "Au moins une couleur doit être saisie.").split(',')
        moteur = self.fn_enter_value("Saisir le type de moteur : ", str, "Le type de moteur ne peut être vide.")
        puissance = self.fn_enter_value("Saisir la puissance (en chevaux) : ", float, "La puissance doit être positive.")
        prix = self.fn_enter_value("Saisir le prix : ", float, "Le prix doit être positif.")
        consommation = self.fn_enter_value("Saisir la consommation : ", float, "La consommation doit être positive.")
        specifications = {"moteur": moteur, "puissance": puissance}
        nouvelle_voiture = Car(marque, modele, annee, couleurs, specifications, prix, consommation)
        return nouvelle_voiture
    
    # Ajout dans un fichier json des données contenues dans une liste d'objets Python 
    def fn_encode_obj_car_to_json(self, car, json_file):
        cars_obj_list = self.fn_load_cars_obj_list(json_file)
        cars_obj_list.append(car)
        cars_dict_list = []
        for car_obj in cars_obj_list:
            cars_dict_list.append(car_obj.fn_to_dict())           
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(cars_dict_list, f, indent=4, ensure_ascii=False)

    # fonction principale
    def fn_main(self):
        script_run = True
        while script_run:
            choix = self.fn_afficher_menu()
            match choix:
                case '1':
                    voiture = self.fn_encode_car_to_obj()
                    self.fn_encode_obj_car_to_json(voiture, self.json_file)
                case '2':
                    try:
                        cars_obj_list = self.fn_load_cars_obj_list(self.json_file)
                    except FileNotFoundError:
                        print(f"Le fichier JSON '{self.json_file}' n'a pas été trouvé.")
                    except json.decoder.JSONDecodeError as e:
                        print(f"Le fichier JSON '{self.json_file}' est corrompu.")
                        print(f"Erreur : {e}")
                    except Exception as e:
                        print(f"Une autre erreur s'est produite : {e}")
                    try:
                        self.fn_display_cars_obj_list(cars_obj_list)
                    except NameError:
                        print("La variable 'cars_obj_list' n'est pas définie.")
                    except TypeError:
                        print("Le type de données de la liste de voitures est incorrect.")
                    except ValueError:
                        print("Une valeur dans la liste de voitures est invalide.")
                    except Exception as e:
                        print(f"Une erreur inattendue s'est produite : {e}")
                case '3':
                    script_run=False
                case _:
                    print("Option invalide, veuillez réessayer.")

    # variable de classe
    json_file = "07_cars_app.json"


if __name__ == "__main__":
    print(f"Lancement du script {__file__}.py")
    app = App()
    app.fn_main()
