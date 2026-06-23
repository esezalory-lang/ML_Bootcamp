import datetime
from recipe import Recipe


class Book:
    def __init__(self: "Book",
                 name: str,
                 last_update: datetime.datetime,
                 creation_date: datetime.datetime,
                 recipes_list: dict):
        if not isinstance(name, str) and name == "":
            raise ValueError("Invalid name")
        elif not isinstance(last_update,
                            datetime.datetime) and last_update == "":
            raise ValueError("Invalid update time")
        elif not isinstance(creation_date,
                            datetime.datetime) and last_update == "":
            raise ValueError("Invalid creation date")
        elif not isinstance(recipes_list, dict) or not all(
                                isinstance(i,
                                           list) for i in
                                recipes_list.values()):
            raise ValueError("Invalid recipe list")
        self.name = name
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipes_list = recipes_list

    def get_recipe_by_name(self, recipe_name: str) -> Recipe:
        """Prints a recipe with the name \texttt{name}
        and returns the instance"""
        for type, recipe_list in self.recipes_list.items():
            for recipe in recipe_list:
                if recipe_name == recipe.name:
                    name = Recipe.__str__(recipe)
                    print(name)
                    return recipe

    def get_recipes_by_types(self, recipe_type: str) -> list:
        """Gets all recipes names for a given recipe_type """
        for key, values in self.recipes_list.items():
            if key == recipe_type:
                return values

    def add_recipe(self, recipe: Recipe) -> None:
        """Adds a recipe to the book and updates last_update"""
        self.last_update = datetime.datetime.now()
        for key, values in self.recipes_list.items():
            if key == recipe.recipe_type:
                values.append(recipe)
