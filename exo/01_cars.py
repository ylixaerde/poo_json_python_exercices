import json

def fn_display_cars_details(cars_dict):
    print(
    f"\n"
    f"Marque : {cars_dict["marque"]}\n" 
    f"Modèle : {cars_dict["modele"]}\n" 
    f"Année : {cars_dict["annee"]}\n"      
    f"couleurs_disponibles : {", ".join(cars_dict["couleurs_disponibles"])}\n" 
    f"Spécifications"     
    f"Moteur : {cars_dict["specifications"]["moteur"]}\n" 
    f"Puissance : {cars_dict["specifications"]["puissance"]}\n"     
    f"Prix : {cars_dict["prix"]}\n" 
    f"Consommation : {cars_dict["consommation"]}\n"
    )

with open("01_cars.json") as file:
  cars_dict = json.load(file)

fn_display_cars_details(cars_dict)