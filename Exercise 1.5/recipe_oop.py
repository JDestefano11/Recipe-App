class Recipe:
    all_ingredients = []

    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.cooking_time = 0
        self.difficulty = None

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_cooking_time(self):
        return self.cooking_time

    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time

    def add_ingredients(self, *ingredients):
        self.ingredients.extend(ingredients)
        self.update_all_ingredients()

    def get_ingredients(self):
        return self.ingredients

    def calculate_difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients) < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and len(self.ingredients) >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and len(self.ingredients) < 4:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"

    def get_difficulty(self):
        if self.difficulty is None:
            self.calculate_difficulty()
        return self.difficulty

    def search_ingredient(self, ingredient):
        return ingredient.lower() in (i.lower() for i in self.ingredients)

    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient.lower() not in (i.lower() for i in self.all_ingredients):
                self.all_ingredients.append(ingredient)

    def __str__(self):
        return f"Recipe: {self.name}\nCooking Time: {self.cooking_time} minutes\nIngredients: {', '.join(self.ingredients)}\nDifficulty: {self.get_difficulty()}"

def recipe_search(data, search_term):
    print(f"\nRecipes containing {search_term}:")
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe)

# Main code
pasta_carbonara = Recipe("Pasta Carbonara")
pasta_carbonara.add_ingredients("Spaghetti", "Eggs", "Pancetta", "Parmesan Cheese", "Black Pepper")
pasta_carbonara.set_cooking_time(20)
print(pasta_carbonara)

simple_salad = Recipe("Simple Salad")
simple_salad.add_ingredients("Lettuce", "Tomatoes", "Cucumber", "Olive Oil")
simple_salad.set_cooking_time(5)
print(simple_salad)

banana_smoothie = Recipe("Banana Smoothie")
banana_smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")
banana_smoothie.set_cooking_time(5)
print(banana_smoothie)

cake = Recipe("Cake")
cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk")
cake.set_cooking_time(50)
print(cake)

recipes_list = [pasta_carbonara, simple_salad, banana_smoothie, cake]

recipe_search(recipes_list, "Eggs")
recipe_search(recipes_list, "Bananas")
recipe_search(recipes_list, "Sugar")
