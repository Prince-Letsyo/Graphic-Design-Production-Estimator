from PaperWork.Material import MaterialCost


class LabourCost(MaterialCost):
    def __init__(self, profit, c_o_f, c_p_i):
        self.__profit = profit
        self.__COF = c_o_f
        self.__CPI = c_p_i

    def set_values_paper_l(self, profit, c_o_f, c_p_i):
        self.__profit = profit
        self.__COF = c_o_f
        self.__CPI = c_p_i

    def num_impression(self):
        num_imp = LabourCost.number_of_wss(self) * LabourCost._cmyk
        return num_imp

    def cost_of_impression(self):
        cost_of_imp = (LabourCost.num_impression(self) / 1000) * self.__CPI
        return cost_of_imp

    def cost_of_finishing(self):
        finishing_cost = (LabourCost.number_of_wss(self) / 1000) * self.__COF
        return finishing_cost

    def cost_of_labour(self):
        labour_cost = LabourCost.cost_of_impression(self) + LabourCost.cost_of_finishing(self)
        return labour_cost

    def sub_total(self):
        sub_total_cost = LabourCost.cost_of_labour(self) + LabourCost.material_cost(self)
        return sub_total_cost

    def profit_cost(self):
        profit = (self.__profit / 100) * LabourCost.sub_total(self)
        return profit

    def grand_total(self):
        grand_total = LabourCost.sub_total(self) + LabourCost.profit_cost(self)
        return grand_total

    def unit_cost(self):
        unit_c = LabourCost.grand_total(self) / LabourCost._qty_paper
        return unit_c


poster = LabourCost(None, None, None)
