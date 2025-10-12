import requests

import json
text_file="C:\\Users\\ragha\\OneDrive\\Desktop\\output.json"
base_url ="https://pokeapi.co/api/v2/"
def get_pokemon_info(name):
    url=f"{base_url}pokemon/{name}"
    response=requests.get(url)
    print(response)

    if response.status_code==200:
        pokemon_data=response.json()
        return pokemon_data
        
    else:
        return "not proper pokemon name"

pokemon_name=input("enter the pokemon name")
pokemon_info=get_pokemon_info(pokemon_name)


if pokemon_info:
    toy=[[f"name of the pokemon is {pokemon_info['name']}"]
    ,[f"height of the pokemon is {pokemon_info['height']}"],
    [f"weight of the pokemon is {pokemon_info['weight']}"],
     [f"abilities of the pokemon are:"
        ,[ability['ability']['name'] for ability in pokemon_info['abilities']]]]
    

    # Write nested list to JSON file
    with open(text_file, "w") as file:
        json.dump(toy, file, indent=4)
    print(f"the file name {text_file} exist")
else:
    print("pokemon not found")