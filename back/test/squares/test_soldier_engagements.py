from src.domain.soldiers import Soldier


def test_trooper_engage_trooper():

    charlie = Soldier("trooper")
    jerry = Soldier("trooper")

    expected_result = "draw"
    result = charlie.engage(jerry)

    assert result == expected_result
