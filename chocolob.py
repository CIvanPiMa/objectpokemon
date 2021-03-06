from basepokemon import BasePokemon, BaseMove, Type


class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        # Has to sum to 100
        self.spend_hp(20)
        self.spend_attack(55)
        self.spend_defence(25)
        self.add_move(Echatelo())
        self.set_type(Type.NORMAL)

    def get_name(self):
        return "Chocolob"

    def choose_move(self, enemy):
        return self.get_move_by_name("Echatelo")


class Echatelo(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(5)
        self.set_type(Type.EARTH)

    def get_name(self):
        return "Echatelo"
