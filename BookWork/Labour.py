from BookWork.Material import MaterialCostBook


class LabourCostBook(MaterialCostBook):
    _num_imp = 0

    def __init__(self, profit, c_o_f, c_p_i):
        self.__profit = profit
        self.__COF = c_o_f
        self.__CPI = c_p_i

    def set_values_l(self, profit, c_o_f, c_p_i):
        self.__profit = profit
        self.__COF = c_o_f
        self.__CPI = c_p_i

    def num_impression(self):

        if LabourCostBook.film_cost(self) > 0:
            if LabourCostBook._spine > 0:
                one_colour_imp = (LabourCostBook._oneColourPages * 2 * LabourCostBook._qty_book) \
                                 / LabourCostBook.number_of_section_to_view(self)

                full_colour_imp = (LabourCostBook._fullColourPages * 2 * LabourCostBook._cmyk * LabourCostBook._qty_book)\
                                  / LabourCostBook.number_of_section_to_view(self)
                cover_imp = LabourCostBook._working_paper_size * LabourCostBook._yk
                LabourCostBook._num_imp = one_colour_imp + full_colour_imp + cover_imp

            elif LabourCostBook._spine == 0:
                one_colour_imp = (LabourCostBook._oneColourPages * 2 * LabourCostBook._qty_book) \
                                 / LabourCostBook.number_of_section_to_view(self)
                full_colour_imp = (LabourCostBook._fullColourPages * 2 * LabourCostBook._cmyk *
                                   LabourCostBook._qty_book) / LabourCostBook.number_of_section_to_view(self)
                LabourCostBook._num_imp = one_colour_imp + full_colour_imp

        elif LabourCostBook.film_cost(self) == 0:
            if LabourCostBook._spine > 0:
                w_imp = (LabourCostBook._qty_book * LabourCostBook._cmyk) / \
                        LabourCostBook.number_of_section_to_view(self)
                cover_imp = LabourCostBook._working_paper_size * LabourCostBook._yk

                LabourCostBook._num_imp = w_imp + cover_imp

            elif LabourCostBook._spine == 0:
                w_imp = (LabourCostBook._qty_book * LabourCostBook._cmyk) \
                        / LabourCostBook.number_of_section_to_view(self)
                LabourCostBook._num_imp = w_imp

        return LabourCostBook._num_imp

    def cost_of_impression(self):
        cost_of_imp = (LabourCostBook.num_impression(self) / 1000) * self.__CPI
        return cost_of_imp

    def cost_of_finishing(self):
        finishing_cost = self.__COF * LabourCostBook._qty_book
        return finishing_cost

    def cost_of_labour(self):
        labour_cost = LabourCostBook.cost_of_impression(self) + LabourCostBook.cost_of_finishing(self)
        return labour_cost

    def sub_total(self):
        sub_total_cost = LabourCostBook.cost_of_labour(self) + LabourCostBook.total_material_cost(self)
        return sub_total_cost

    def profit(self):
        profit = (self.__profit / 100) * LabourCostBook.sub_total(self)
        return profit

    def grand_total(self):
        grand_total = LabourCostBook.sub_total(self) + LabourCostBook.profit(self)
        return grand_total

    def unit_cost(self):
        unit_c = LabourCostBook.grand_total(self) / LabourCostBook._qty_book
        return unit_c


books = LabourCostBook(None, None, None)
