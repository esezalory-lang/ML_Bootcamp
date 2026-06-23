
def recipe_names(cookbook: dict) -> None:
    for key, value in cookbook.items():
        print(f"{key}")


def recipe_details(recipe: str, cookbook: dict) -> str:
    recipe_data = {key.lower(): value for key,
                   value in cookbook.items()}.get(recipe.lower(), {})
    details = {key.lower(): value for key,
               value in recipe_data.items()}.get("ingredients")
    if details:
        return details


def recipe_type(recipe: str, cookbook: dict) -> str:
    recipe_data = {key.lower(): value for key,
                   value in cookbook.items()}.get(recipe.lower(), {})
    details = {key.lower(): value for key,
               value in recipe_data.items()}.get("meal")
    if details:
        return details


def recipe_prep(recipe: str, cookbook: dict) -> None:
    recipe_data = {key.lower(): value for key,
                   value in cookbook.items()}.get(recipe.lower(), {})
    details = {key.lower(): value for key,
               value in recipe_data.items()}.get("prep_time")
    if details:
        return details


def recipe_remove(recipe: str, cookbook: dict) -> None:
    for key, value in cookbook.items():
        if recipe.lower() == key.lower():
            cookbook.pop(key)
            return


def recipe_add(cookbook: dict) -> dict:
    recipe_name = ""
    ingredients = []
    meal_type = ""
    meal_prep = 0
    new_recipe = {}
    recipe_name = input(">>> Enter a name:\n")
    print(">>> Enter ingredients:")
    for i in range(5):
        food = input()
        if food == "":
            break
        ingredients.append(food)
    meal_type = input(">>> Enter a meal type:\n")
    meal_prep = int(input(">>> Enter a preperation time:\n"))

    new_recipe.update({"ingredients": ingredients, "meal": meal_type,
                       "prep_time": meal_prep})
    cookbook.update({recipe_name: new_recipe})


if __name__ == "__main__":
    cookbook = {
        "Sandwich":
        {
            "ingredients": ["ham", "bread", "cheese", "tomatoes"],
            "meal": "lunch",
            "prep_time": 10
         },
        "Cake":
        {
            "ingredients": ["flour", "sugar", "eggs"],
            "meal": "dessert",
            "prep_time": 60
         },
        "Salad":
        {
            "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
            "meal": "lunch",
            "prep_time": 15
         }
         }
    while True:
        print("Welcome to the python Cookbook!\nList of available options:")
        print("\t1: Add a recipe:")
        print("\t2: Delete a recipe")
        print("\t3: Print a recipe")
        print("\t4: Print the cookbook")
        print("\t5: Quick")
        print("Please select an option:")
        try:
            option = int(input(">>> "))
        except Exception:
            print("Sorry, this option does not exist.")
        if option == 1:
            recipe_add(cookbook)
        elif option == 2:
            print("Enter recipe to remove:")
            to_remove = input(">>> ")
            recipe_remove(to_remove, cookbook)
        elif option == 3:
            print("Please enter a recipe name to get its details:")
            to_print = input(">>> ")
            print(f"Recipe for {to_print}:")
            print(f"Ingredients list: {recipe_details(to_print, cookbook)}")
            print(f"To be eaten for {recipe_type(to_print, cookbook)}")
            print(f"Takes {recipe_prep(to_print, cookbook)}",
                  "minutes of cooking\n")
        elif option == 4:
            print(f"{cookbook}")
        elif option == 5:
            print("Cookbook close. Goodbye")
            break
        else:
            print("Sorry, this option does not exist.")
