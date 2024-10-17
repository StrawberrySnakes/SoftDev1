#tests code of total_cost with value 7
import total_cost
def test_calculate_total_cost_7():
    #setup
    quantity = 7
    expected = 350

    #invoke
    actual = total_cost.calculate_total_cost(quantity)

    #analyze
    assert actual == expected

#tests code of total_cost with value 40
import total_cost
def test_calculate_total_cost_40():
    #setup
    quantity = 40
    expected = 1280

    #invoke
    actual = total_cost.calculate_total_cost(quantity)

    #analyze
    assert actual == expected
