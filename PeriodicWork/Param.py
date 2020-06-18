class ParamsPeriodic:
    _periods_to_view_per_section = 0
    _working_size_x = 0
    _working_size_y = 0
    _xv_up = 0
    _yv_up = 0
    _xd_up = 0
    _yd_up = 0
    _vertical_period = 0
    _diagonal_period = 0
    _front_back = False
    _qty_paper = 0
    wrong = ''

    def __init__(self, machine_size_x, machine_size_y, finish_size_x, finish_size_y, quantity, stock_size_x,
                 stock_size_y, spoilage, period_per_flat, number_of_periods):
        self.__machineSize_x = machine_size_x
        self.__machineSize_y = machine_size_y
        self.__finishSize_x = finish_size_x
        self.__finishSize_y = finish_size_y
        self.__stockSize_x = stock_size_x
        self.__stockSize_y = stock_size_y
        self.__quantity = quantity
        self.__spoilage = spoilage
        self.__period_per_flat = period_per_flat
        self.__number_of_periods = number_of_periods

    def set_values_period(self, machine_size_x, machine_size_y, finish_size_x, finish_size_y, quantity, stock_size_x,
                          stock_size_y, spoilage, period_per_flat, number_of_periods):
        self.__machineSize_x = machine_size_x
        self.__machineSize_y = machine_size_y
        self.__finishSize_x = finish_size_x
        self.__finishSize_y = finish_size_y
        self.__stockSize_x = stock_size_x
        self.__stockSize_y = stock_size_y
        self.__quantity = quantity
        self.__spoilage = spoilage
        self.__period_per_flat = period_per_flat
        self.__number_of_periods = number_of_periods

        ParamsPeriodic._working_size_x = self.__finishSize_x + 0.5
        ParamsPeriodic._working_size_y = self.__finishSize_y + 0.5

        # Vertical
        ParamsPeriodic._xv_up = self.__machineSize_x // ParamsPeriodic._working_size_x
        ParamsPeriodic._yv_up = self.__machineSize_y // ParamsPeriodic._working_size_y

        # Diagonal
        ParamsPeriodic._xd_up = self.__machineSize_x // ParamsPeriodic._working_size_y
        ParamsPeriodic._yd_up = self.__machineSize_y // ParamsPeriodic._working_size_x

        ParamsPeriodic._vertical_period = ParamsPeriodic._xv_up * ParamsPeriodic._yv_up
        ParamsPeriodic._diagonal_period = ParamsPeriodic._xd_up * ParamsPeriodic._yd_up
        ParamsPeriodic._qty_paper = self.__quantity

    def number_of_periods_to_view(self):
        if ParamsPeriodic._front_back:
            periods_to_view_per_panel = (self.__number_of_periods / self.__period_per_flat) / 2
        else:
            periods_to_view_per_panel = self.__number_of_periods / self.__period_per_flat
        return round(periods_to_view_per_panel)

    def panels_to_view(self):
        num_up = [ParamsPeriodic._vertical_period, ParamsPeriodic._diagonal_period]
        maximum_up = max(num_up)
        return round(maximum_up)

    def number_of_out(self):
        try:
            # new_working_size
            if ParamsPeriodic._vertical_period > ParamsPeriodic._diagonal_period:
                new_working_size_x = ParamsPeriodic._working_size_x * ParamsPeriodic._xv_up
                new_working_size_y = ParamsPeriodic._working_size_y * ParamsPeriodic._yv_up
            else:
                new_working_size_x = ParamsPeriodic._working_size_x * ParamsPeriodic._yd_up
                new_working_size_y = ParamsPeriodic._working_size_y * ParamsPeriodic._xd_up

            # Vertical_out
            xv_out = self.__stockSize_x // new_working_size_x
            yv_out = self.__stockSize_y // new_working_size_y

            # Diagonal_out
            xd_out = self.__stockSize_x // new_working_size_y
            yd_out = self.__stockSize_y // new_working_size_x

            diagonal_out = xd_out * yd_out
            vertical_out = xv_out * yv_out

            num_out = [diagonal_out, vertical_out]
            maximums = max(num_out)
            return round(maximums)
        except ZeroDivisionError:
            ParamsPeriodic.wrong = 'PLease check your finish size.'
            return ParamsPeriodic.wrong

    def total_number_of_wss(self):
        try:
            wss = self.__quantity * ParamsPeriodic.number_of_periods_to_view(self) / ParamsPeriodic.panels_to_view(self)
            return wss
        except ZeroDivisionError:
            ParamsPeriodic.wrong = 'PLease check your Machine size.'
            return ParamsPeriodic.wrong

    def number_of_sss(self):
        try:
            sss = ParamsPeriodic.total_number_of_wss(self) / ParamsPeriodic.number_of_out(self)
            return sss
        except ZeroDivisionError:
            ParamsPeriodic.wrong = 'PLease check your Stock size.'
            return ParamsPeriodic.wrong

    def spoilage(self):
        spoilage = (self.__spoilage / 100) * ParamsPeriodic.number_of_sss(self)
        return spoilage

    def total_number_of_sss(self):
        total_sss = ParamsPeriodic.number_of_sss(self) + ParamsPeriodic.spoilage(self)
        return total_sss

    def number_of_reams(self):
        reams = ParamsPeriodic.total_number_of_sss(self) / 500
        return reams
