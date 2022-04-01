class Soldier:
    def __init__(self, troop_type):
        self.troop_type = troop_type
        self.engage_rules = self.asing_engage_rules(troop_type)

    def asing_engage_rules(self, troop_type):
        engagement_ruleset = {
            "trooper": {"trooper": "draw", "grenadier": "win"},
            "grenadier": {"trooper": "lose", "grenadier": "draw"},
        }
        return engagement_ruleset[troop_type]

    def engage(self, defender):
        return self.engage_rules[defender.troop_type]
