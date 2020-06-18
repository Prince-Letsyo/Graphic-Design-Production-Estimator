from PaperWork.Param import ParamsPaper


class MaterialCost(ParamsPaper):
    _cmyk = 0
    _sc = 0

    def __init__(self, over_head, cp_ream, co_plate, number_color, film, co_separation, part_color, *args, **kwargs):
        self.__overHead = over_head
        self.__CPR = cp_ream
        self.__COP = co_plate
        self.__numColor = number_color
        self.__flat = film
        self.__COS = co_separation
        self.__partColour = part_color

    def set_values_paper(self, over_head, cp_ream, co_plate, number_color, film, co_separation, part_color):
        self.__overHead = over_head
        self.__CPR = cp_ream
        self.__COP = co_plate
        self.__numColor = number_color
        self.__flat = film
        self.__COS = co_separation
        self.__partColour = part_color

        MaterialCost._cmyk = self.__numColor

    def paper_cost(self):
        pc = MaterialCost.number_of_ream(self) * self.__CPR
        return pc

    def plate_cost(self):
        pl_c = self.__numColor * self.__COP
        return pl_c

    def separation_cost(self):
        if 0 < self.__numColor <= 3:
            MaterialCost._sc = MaterialCost._cmyk * self.__COS
        else:
            MaterialCost._sc = 2 * self.__COS
        return MaterialCost._sc

    def material_cost(self):
        mc = MaterialCost.paper_cost(self) + MaterialCost.plate_cost(self) + MaterialCost.separation_cost(self)
        return mc

    def over_head(self):
        oh_per = (self.__overHead / 100) * MaterialCost.material_cost(self)
        return oh_per

    def total_material_cost(self):
        t_m_c = MaterialCost.material_cost(self) + MaterialCost.over_head(self)
        return t_m_c
