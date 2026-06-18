#learing how to connect to an API using python
import requests

base_url="https://pokeapi.co/api/v2"

def get_pokemon_info(name):
  url= f"{base_url}/pokemon/{name}"
  # Send a request to the Pokémon API
  response= requests.get(url)

  # Check if the request was successful
  if response.status_code == 200:
    # Convert the JSON response into a Python dictionary
    pokemon_data=response.json()
    return pokemon_data#here this "pokemon_data" variable is contianing data in dict format which easy to read
  else:
    print(f"failed to retrieve data{response.status_code}")
pokemon_name=input("Enter the name of pokemon: ")
#
# pokemon_name="pikachu"
pokemon_info=get_pokemon_info(pokemon_name)

if pokemon_info:
  print(f"Name {pokemon_info['name'].capitalize()}")
  print(f"ID: {pokemon_info['id']}")
  print(f"Height: {pokemon_info['height']}")
  print(f"Weight: {pokemon_info['weight']}")


