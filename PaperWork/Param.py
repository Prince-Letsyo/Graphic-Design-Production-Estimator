class ParamsPaper:
    _num_wss = 0
    _x_v = 0
    _y_v = 0
    _x_d = 0
    _y_d = 0
    _vertical = 0
    _diagonal = 0
    _qty_paper = 0
    wrong = ''
    _is_poster = True

    def __init__(self, machine_size_x, machine_size_y, finish_size_x, finish_size_y, quantity, stock_size_x,
                 stock_size_y, spoilage, *args, **kwargs):
        self.__machineSize_x = machine_size_x
        self.__machineSize_y = machine_size_y
        self.__finishSize_x = finish_size_x
        self.__finishSize_y = finish_size_y
        self.__stockSize_x = stock_size_x
        self.__stockSize_y = stock_size_y
        self.__quantity = quantity
        self.__spoilage = spoilage

    def set_values(self, machine_size_x, machine_size_y, finish_size_x, finish_size_y, quantity, stock_size_x,
                   stock_size_y, spoilage):
        self.__machineSize_x = machine_size_x
        self.__machineSize_y = machine_size_y
        self.__finishSize_x = finish_size_x
        self.__finishSize_y = finish_size_y
        self.__stockSize_x = stock_size_x
        self.__stockSize_y = stock_size_y
        self.__quantity = quantity
        self.__spoilage = spoilage

        # Vertically
        ParamsPaper._x_v = self.__machineSize_x // self.__finishSize_x
        ParamsPaper._y_v = self.__machineSize_y // self.__finishSize_y

        # Diagonally
        ParamsPaper._x_d = self.__machineSize_x // self.__finishSize_y
        ParamsPaper._y_d = self.__machineSize_y // self.__finishSize_x

        ParamsPaper._vertical = ParamsPaper._x_v * ParamsPaper._y_v
        ParamsPaper._diagonal = ParamsPaper._x_d * ParamsPaper._y_d

        ParamsPaper._qty_paper = self.__quantity

    def number_of_up(self):
        nums = [ParamsPaper._diagonal, ParamsPaper._vertical]
        maximums = max(nums)
        return round(maximums)

    def number_of_out(self):
        # WORKING SIZE
        if ParamsPaper._vertical > ParamsPaper._diagonal:
            x_working_size = (ParamsPaper._x_v * self.__finishSize_x) + 0.5
            y_working_size = (ParamsPaper._y_v * self.__finishSize_y) + 0.5

        else:
            x_working_size = (ParamsPaper._x_d * self.__finishSize_y) + 0.5
            y_working_size = (ParamsPaper._y_d * self.__finishSize_x) + 0.5

        # Number 0f out
        # Vertical_out
        x_v_out = self.__stockSize_x // x_working_size
        y_v_out = self.__stockSize_y // y_working_size

        # Diagonal_out
        x_d_out = self.__stockSize_x // y_working_size
        y_d_out = self.__stockSize_y // x_working_size

        diagonal_out = x_d_out * y_d_out
        vertical_out = x_v_out * y_v_out

        nums = [diagonal_out, vertical_out]
        maximums = max(nums)
        return round(maximums)

    def number_of_wss(self):
        try:
            ParamsPaper._num_wss = self.__quantity / self.number_of_up()
            return ParamsPaper._num_wss
        except ZeroDivisionError:
            ParamsPaper.wrong = 'PLease check your Machine size.'
            return ParamsPaper.wrong

    def number_of_sss(self):
        try:
            return ParamsPaper.number_of_wss(self) / ParamsPaper.number_of_out(self)
        except ZeroDivisionError:
            ParamsPaper.wrong = 'PLease check your Stock size.'
            return ParamsPaper.wrong

    def spoilage_percent(self):
        sp = (self.__spoilage / 100) * ParamsPaper.number_of_sss(self)
        return sp

    def total_sss(self):
        ss = ParamsPaper.number_of_sss(self) + ParamsPaper.spoilage_percent(self)
        return ss

    def number_of_ream(self):
        ts = ParamsPaper.total_sss(self) / 500
        return ts
