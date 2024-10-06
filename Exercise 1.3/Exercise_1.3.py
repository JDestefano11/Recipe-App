recipes_list = []
ingredients_list = []

def take_recipe():
    name = input("Enter the name of the recipe: ")
    cooking_time = int(input("Enter the cooking time in minutes: "))
    ingredients = input("Enter the ingredients (comma-separated): ").split(',')
    ingredients = [ingredient.strip() for ingredient in ingredients]
    recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients}
    return recipe

n = int(input("How many recipes would you like to enter? "))

for i in range(n):
    recipe = take_recipe()
    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    recipes_list.append(recipe)

for recipe in recipes_list:
    cooking_time = recipe['cooking_time']
    num_ingredients = len(recipe['ingredients'])
    
    if cooking_time < 10 and num_ingredients < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        difficulty = "Intermediate"
    else:
        difficulty = "Hard"
    
    print(f"Recipe: {recipe['name']}")
    print(f"Cooking Time: {cooking_time} minutes")
    print(f"Ingredients: {', '.join(recipe['ingredients'])}")
    print(f"Difficulty: {difficulty}")
    print()

print("\nAll Ingredients List:")
sorted_ingredients = sorted(ingredients_list)
for index, ingredient in enumerate(sorted_ingredients, 1):
    print(f"{index}. {ingredient}")
