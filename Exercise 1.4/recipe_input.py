import pickle

def take_recipe():
    name = input("Enter the recipe name: ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients = input("Enter ingredients (comma-separated): ").split(',')
    ingredients = [ingredient.strip() for ingredient in ingredients]
    difficulty = calc_difficulty(cooking_time, len(ingredients))
    return {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients,
        'difficulty': difficulty
    }

def calc_difficulty(cooking_time, num_ingredients):
    if cooking_time < 10 and num_ingredients < 4:
        return "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        return "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        return "Intermediate"
    else:
        return "Hard"

filename = input("Enter the filename to store the recipes: ")

try:
    with open(filename, 'rb') as file:
        data = pickle.load(file)
except FileNotFoundError:
    data = {'recipes_list': [], 'all_ingredients': []}
except:
    print("Unexpected error. Creating new data structure.")
    data = {'recipes_list': [], 'all_ingredients': []}
else:
    file.close()
finally:
    recipes_list = data['recipes_list']
    all_ingredients = data['all_ingredients']

n = int(input("How many recipes would you like to enter? "))

for i in range(n):
    recipe = take_recipe()
    recipes_list.append(recipe)
    for ingredient in recipe['ingredients']:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)

data = {'recipes_list': recipes_list, 'all_ingredients': all_ingredients}

with open(filename, 'wb') as file:
    pickle.dump(data, file)

print(f"Recipe data has been saved to {filename}")
