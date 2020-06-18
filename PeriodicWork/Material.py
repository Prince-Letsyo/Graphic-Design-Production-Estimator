from PeriodicWork.Param import *





class MaterialCostPeriodic(ParamsPeriodic):
    _cmyk = 0

    def __init__(self, over_head, cp_ream, co_plate, number_color, co_separation):
        self.__overHead = over_head
        self.__CPR = cp_ream
        self.__COP = co_plate
        self.__numColor = number_color
        self.__COS = co_separation

    def set_values_period_m(self, over_head, cp_ream, co_plate, number_color, co_separation):
        self.__overHead = over_head
        self.__CPR = cp_ream
        self.__COP = co_plate
        self.__numColor = number_color
        self.__COS = co_separation

        MaterialCostPeriodic._cmyk = self.__numColor

    def paper_cost(self):
        pc = MaterialCostPeriodic.number_of_reams(self) * self.__CPR
        return pc

    def plate_cost(self):
        if MaterialCostPeriodic._front_back:
            pl_c = MaterialCostPeriodic.number_of_periods_to_view(self) * 2 * self.__numColor * self.__COP

        else:
            pl_c = MaterialCostPeriodic.number_of_periods_to_view(self) * self.__numColor * self.__COP

        return pl_c

    def separation_cost(self):
        if MaterialCostPeriodic._front_back:
            sc = MaterialCostPeriodic.number_of_periods_to_view(self) * 2 * self.__COS

        else:
            sc = MaterialCostPeriodic.number_of_periods_to_view(self) * self.__COS

        return sc

    def material_cost(self):
        mc = MaterialCostPeriodic.paper_cost(self) + MaterialCostPeriodic.plate_cost(self) + \
             MaterialCostPeriodic.separation_cost(self)
        return mc

    def over_head(self):
        oh_per = (self.__overHead / 100) * MaterialCostPeriodic.material_cost(self)
        return oh_per

    def total_material_cost(self):
        t_m_c = MaterialCostPeriodic.material_cost(self) + MaterialCostPeriodic.over_head(self)
        return t_m_c
