import re

number = "six"
item = "7pqrstsixteen"

# Recherche de l'indice pour number[i]
match_number_i = re.search(rf'\b{number[1]}\b', item)
index_number_i = match_number_i.start() if match_number_i else -1

# Recherche de l'indice pour str(i)
i = 1
match_str_i = re.search(rf'\b{str(i)}\b', item)
index_str_i = match_str_i.start() if match_str_i else -1

# Récupération de l'indice minimum
min_index = min(index_number_i, index_str_i)

print(f"L'indice minimum est : {min_index}")