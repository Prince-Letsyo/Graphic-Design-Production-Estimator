from PeriodicWork.Material import *


class LabourCostPeriodic(MaterialCostPeriodic):
    def __init__(self, profit, c_o_f, c_p_i):
        self.__profit = profit
        self.__COF = c_o_f
        self.__CPI = c_p_i

    def set_values_period_l(self, profit, c_o_f, c_p_i):
        self.__profit = profit
        self.__COF = c_o_f
        self.__CPI = c_p_i

    def num_impression(self):
        if LabourCostPeriodic._front_back:
            num_imp = (LabourCostPeriodic.number_of_periods_to_view(self) * 2 * LabourCostPeriodic._cmyk) * \
                      (LabourCostPeriodic._qty_paper / LabourCostPeriodic.panels_to_view(self))
        else:
            num_imp = (LabourCostPeriodic.number_of_periods_to_view(self) * LabourCostPeriodic._cmyk) * \
                      (LabourCostPeriodic._qty_paper / LabourCostPeriodic.panels_to_view(self))

        return num_imp

    def cost_of_impression(self):
        cost_of_imp = (LabourCostPeriodic.num_impression(self) / 1000) * self.__CPI
        return cost_of_imp

    def cost_of_finishing(self):
        finishing_cost = LabourCostPeriodic._qty_paper * self.__COF
        return finishing_cost

    def cost_of_labour(self):
        labour_cost = LabourCostPeriodic.cost_of_impression(self) + LabourCostPeriodic.cost_of_finishing(self)
        return labour_cost

    def sub_total(self):
        sub_total_cost = LabourCostPeriodic.cost_of_labour(self) + LabourCostPeriodic.material_cost(self)
        return sub_total_cost

    def profit_cost(self):
        profit = (self.__profit / 100) * LabourCostPeriodic.sub_total(self)
        return profit

    def grand_total(self):
        grand_total = LabourCostPeriodic.sub_total(self) + LabourCostPeriodic.profit_cost(self)
        return grand_total

    def unit_cost(self):
        unit_c = LabourCostPeriodic.grand_total(self) / LabourCostPeriodic._qty_paper
        return unit_c


calender = LabourCostPeriodic(None, None, None)
