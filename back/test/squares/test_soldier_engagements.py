from src.domain.soldiers import Soldier


def test_trooper_engagements():

    charlie = Soldier("trooper")
    jerry = Soldier("trooper")
    hans = Soldier("grenadier")
    brian = Soldier("machinegun")

    result_1 = charlie.engage(jerry)
    result_2 = charlie.engage(hans)
    result_3 = charlie.engage(brian)

    assert result_1 == "draw"
    assert result_2 == "win"
    assert result_3 == "lose"


def test_grenadier_engagements():

    charlie = Soldier("grenadier")
    jerry = Soldier("trooper")
    hans = Soldier("grenadier")
    brian = Soldier("machinegun")

    result_1 = charlie.engage(jerry)
    result_2 = charlie.engage(hans)
    result_3 = charlie.engage(brian)

    assert result_1 == "lose"
    assert result_2 == "draw"
    assert result_3 == "win"


def test_machinegun_engagements():

    charlie = Soldier("machinegun")
    jerry = Soldier("trooper")
    hans = Soldier("grenadier")
    brian = Soldier("machinegun")

    result_1 = charlie.engage(jerry)
    result_2 = charlie.engage(hans)
    result_3 = charlie.engage(brian)

    assert result_1 == "win"
    assert result_2 == "lose"
    assert result_3 == "draw"
