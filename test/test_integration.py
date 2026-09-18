from app import add, multiply


def test_calculation_flow():
    result = add(2, 3)
    result = multiply(result, 4)


    assert result == 20
