"""Dessa Shapiro"""
import food_truck

class Combo:
    def __init__(self, drink, entree, side, price):
        self.drink=drink
        self.entree=entree
        self.side=side
        self.price = price

def test_print_menu():
    #setup
    menu = food_truck.MENU
    prices = food_truck.PRICES
    expected = "MENU\nAll meals are a combo!\nDrinks\ncoke(co): $2.3\nlemonaid(le): $3.0\nwater(wa): $2.1\nEntrees\ntaco(ta): $3.5\nburrito(bu): $6.0\nenchalata(en): $6.5\nSides\nchips(ch): $3.15\nsalsa(sa): $1.0\nguacamole(gu): $1.8"
    actual = food_truck.print_menu(menu, prices)
    assert expected == actual

def test_create_combo():
    prices = {
        "co": 2.30, "en": 6.50, "ch": 3.15
    }
    drink, entree, side = "co", "en", "ch"
    expected_combo = Combo(drink, entree, entree, 11.95)
    actual_combo = food_truck.create_combo(drink, entree, side, prices)
    assert actual_combo.drink == expected_combo.drink
    assert actual_combo.entree == expected_combo.entree
    assert actual_combo.side == expected_combo.side
    assert actual_combo.price == expected_combo.price

def test_order():
    expected_order = [Combo("co", "en", "ch", 11.95)]
    actual_order = food_truck.order(food_truck.MENU, food_truck.PRICES)
    assert actual_order == expected_order