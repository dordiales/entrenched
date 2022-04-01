from src.domain.soldiers import Soldier


def test_trooper_engage_trooper():

    charlie = Soldier("trooper")
    jerry = Soldier("trooper")

    result = charlie.engage(jerry)

    assert result.isalpha


def test_trooper_should_have_correct_engagements():

    charlie = Soldier("trooper")

    expected_rules = {"trooper": "draw", "grenadier": "win"}

    assert charlie.engage_rules == expected_rules


def test_grenadier_should_have_correct_engagements():

    jerry = Soldier("grenadier")

    expected_rules = {"trooper": "lose", "grenadier": "draw"}

    assert jerry.engage_rules == expected_rules
