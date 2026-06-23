
class Recipe:
    VALID_TYPES = ("starter", "lunch", "dessert")

    def __init__(self: "Recipe",
                 name: str,
                 cooking_lvl: int,
                 cooking_time: int,
                 ingredients: list,
                 description: str,
                 recipe_type: str):
        if not isinstance(name, str) and name == "":
            raise ValueError("Invalid name")
        elif not isinstance(cooking_lvl,
                            int) and cooking_lvl is not range(0, 5):
            raise ValueError("Invalid cooking level")
        elif not isinstance(cooking_time,
                            int) and cooking_time < 0:
            raise ValueError("Invalid cooking time")
        elif not isinstance(ingredients,
                            list) or not all(
                                isinstance(i, str) for i in ingredients):
            raise ValueError("Invalid ingredients")
        elif not isinstance(description, str):
            raise ValueError("Invalid description")
        elif not isinstance(recipe_type,
                            str) or recipe_type not in self.VALID_TYPES:
            raise ValueError("Invalid recipe type")

        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        """Returns the string to print with the recipe’s info"""
        txt = ""
        txt += "Recipe Name: " + self.name + "\n"
        txt += "Recipe cooking level: " + str(self.cooking_lvl) + "\n"
        txt += "Recipe cooking time: " + str(self.cooking_time) + "\n"
        txt += "Recipe ingredients: " + ", ".join(self.ingredients) + "\n"
        txt += "Recipe description: " + self.description + "\n"
        txt += "Recipe type: " + self.recipe_type + "\n"
        return txt


# if __name__ == "__main__":
#     tourte = Recipe("tourte", 3, 30,
#                     ["eggs", "plums", "milk", "flour", "vanilla"],
#                     "Great recipe to eat for dessert",
#                     "lunch")
#     to_print = str(tourte)
#     print(to_print)
