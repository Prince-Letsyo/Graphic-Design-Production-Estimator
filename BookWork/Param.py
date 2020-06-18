class ParamsBook:
    _is_book = True
    _spine = 0
    wrong = ''

    # Cover
    _newCover_x_size = 0
    _newCover_y_size = 0
    _numReamCover = 0
    _workingSize_x_cover = 0
    _workingSize_y_cover = 0
    _up_cover = 0
    _out_cover = 0
    _working_paper_size = 0

    # Pages
    _page = 0
    _working_x = 0
    _working_y = 0
    _vertical_page = 0
    _diagonal_page = 0
    _xV = 0
    _yV = 0
    _xD = 0
    _yD = 0
    _qty_book = 0

    def __init__(self, machine_size_x, machine_size_y, finish_size_x, finish_size_y, stock_size_x, stock_size_y, pages,
                 quantity, spoilage, spine, *args, **kwargs):
        self.__machineSize_x = machine_size_x
        self.__machineSize_y = machine_size_y
        self.__finishSize_x = finish_size_x
        self.__finishSize_y = finish_size_y
        self.__stockSize_x = stock_size_x
        self.__stockSize_y = stock_size_y
        self.__quantity = quantity
        self.__pages = pages
        self.__spoilage = spoilage
        self.__spine = spine

    def set_values_b(self, machine_size_x, machine_size_y, finish_size_x, finish_size_y, stock_size_x, stock_size_y,
                     pages, quantity, spoilage, spine):
        self.__machineSize_x = machine_size_x
        self.__machineSize_y = machine_size_y
        self.__finishSize_x = finish_size_x
        self.__finishSize_y = finish_size_y
        self.__stockSize_x = stock_size_x
        self.__stockSize_y = stock_size_y
        self.__quantity = quantity
        self.__pages = pages
        self.__spoilage = spoilage
        self.__spine = spine

        ParamsBook._spine = self.__spine

        # Pages
        ParamsBook._working_x = (self.__finishSize_x * 2) + 0.5
        ParamsBook._working_y = (self.__finishSize_y * 2) + 1

        # Vertically
        ParamsBook._xV = self.__machineSize_x // ParamsBook._working_x
        ParamsBook._yV = self.__machineSize_y // ParamsBook._working_y

        # Diagonally
        ParamsBook._xD = self.__machineSize_x // ParamsBook._working_y
        ParamsBook._yD = self.__machineSize_y // ParamsBook._working_x

        ParamsBook._vertical_page = ParamsBook._xV * ParamsBook._yV
        ParamsBook._diagonal_page = ParamsBook._xD * ParamsBook._yD

        # Cover
        ParamsBook._qty_book = self.__quantity

    def number_of_section(self):
        ParamsBook._page = self.__pages
        num_of_pv = 4
        flat = 2
        num_of_ps = num_of_pv * flat
        num_of_section = ParamsBook._page / num_of_ps
        return num_of_section

    def number_of_section_to_view(self):
        try:
            # WORKING SIZE
            nums = [ParamsBook._diagonal_page, ParamsBook._vertical_page]
            maximums_up = max(nums)
            section_view = round(maximums_up)
            return section_view
        except ZeroDivisionError:
            ParamsBook.wrong = "Please check your finish size."
            return ParamsBook.wrong

    def number_of_panels(self):
        try:
            panel = ParamsBook.number_of_section(self) / ParamsBook.number_of_section_to_view(self)
            return panel
        except ZeroDivisionError:
            ParamsBook.wrong = "Please check your finish size."
            return ParamsBook.wrong

    def number_of_out_of_section(self):
        try:
            # New Working size
            if ParamsBook._vertical_page > ParamsBook._diagonal_page:
                x_working_size = (ParamsBook._xV * ParamsBook._working_x)
                y_working_size = (ParamsBook._yV * ParamsBook._working_y)
            else:
                x_working_size = (ParamsBook._xD * ParamsBook._working_y)
                y_working_size = (ParamsBook._yD * ParamsBook._working_x)

            # NUMBER OUT
            # Vertical_out
            xv_out = self.__stockSize_x // x_working_size
            yv_out = self.__stockSize_y // y_working_size

            # Diagonal_out
            xd_out = self.__stockSize_x // y_working_size
            yd_out = self.__stockSize_y // x_working_size

            diagonal_out = xd_out * yd_out
            vertical_out = xv_out * yv_out

            nums = [diagonal_out, vertical_out]
            maximums_out = max(nums)
            return round(maximums_out)
        except ZeroDivisionError:
            ParamsBook.wrong = "Please check your Machine size."
            return ParamsBook.wrong

    def number_of_working_size_sheet(self):
        sheets = self.__quantity * ParamsBook.number_of_section(self) / ParamsBook.number_of_section_to_view(self)
        return sheets

    def stock_size_sheet(self):
        try:
            sheets = ParamsBook.number_of_working_size_sheet(self) / ParamsBook.number_of_out_of_section(self)
            return sheets
        except ZeroDivisionError:
            ParamsBook.wrong = "Please check your Stock size."
            return ParamsBook.wrong

    def spoilage(self):
        spoilt_sheet = (self.__spoilage / 100) * ParamsBook.stock_size_sheet(self)
        return spoilt_sheet

    def total_sss(self):
        total_sss = ParamsBook.stock_size_sheet(self) + ParamsBook.spoilage(self)
        return total_sss

    def ream_for_cover(self):
        try:
            # Cover Size
            i = (self.__finishSize_x * 2) + self.__spine
            j = self.__finishSize_y

            if i > j:
                ParamsBook._newCover_x_size = j
                ParamsBook._newCover_y_size = i
            else:
                ParamsBook._newCover_x_size = i
                ParamsBook._newCover_y_size = j

            if ParamsBook._newCover_x_size > 0 and ParamsBook._newCover_y_size > 0:
                # New Cover WorkingSize
                ParamsBook._workingSize_x_cover = ParamsBook._newCover_x_size + 0.5
                ParamsBook._workingSize_y_cover = ParamsBook._newCover_y_size + 0.5

                # Number of Cover to view (Machine)
                # Vertically
                xv_cover = self.__machineSize_x // ParamsBook._workingSize_x_cover
                yv_cover = self.__machineSize_y // ParamsBook._workingSize_y_cover

                # Diagonally
                xd_cover = self.__machineSize_x // ParamsBook._workingSize_y_cover
                yd_cover = self.__machineSize_y // ParamsBook._workingSize_x_cover

                vertical_cover = xv_cover * yv_cover
                diagonal_cover = xd_cover * yd_cover

                nums_up = [diagonal_cover, vertical_cover]
                maximums_up = max(nums_up)
                ParamsBook._up_cover = round(maximums_up)

                # New Working size
                if vertical_cover > diagonal_cover:
                    x_working_size = (xv_cover * ParamsBook._workingSize_x_cover)
                    y_working_size = (yv_cover * ParamsBook._workingSize_y_cover)
                else:
                    x_working_size = (xd_cover * ParamsBook._workingSize_y_cover)
                    y_working_size = (yd_cover * ParamsBook._workingSize_x_cover)

                # NUMBER OUT
                # Vertical_out
                xv_out = self.__stockSize_x // x_working_size
                yv_out = self.__stockSize_y // y_working_size

                # Diagonal_out
                xd_out = self.__stockSize_x // y_working_size
                yd_out = self.__stockSize_y // x_working_size

                diagonal_out = xd_out * yd_out
                vertical_out = xv_out * yv_out

                nums = [diagonal_out, vertical_out]
                maximums_out = max(nums)
                ParamsBook._out_cover = round(maximums_out)

                # Working Size for cover
                ParamsBook._working_paper_size = self.__quantity / ParamsBook._up_cover

                # Stock Size for cover
                stock_paper_size = ParamsBook._working_paper_size / ParamsBook._out_cover

                # number of ream for cover
                ParamsBook._numReamCover = stock_paper_size / 500

            return ParamsBook._numReamCover
        except ZeroDivisionError:
            ParamsBook.wrong = "Please check your finish size."
            return ParamsBook.wrong

    def number_of_reams(self):
        reams = ParamsBook.total_sss(self) / 500
        if self.__spine > 0:
            reams += ParamsBook.ream_for_cover(self)
        return reams
