'''
Consigna
Creá una lista de 10 elementos.
Luego utilizando un bucle, 
recorrer la lista e imprimir la posición 
y el elemento en dicha posición.
'''

pokemon_list = [
   "Venusaur",
   "Charizard",
   "Blastoise",
   "Butterfree",
   "Metapod",
    "Pidgeot",
    "Rattata",
    "Pikachu",
    "Nidoran",
    "Jigglypuff"
]

for i, pokemons in enumerate(pokemon_list):
    print(f"En la posicion {i} esta el pokemon: {pokemons}")

print("Fin del listado de pokemons")