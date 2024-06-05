from unittest.mock import Mock, patch
from lib.blender import Blender, Ingredient, FoodAPI

def test_initialise_blender_class():
    blender = Blender()
    assert isinstance(blender, Blender) == True
    assert blender.ingredients == []

def test_add_ingredients_with_non_list_input():
    blender = Blender()

    try:
        blender.add_ingredients("not a list")
        assert False
    except ValueError:
        assert True

def test_blender_adds_one_ingredient():
    blender = Blender()
    blender.add_ingredients([Ingredient(50, "oats")])
    assert blender.ingredients[0].grams == 50
    assert blender.ingredients[0].name == "oats"

def test_blender_adds_multiple_ingredients():
    blender = Blender()
    blender.add_ingredients([
        Ingredient(150, "apple"),
        Ingredient(50, "oats")
    ])

    assert blender.ingredients[0].grams == 150
    assert blender.ingredients[0].name == "apple"
    assert blender.ingredients[1].grams == 50
    assert blender.ingredients[1].name == "oats"

@patch.object(FoodAPI, 'get_macros') 
# In this function if anything calls a class called FoodAPI and a method called get_macros
def test_blender_blends_ingredients(mock_get_macros):
    # THEN rename it to mock_get_macros
    mock_get_macros.return_value = {
        'carbs': 37,
        'protein': 4,
        'fats': 2,
        'calories': 185
    }
    # Arrange
    blender = Blender()

    # Act
    blender.add_ingredients([
        Ingredient(150, "apple"),
        Ingredient(50, "oats")
    ])
    smoothie = blender.blend_ingredients()

    assert smoothie.macros == {
        'carbs': 37,
        'protein': 4,
        'fats': 2,
        'calories': 185
    }

def test_print_ingredients():
    blender = Blender();

    fake_apple = Mock()
    # create instance of Mock called fake_apple

    fake_apple.get_key_info.return_value = "50 grams of Apples"
    # add a function called get_key_info which returns 50 grams of Apples

    fake_berries = Mock()
    fake_berries.get_key_info.return_value = "100 grams of Raspberries"
    
    fake_protein = Mock()
    fake_protein.get_key_info.return_value = "25 grams of Protein Powder"
    
    blender.add_ingredients([
        fake_apple,
        fake_berries,
        fake_protein
    ])
    print = blender.print_ingredients()

    assert print == "50 grams of Apples + 100 grams of Raspberries + 25 grams of Protein Powder"
