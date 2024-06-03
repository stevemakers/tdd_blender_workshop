"""
1 A blender should have the ability to create smoothies from food
2 Smoothies should store information about macronutrients and calories
"""

class Blender():
    def __init__(self):
        self.ingredients = []
        self.capacity = 500

    """
    Adds a list of ingredients to the blender
    Ingredient is an array of tuples containing grams and macronutrients
    e.g.
    [
        (50, { "carbohyrdrate": 50", protein: "51", fat: "4", "calories": 45 })   
        (20, { "carbohydrates": 50", protein: "52", fat: "40", "calories": 55 })   
    ]
    """
    def add_ingredients(self, ingredients):        
        for ingredient in ingredients:
            grams = ingredient[0]
            macros = ingredient[1].keys()

            for macro in macros:
                # Adds a proportion of the macros
                ingredient[1][macro] *= (grams / 100)

            self.ingredients.append(ingredient[1])

    """
    Blends all the ingredients that have been passed into the blender
    Returns a Smoothie with the combined macronutrients
    """
    def blend_ingredients(self):
        total_grams = sum([ingredient[0] for ingredient in self.ingredients])
        if total_grams > self.capacity:
            raise ValueError("Exceeded blender capacity")
        
        smoothie_macros = {
            "calories": 0,
            "carbohydrates": 0,
            "protein": 0,
            "fat": 0,
        }

        for ingredient in self.ingredients:
            macros = ingredient.keys()

            for macro in macros:
                smoothie_macros[macro] += ingredient[macro]

        return Smoothie(smoothie_macros)
    
class Smoothie():
    def __init__(self, macros):
        self.macros = macros

    """
    Returns a health rating of the smoothie based on the macros
    """
    def categorize(self):
        calories = self.macros["calories"]
        carbohydrates = self.macros["carbohydrates"]
        protein = self.macros["protein"]
        fat = self.macros["fat"]

        if (
            calories <= 300
            and carbohydrates <= 50
            and protein >= 20
            and fat <= 15
        ):
            return "Healthy"
        elif (
            calories <= 400
            and carbohydrates <= 80
            and protein <= 20
            and fat <= 10
        ):
            return "Normal"
        else:
            return "Unhealthy"