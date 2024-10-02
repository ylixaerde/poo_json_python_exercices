import json

with open("01_smartphone.json") as file:
  smartphone_dict = json.load(file)

print(type(smartphone_dict)) # <class "dict">
features = smartphone_dict["features"] # ["5G", "HD display", "Dual camera"]

print(
  f"\n"
  f"Nom : {smartphone_dict["name"]}\n"      
  f"Couleurs : {smartphone_dict["colors"][0]}, {smartphone_dict["colors"][1]}, {smartphone_dict["colors"][2]}\n"      
  f"Prix   {smartphone_dict["price"]}\n" 
  f"En stock : {smartphone_dict["in_stock"]}\n"      
  f"Largeur : {smartphone_dict["dimensions"]["width"]}\n"      
  f"Hauteur : {smartphone_dict["dimensions"]["height"]}\n"  
  f"Profondeur : {smartphone_dict["dimensions"]["depth"]}\n"       
  f"Détails : {smartphone_dict["features"][0]}, {smartphone_dict["features"][1]}, {smartphone_dict["features"][2]}\n"
)