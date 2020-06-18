from BookWork.Param import ParamsBook


class MaterialCostBook(ParamsBook):
    _one_colour_page = 0
    _fullColourPages = 0
    _oneColourPages = 0
    _fc = 0
    _sc = 0
    _pl_c = 0
    _cmyk = 0
    _yk = 0

    def __init__(self, over_head, cp_ream, co_plate, number_color, film, co_separation, part_color, cover_hue, *args,
                 **kwargs):
        self.__overHead = over_head
        self.__CPR = cp_ream
        self.__COP = co_plate
        self.__numColor = number_color
        self.__flat = film
        self.__COS = co_separation
        self.__partColour = part_color
        self.__cover_hue = cover_hue

    def set_values_m(self, over_head, cp_ream, co_plate, number_color, film, co_separation, part_color, cover_hue):
        self.__overHead = over_head
        self.__CPR = cp_ream
        self.__COP = co_plate
        self.__numColor = number_color
        self.__flat = film
        self.__COS = co_separation
        self.__partColour = part_color
        self.__cover_hue = cover_hue

        MaterialCostBook._cmyk = self.__numColor
        MaterialCostBook._yk = self.__cover_hue

    def paper_cost(self):
        pc = MaterialCostBook.number_of_reams(self) * self.__CPR
        return pc

    def plate_cost(self):

        if self.__numColor == 1:
            if MaterialCostBook._spine > 0:
                if MaterialCostBook._yk == 1:
                    number_of_plates = (MaterialCostBook.number_of_section(self) * 2 * self.__numColor) // \
                                       MaterialCostBook.number_of_section_to_view(self) + MaterialCostBook._yk
                    MaterialCostBook._pl_c = self.__COP * number_of_plates

                elif MaterialCostBook._yk == 4:
                    number_of_plates = (MaterialCostBook.number_of_section(self) * 2 * self.__numColor) // \
                                       MaterialCostBook.number_of_section_to_view(self) + MaterialCostBook._yk
                    MaterialCostBook._pl_c = self.__COP * number_of_plates

            elif MaterialCostBook._spine == 0:
                number_of_plates = (MaterialCostBook.number_of_section(self) * 2 * self.__numColor) // \
                                   MaterialCostBook.number_of_section_to_view(self)
                MaterialCostBook._pl_c = self.__COP * number_of_plates

        elif self.__partColour > 0:
            MaterialCostBook._fullColourPages = (self.__partColour / MaterialCostBook._page) * \
                                                MaterialCostBook.number_of_section(self)
            MaterialCostBook._oneColourPages = MaterialCostBook.number_of_section(self) - \
                                               MaterialCostBook._fullColourPages

            if MaterialCostBook._spine > 0:
                if MaterialCostBook._yk == 4:
                    number_of_plates = ((MaterialCostBook._fullColourPages * 2 * self.__numColor) //
                                        MaterialCostBook.number_of_section_to_view(self)) + \
                                       ((MaterialCostBook._oneColourPages * 2) //
                                        MaterialCostBook.number_of_section_to_view(self)) + MaterialCostBook._yk
                    MaterialCostBook._pl_c = self.__COP * number_of_plates

                elif MaterialCostBook._yk == 1:
                    number_of_plates = ((MaterialCostBook._fullColourPages * 2 * self.__numColor) //
                                        MaterialCostBook.number_of_section_to_view(self)) + \
                                       ((MaterialCostBook._oneColourPages * 2) //
                                        MaterialCostBook.number_of_section_to_view(self)) + MaterialCostBook._yk
                    MaterialCostBook._pl_c = self.__COP * number_of_plates

            elif MaterialCostBook._spine == 0:
                number_of_plates = ((MaterialCostBook._fullColourPages * 2 * self.__numColor) //
                                    MaterialCostBook.number_of_section_to_view(self)) + \
                                   (MaterialCostBook._oneColourPages * 2) // \
                                   MaterialCostBook.number_of_section_to_view(self)
                MaterialCostBook._pl_c = self.__COP * number_of_plates

        else:
            if MaterialCostBook._spine > 0:
                if MaterialCostBook._yk == 4:
                    number_of_plates = self.__COS * 2 * MaterialCostBook.number_of_section(self) + MaterialCostBook._yk
                    MaterialCostBook._pl_c = self.__COP * number_of_plates

                elif MaterialCostBook._yk == 1:
                    number_of_plates = self.__COS * 2 * MaterialCostBook.number_of_section(self) + MaterialCostBook._yk
                    MaterialCostBook._pl_c = self.__COP * number_of_plates

            elif MaterialCostBook._spine == 0:
                number_of_plates = self.__COS * 2 * MaterialCostBook.number_of_section(self)
                MaterialCostBook._pl_c = self.__COP * number_of_plates

        return MaterialCostBook._pl_c

    def film_cost(self):
        if MaterialCostBook._cmyk == 1:
            self.__partColour = 0

        if self.__partColour > 0:
            if MaterialCostBook._yk == 1 and self.__numColor == 4:
                MaterialCostBook._fc = MaterialCostBook._oneColourPages * 2 * self.__flat + \
                                       (MaterialCostBook._yk * self.__flat)

            elif MaterialCostBook._yk == 4 and self.__numColor == 4:
                MaterialCostBook._fc = MaterialCostBook._oneColourPages * 2 * self.__flat

        elif self.__partColour == 0:

            if MaterialCostBook._yk == 1 and self.__numColor == 1:
                MaterialCostBook._fc = MaterialCostBook.number_of_section(self) * 2 * self.__numColor * self.__flat \
                                       + (MaterialCostBook._yk * self.__flat)

            elif MaterialCostBook._yk == 1 and self.__numColor == 4:
                MaterialCostBook._fc = (MaterialCostBook._yk * self.__flat)

            elif MaterialCostBook._yk == 4 and self.__numColor == 1:
                MaterialCostBook._fc = MaterialCostBook.number_of_section(self) * 2 * self.__numColor * self.__flat

            elif self.__numColor == 1:
                MaterialCostBook._fc = MaterialCostBook.number_of_section(self) * 2 * self.__numColor * self.__flat

            else:
                MaterialCostBook._fc = 0

        return MaterialCostBook._fc

    def separation_cost(self):
        if MaterialCostBook._cmyk == 1:
            self.__partColour = 0

        if self.__partColour > 0:
            if MaterialCostBook._yk == 1 and self.__numColor == 4:
                sc = MaterialCostBook._fullColourPages * 2 * self.__COS
                MaterialCostBook._sc = sc + MaterialCostBook.film_cost(self)

            elif MaterialCostBook._yk == 4 and self.__numColor == 4:
                sc = (MaterialCostBook._fullColourPages * 2 * self.__COS) + (2 * self.__COS)
                MaterialCostBook._sc = MaterialCostBook.film_cost(self) + sc

        elif self.__partColour == 0:
            if MaterialCostBook._yk == 1 and self.__numColor == 1:
                MaterialCostBook._sc = MaterialCostBook.film_cost(self)

            elif MaterialCostBook._yk == 1 and self.__numColor == 4:
                sc = MaterialCostBook.number_of_section(self) * 2 * self.__COS
                MaterialCostBook._sc = sc + MaterialCostBook.film_cost(self)

            elif MaterialCostBook._yk == 4 and self.__numColor == 1:
                MaterialCostBook._sc = MaterialCostBook.film_cost(self) + (MaterialCostBook._yk * self.__COS)

            elif self.__numColor == 1:
                MaterialCostBook._sc = MaterialCostBook.film_cost(self)

            else:
                MaterialCostBook._sc = MaterialCostBook.number_of_section(self) * 2 * self.__COS

        return MaterialCostBook._sc

    def material_cost(self):
        mc = MaterialCostBook.paper_cost(self) + MaterialCostBook.plate_cost(self) + \
             MaterialCostBook.separation_cost(self)
        return mc

    def over_head(self):
        oh_per = (self.__overHead / 100) * MaterialCostBook.material_cost(self)
        return oh_per

    def total_material_cost(self):
        t_m_c = MaterialCostBook.material_cost(self) + MaterialCostBook.over_head(self)
        return t_m_c
