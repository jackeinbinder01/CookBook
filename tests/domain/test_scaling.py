from cookbook.domain.ingredient import Ingredient
from cookbook.domain.recipe import Recipe
from cookbook.domain.yield_ import Yield


def test_ingredient_scaling():

    ribeye_steak = Ingredient(
        name="ribeye steak",
        quantity=100,
        unit="g",
    )

    scaled = ribeye_steak.scaled(2)

    assert scaled.quantity == 200
    assert ribeye_steak.quantity == 100


def test_yield_scaling():
    yield_ = Yield(
        quantity=1,
        unit="servings",
    )

    scaled = yield_.scaled(2) 

    assert yield_.quantity == 1
    assert scaled.quantity == 2


def test_recipe_scaling():

    ribeye_steak = Ingredient(
        name="ribeye steak",
        quantity=100,
        unit="g",
    )

    salt = Ingredient(
        name="salt",
        quantity=2,
        unit="g",
    )

    pepper = Ingredient(
        name="pepper",
        quantity=4,
        unit="g",
    )

    ribeye_steak_recipe = Recipe(
        name="ribeye steak",
        description="A cross section of a beef ribeye",
        ingredients=[ribeye_steak, salt, pepper],
        yield_=Yield(quantity=1, unit="steak"),
        steps=[],
        gallery=None,
    )

    scaled = ribeye_steak_recipe.scaled(2)
    ribeye_steak_idx, salt_idx, pepper_idx = 0, 1, 2

    assert ribeye_steak_recipe.yield_.quantity == 1
    assert ribeye_steak_recipe.ingredients[ribeye_steak_idx].quantity == 100
    assert ribeye_steak_recipe.ingredients[salt_idx].quantity == 2
    assert ribeye_steak_recipe.ingredients[pepper_idx].quantity == 4

    assert scaled.yield_.quantity == 2
    assert scaled.ingredients[ribeye_steak_idx].quantity == 200
    assert scaled.ingredients[salt_idx].quantity == 4
    assert scaled.ingredients[pepper_idx].quantity == 8
