from tkinter import *
from tkinter import messagebox
from PaperWork.Labour import poster
from BookWork.Labour import books
from PeriodicWork.Labour import calender

HEIGHT = 1200
WIDTH = 700
bg = "#b3daff"
nav = "#80c1ff"
nav_paper = "#80c1ff"
nav_book = "#80c1ff"
nav_period = "#80c1ff"
answer = "#e6f3ff"
fon = "#ffffff"

change_button_paper = False
change_button_book = False
change_button_period = False
root = Tk()
root.title("GDP Estimator")
root.geometry(str(HEIGHT) + "x" + str(WIDTH))
root.configure(background=bg)


def work_place():
    global nav_paper
    global MS_x
    global MS_y
    global FS_x
    global FS_y
    global SS_x
    global SS_y
    global Qty_needed
    global Spoilage_given
    global Spoilage_given
    global colour
    global Cost_per_Ream_given
    global Cost_per_Plate_given
    global Cost_per_Separation_given
    global overhead_given
    global num_of_pages_given
    global spine_given

    nav_tab = Frame(root, bg=nav, bd=0)
    nav_tab.place(relx=0, rely=0, relwidth=1, relheight=0.05)

    nav_button = Frame(nav_tab, bg=fon, bd=0)
    nav_button.place(relx=0, rely=0, relwidth=0.32, relheight=1)

    body_content = Frame(root, bg=bg, bd=0)
    body_content.place(relx=0, rely=0.05, relwidth=1, relheight=0.95)

    cal_slide = Frame(body_content, bg=bg, bd=0)
    cal_slide.place(relx=0, rely=0, relwidth=0.3148, relheight=1)

    cal_slide_parameter = Frame(cal_slide, bg=bg, bd=0)
    cal_slide_parameter.place(relx=0.03, rely=0.01, width=390, relheight=0.39)

    cal_slide_material = Frame(cal_slide, bg=bg, bd=0)
    cal_slide_material.place(relx=0.03, rely=0.415, width=370, relheight=0.28)

    cal_slide_labour = Frame(cal_slide, bg=bg, bd=0)
    cal_slide_labour.place(relx=0.03, rely=0.7, width=370, relheight=0.28)

    cal_slide_result = Frame(cal_slide, bg=bg, bd=0)
    cal_slide_result.place(relx=0.03, rely=0.9, relwidth=1, relheight=0.05)

    ans_slide = Frame(body_content, bg=answer, bd=0)
    ans_slide.place(relx=0.32, rely=0, relwidth=0.68, relheight=1)

    ans_slide_hold = Frame(ans_slide, bg='#ffffff', bd=0)
    ans_slide_hold.place(relwidth=0.95, relheight=0.95, relx=0.025, rely=0.025)

    scrol = Scrollbar(ans_slide_hold)
    scrol.place(relwidth=0.02, relheight=1, relx=0.98)

    listbox = Listbox(ans_slide_hold, yscrollcommand=scrol.set)

    scrol.config(command=listbox.yview)

    # Parameter frame
    parameters = LabelFrame(cal_slide_parameter, text="Parameters", pady=10, padx=10, font=10, bg=bg)

    # Material frame
    material = LabelFrame(cal_slide_material, text="Cost of material", pady=10, padx=10, font=10, bg=bg)

    # Labour frame
    labour = LabelFrame(cal_slide_labour, text="Cost of Labour", pady=10, padx=10, font=10, bg=bg)

    # Machine size
    ms = Label(parameters, text="Machine Size: ", bg=bg)
    MS_x = Entry(parameters, width=7, )
    by_ms = Label(parameters, text="x", bg=bg)
    MS_y = Entry(parameters, width=7)

    # Finish size
    fs = Label(parameters, text="Finish Size: ", bg=bg)
    FS_x = Entry(parameters, width=7)
    by_fs = Label(parameters, text="x", bg=bg)
    FS_y = Entry(parameters, width=7)

    # Stock size
    ss = Label(parameters, text="Stock Size: ", bg=bg)
    SS_x = Entry(parameters, width=7)
    by_ss = Label(parameters, text="x", bg=bg)
    SS_y = Entry(parameters, width=7)

    # Quantity
    qty = Label(parameters, text="Quantity: ", bg=bg)
    Qty_needed = Entry(parameters, width=21)

    # Spoilage
    spoilage = Label(parameters, text="Spoilage: ", bg=bg)
    Spoilage_given = Entry(parameters, width=7)
    Spoilage_given.insert(END, 0)

    # Page of colours
    page_colour = Label(parameters, text="Colour: ", bg=bg)
    colour = IntVar()
    colour.set(4)

    Radiobutton(parameters, text="1", variable=colour, value=1, bg=bg).grid(row=6, column=1, )
    Radiobutton(parameters, text="4", variable=colour, value=4, bg=bg).grid(row=6, column=2)

    # Cover of colours
    cover_colour = Label(parameters, text="Cover colour: ", bg=bg)
    cover = IntVar()
    cover.set(4)

    cover_1 = Radiobutton(parameters, text="1", variable=cover, value=1, bg=bg)
    cover_4 = Radiobutton(parameters, text="4", variable=cover, value=4, bg=bg)

    # Cost per Ream
    cost_per_ream = Label(material, text="Cost per Ream: ", bg=bg)
    Cost_per_Ream_given = Entry(material, width=7)

    # Cost per Plate
    cost_per_plate = Label(material, text="Cost per Plate: ", bg=bg)
    Cost_per_Plate_given = Entry(material, width=7)

    # Cost per Separation
    cost_per_separation = Label(material, text="Cost per Separation: ", bg=bg)
    Cost_per_Separation_given = Entry(material, width=7)

    # Overhead
    overhead = Label(material, text="Overhead: ", bg=bg)
    overhead_given = Entry(material, width=7)
    overhead_given.insert(END, 0)

    # Cost per Film
    cost_per_film = Label(material, text="Cost of film per Flat: ", bg=bg)
    cost_per_film_given = Entry(material, width=7)

    # partColour
    part_colour = Label(material, text="Part Colour: ", bg=bg)
    part_colour_given = Entry(material, width=7)

    # Number of Pages
    num_of_pages = Label(parameters, text="Number Of pages: ", bg=bg)
    num_of_pages_given = Entry(parameters, width=7)

    # Number of Pages
    num_of_periods = Label(parameters, text="Number Of Periods: ", bg=bg)
    num_of_periods_given = Entry(parameters, width=7)

    # Spine
    spine = Label(parameters, text="Spine: ", bg=bg)
    spine_given = Entry(parameters, width=7)
    spine_given.insert(END, 0)

    # Profit
    profit = Label(labour, text="Profit: ", bg=bg)
    profit_given = Entry(labour, width=7)

    # Cost of finishing
    cost_of_finishing = Label(labour, text="Cost of Finishing: ", bg=bg)
    cost_of_finishing_given = Entry(labour, width=7)

    # Cost of impression
    cost_of_impression = Label(labour, text="Cost of Impression: ", bg=bg)
    cost_of_impression_given = Entry(labour, width=7)

    number_of_period = Label(parameters, text='Period per flat: ', bg=bg)
    number_of_period_given = Entry(parameters, width=7)

    def calculate():
        if MS_x.get() != "" and MS_y.get() != "" and FS_x.get() != "" and SS_x.get() != "" and SS_y.get() != "" and \
                Qty_needed.get() != "" and Spoilage_given.get() != "" and Cost_per_Ream_given.get() != "" and \
                Cost_per_Plate_given.get() != "" and Cost_per_Separation_given.get() != "" and overhead_given.get() \
                != "" and profit_given.get() != "" and cost_of_impression_given.get() != "":
            try:
                ms_x = float(MS_x.get())
                ms_y = float(MS_y.get())
                fs_x = float(FS_x.get())
                fs_y = float(FS_y.get())
                ss_x = float(SS_x.get())
                ss_y = float(SS_y.get())
                qty_needed = float(Qty_needed.get())
                spoilage = float(Spoilage_given.get())
                color = float(colour.get())
                c_per_r = float(Cost_per_Ream_given.get())
                c_per_p = float(Cost_per_Plate_given.get())
                c_per_s = float(Cost_per_Separation_given.get())
                c_per_fin = float(cost_of_finishing_given.get())
                c_per_imp = float(cost_of_impression_given.get())
                over_h = float(overhead_given.get())
                film_p = 0
                part_color_p = 0
                profit_g = float(profit_given.get())

                poster.set_values(ms_x, ms_y, fs_x, fs_y, qty_needed, ss_x, ss_y, spoilage)
                poster.set_values_paper(over_h, c_per_r, c_per_p, color, film_p, c_per_s, part_color_p)
                poster.set_values_paper_l(profit_g, c_per_fin, c_per_imp)

                done = [

                    # ParamsPaper
                    " ",
                    "Paper Parameter"
                    ,
                    "===================================================================",
                    "Number of out.........................." + str(poster.number_of_out()),
                    "Number of up..........................." + str(poster.number_of_up()),
                    "Working Size Sheet.....................{0:.2f}".format(poster.number_of_wss()),
                    "Stock Size Sheet.......................{0:.2f}".format(poster.number_of_sss()),
                    "Spoilage...............................{0:.2f}".format(poster.spoilage_percent()),
                    "Total stock size sheet.................{0:.2f}".format(poster.total_sss()),
                    "Number of ream.........................{0:.2f}".format(poster.number_of_ream()),

                    # MaterialCostBook
                    " ",
                    " ",
                    "Material Cost"
                    ,
                    "===================================================================",
                    "Cost of paper..........................{0:.2f}".format(poster.paper_cost()),
                    "Cost of plate..........................{0:.2f}".format(poster.plate_cost()),
                    "Cost of separation.....................{0:.2f}".format(poster.separation_cost()),
                    "Cost of material.......................{0:.2f}".format(poster.material_cost()),
                    "Over head cost.........................{0:.2f}".format(poster.over_head()),
                    "Total material cost....................{0:.2f}".format(poster.total_material_cost()),
                    " ",
                    " ",
                    "Labour Cost",
                    "===================================================================",
                    "Number of impression...................{0:.2f}".format(poster.num_impression()),
                    "Cost of impression.....................{0:.2f}".format(poster.cost_of_impression()),
                    "Cost of finishing......................{0:.2f}".format(poster.cost_of_finishing()),
                    "Cost of labour.........................{0:.2f}".format(poster.cost_of_labour()),
                    "Subtotal...............................{0:.2f}".format(poster.sub_total()),
                    "Profit.................................{0:.2f}".format(poster.profit_cost()),
                    " ",
                    " ",
                    "Grand Total",
                    "===================================================================",
                    "Grand total............................{0:.2f}".format(poster.grand_total()),

                    " ",
                    " ",
                    "Unit Cost",
                    "===================================================================",
                    "Unit cost..............................{0:.2f}".format(poster.unit_cost()),

                ]

                if len(done) == listbox.size():
                    listbox.delete(0, END)
                    for i in done:
                        listbox.insert(END, '           ' + str(i))
                else:
                    for i in done:
                        listbox.insert(END, '           ' + str(i))
                listbox.place(relwidth=0.98, relheight=1)

            except ValueError or TypeError:
                msg = ''
                if poster.wrong == '':
                    msg = "Please check your values"
                else:
                    msg = poster.wrong
                messagebox.showerror("Input Error", msg)

        else:
            messagebox.showerror("Required Fields", "Please include all fields")
            return

    result = Button(cal_slide_result, text="Result", bg=nav, command=calculate)

    def paper():
        listbox.delete(0, END)
        global change_button_paper
        global change_button_book
        global change_button_period
        global MS_x
        global MS_y
        global FS_x
        global FS_y
        global SS_x
        global SS_y
        global Qty_needed
        global Spoilage_given
        global Spoilage_given
        global colour
        global Cost_per_Ream_given
        global Cost_per_Plate_given
        global Cost_per_Separation_given
        global overhead_given
        global num_of_pages_given
        global spine_given

        change_button_paper = True
        change_button_book = False
        change_button_period = False

        change_colour()

        # Mounting machine size
        fs.grid(row=2, column=0, sticky=E)
        FS_x.grid(row=2, column=1)
        by_fs.grid(row=2, column=2)
        FS_y.grid(row=2, column=3)

        # Mounting machine size
        ms.grid(row=1, column=0, sticky=E)
        MS_x.grid(row=1, column=1)
        by_ms.grid(row=1, column=2)
        MS_y.grid(row=1, column=3)

        # Mounting Stock size
        ss.grid(row=3, column=0, sticky=E)
        SS_x.grid(row=3, column=1)
        by_ss.grid(row=3, column=2)
        SS_y.grid(row=3, column=3)

        # Mounting quantity
        qty.grid(row=4, column=0, sticky=E)
        Qty_needed.grid(row=4, column=1, columnspan=3)

        # Mounting spoilage_g
        spoilage.grid(row=5, column=0, sticky=E)
        Spoilage_given.grid(row=5, column=1, )

        # Mounting number of colours
        page_colour.grid(row=6, column=0, sticky=E)

        # Mounting Number of Pages
        num_of_pages.grid_forget()
        num_of_pages_given.grid_forget()

        # Mounting of Spine
        spine.grid_forget()
        spine_given.grid_forget()

        num_of_periods.grid_forget()
        num_of_periods_given.grid_forget()

        # Mounting Cost per Ream
        cost_per_ream.grid(row=0, column=0, sticky=E)
        Cost_per_Ream_given.grid(row=0, column=1)

        # Mounting Cost per Plate
        cost_per_plate.grid(row=1, column=0, sticky=E)
        Cost_per_Plate_given.grid(row=1, column=1)

        # Mounting Cost per Separation
        cost_per_separation.grid(row=2, column=0, sticky=E)
        Cost_per_Separation_given.grid(row=2, column=1)

        # Mounting Overhead
        overhead.grid(row=3, column=0, sticky=E)
        overhead_given.grid(row=3, column=1)

        # Mounting Cost per Film
        cost_per_film.grid_forget()
        cost_per_film_given.grid_forget()

        # Mounting partColour
        part_colour.grid_forget()
        part_colour_given.grid_forget()

        # Mounting Profit
        profit.grid(row=0, column=0, sticky=E)
        profit_given.grid(row=0, column=1)

        # Mounting Cost of finishing
        cost_of_finishing.grid(row=1, column=0, sticky=E)
        cost_of_finishing_given.grid(row=1, column=1)

        # Mounting Cost of impression
        cost_of_impression.grid(row=2, column=0, sticky=E)
        cost_of_impression_given.grid(row=2, column=1)

        # demounting cover
        cover_1.grid_forget()
        cover_4.grid_forget()
        cover_colour.grid_forget()

        # Mounting Parameter
        parameters.grid(row=1, column=0, sticky=E)

        # Mounting Material
        material.grid(row=2, column=0, )

        # Mounting Material
        labour.grid(row=3, column=0, )

        result.place(relheight=1, relwidth=1, )
        result2.place_forget()
        result3.place_forget()

        number_of_period.grid_forget()
        number_of_period_given.grid_forget()

        number_of_period.grid_forget()
        number_of_period_given.grid_forget()

    def calculate2():

        if MS_x.get() != "" and MS_y.get() != "" and FS_x.get() != "" and SS_x.get() != "" and SS_y.get() != "" and \
                Qty_needed.get() != "" and Spoilage_given.get() != "" and Cost_per_Ream_given.get() != "" and \
                Cost_per_Plate_given.get() != "" and Cost_per_Separation_given.get() != "" and overhead_given.get() != "" \
                and profit_given.get() != "" and cost_of_impression_given.get() != "" and num_of_pages_given.get() != "" \
                and cost_per_film_given.get() != "" and part_colour_given.get() != "" and spine_given.get() != "":

            try:

                if float(part_colour_given.get()) > float(num_of_pages_given.get()):
                    messagebox.showerror("Pages given error", "Full colour pages of " + str(part_colour_given.get()) +
                                         " Total number of pages " + str(num_of_pages_given.get()))

                else:
                    ms_x = float(MS_x.get())
                    ms_y = float(MS_y.get())
                    fs_x = float(FS_x.get())
                    fs_y = float(FS_y.get())
                    ss_x = float(SS_x.get())
                    ss_y = float(SS_y.get())
                    qty_needed = float(Qty_needed.get())
                    part_g = float(part_colour_given.get())
                    spoilage_g = float(Spoilage_given.get())
                    color = float(colour.get())
                    c_per_r = float(Cost_per_Ream_given.get())
                    c_per_p = float(Cost_per_Plate_given.get())
                    c_per_s = float(Cost_per_Separation_given.get())
                    c_per_fin = float(cost_of_finishing_given.get())
                    c_per_imp = float(cost_of_impression_given.get())
                    over_h = float(overhead_given.get())
                    profit_g = float(profit_given.get())
                    pages_g = float(num_of_pages_given.get())
                    film_g = float(cost_per_film_given.get())
                    spine_g = float(spine_given.get())
                    cover_h = float(cover.get())

                    books.set_values_b(ms_x, ms_y, fs_x, fs_y, ss_x, ss_y, pages_g, qty_needed, spoilage_g, spine_g)
                    books.set_values_m(over_h, c_per_r, c_per_p, color, film_g, c_per_s, part_g, cover_h)
                    books.set_values_l(profit_g, c_per_fin, c_per_imp)

                    # ParamsPaper
                    done = [
                        " ",
                        "Book Parameter"
                        ,
                        "===================================================================",
                        "Number of section........................{0:.2f}".format(books.number_of_section()),
                        "Number of section to view................" + str(books.number_of_section_to_view()),
                        "Number of out............................" + str(books.number_of_out_of_section()),
                        "Number of panel..........................{0:.2f}".format(books.number_of_panels()),
                        "Working Size Sheet.......................{0:.2f}".format(books.number_of_working_size_sheet()),
                        "Stock Size Sheet.........................{0:.2f}".format(books.stock_size_sheet()),
                        "Spoilage.................................{0:.2f}".format(books.spoilage()),
                        "Total stock size sheet...................{0:.2f}".format(books.total_sss()),
                        "Ream/s for cover.........................{0:.2f}".format(books.ream_for_cover()),
                        "Total number of reams....................{0:.2f}".format(books.number_of_reams()),

                        # MaterialCostBook
                        " ",
                        " ",
                        "Material Cost"
                        ,
                        "===================================================================",
                        "Cost of paper............................{0:.2f}".format(books.paper_cost()),
                        "Cost of plate............................{0:.2f}".format(books.plate_cost()),
                        "Cost of film.............................{0:.2f}".format(books.film_cost()),
                        "Cost of separation.......................{0:.2f}".format(books.separation_cost()),
                        "Cost of material.........................{0:.2f}".format(books.material_cost()),
                        "Over head cost...........................{0:.2f}".format(books.over_head()),
                        "Total material cost......................{0:.2f}".format(books.total_material_cost()),

                        # LabourCostBook
                        " ",
                        " ",
                        "Labour Cost"
                        ,
                        "===================================================================",
                        "Number of impression.....................{0:.2f}".format(books.num_impression()),
                        "Cost of impression.......................{0:.2f}".format(books.cost_of_impression()),
                        "Cost of finishing........................{0:.2f}".format(books.cost_of_finishing()),
                        "Cost of labour...........................{0:.2f}".format(books.cost_of_labour()),
                        "Subtotal.................................{0:.2f}".format(books.sub_total()),
                        "Profit...................................{0:.2f}".format(books.profit()),

                        " ",
                        " ",
                        "Grand Total",
                        "===================================================================",
                        "Grand total..............................{0:.2f}".format(books.grand_total()),

                        " ",
                        " ",
                        "Unit Cost",
                        "===================================================================",
                        "Unit cost................................{0:.2f}".format(books.unit_cost())
                    ]

                    if len(done) == listbox.size():
                        listbox.delete(0, END)
                        for i in done:
                            listbox.insert(END, '           ' + str(i))
                    else:
                        for i in done:
                            listbox.insert(END, '           ' + str(i))
                    listbox.place(relwidth=0.98, relheight=1)

            except ValueError or TypeError:
                msg = ''
                if books.wrong == '':
                    msg = "Please check your values"
                else:
                    msg = books.wrong
                messagebox.showerror("Input Error", msg)

        else:
            messagebox.showerror("Required Fields", "Please include all fields")
            return

    result2 = Button(cal_slide_result, text="Result", bg=nav, command=calculate2)

    def book():
        listbox.delete(0, END)
        global MS_x
        global MS_y
        global FS_x
        global FS_y
        global SS_x
        global SS_y
        global Qty_needed
        global Spoilage_given
        global colour
        global Cost_per_Ream_given
        global Cost_per_Plate_given
        global Cost_per_Separation_given
        global overhead_given
        global num_of_pages_given
        global spine_given
        global change_button_book
        global change_button_paper
        global change_button_period

        change_button_book = True
        change_button_paper = False
        change_button_period = False

        change_colour()

        # Mounting machine size
        fs.grid(row=2, column=0, sticky=E)
        FS_x.grid(row=2, column=1)
        by_fs.grid(row=2, column=2)
        FS_y.grid(row=2, column=3)

        # Mounting machine size
        ms.grid(row=1, column=0, sticky=E)
        MS_x.grid(row=1, column=1)
        by_ms.grid(row=1, column=2)
        MS_y.grid(row=1, column=3)

        # Mounting Stock size
        ss.grid(row=3, column=0, sticky=E)
        SS_x.grid(row=3, column=1)
        by_ss.grid(row=3, column=2)
        SS_y.grid(row=3, column=3)

        # Mounting quantity
        qty.grid(row=4, column=0, sticky=E)
        Qty_needed.grid(row=4, column=1, columnspan=3)

        # Mounting spoilage_g
        spoilage.grid(row=5, column=0, sticky=E)
        Spoilage_given.grid(row=5, column=1, )

        # Mounting number of colours
        cover_colour.grid(row=7, column=0, sticky=E)

        # Mounting number of colours
        page_colour.grid(row=6, column=0, sticky=E)

        # Mounting Number of Pages
        num_of_pages.grid(row=8, column=0, sticky=E)
        num_of_pages_given.grid(row=8, column=1)

        spine.grid(row=9, column=0, sticky=E)
        spine_given.grid(row=9, column=1)

        number_of_period.grid_forget()
        number_of_period_given.grid_forget()

        num_of_periods.grid_forget()
        num_of_periods_given.grid_forget()

        # Mounting Cost per Ream
        cost_per_ream.grid(row=0, column=0, sticky=E)
        Cost_per_Ream_given.grid(row=0, column=1)

        # Mounting Cost per Plate
        cost_per_plate.grid(row=1, column=0, sticky=E)
        Cost_per_Plate_given.grid(row=1, column=1)

        # Mounting Cost per Separation
        cost_per_separation.grid(row=2, column=0, sticky=E)
        Cost_per_Separation_given.grid(row=2, column=1)

        # Mounting Overhead
        overhead.grid(row=3, column=0, sticky=E)
        overhead_given.grid(row=3, column=1)

        # Mounting Cost per Film
        cost_per_film.grid(row=5, column=0, sticky=E)
        cost_per_film_given.grid(row=5, column=1)

        # Mounting partColour
        part_colour.grid(row=7, column=0, sticky=E)
        part_colour_given.grid(row=7, column=1)

        # Mounting Profit
        profit.grid(row=0, column=0, sticky=E)
        profit_given.grid(row=0, column=1)

        # Mounting Cost of finishing
        cost_of_finishing.grid(row=1, column=0)
        cost_of_finishing_given.grid(row=1, column=1)

        # Mounting Cost of impression
        cost_of_impression.grid(row=2, column=0)
        cost_of_impression_given.grid(row=2, column=1)

        # Demounting cover
        cover_1.grid(row=7, column=1)
        cover_4.grid(row=7, column=2)

        # Mounting Parameter
        parameters.grid(row=1, column=0, )

        # Mounting Material
        material.grid(row=2, column=0, )

        # Mounting Material
        labour.grid(row=3, column=0, )

        result.place_forget()
        result3.place_forget()
        result2.place(relheight=1, relwidth=1, )

    def calculate3():
        if MS_x.get() != "" and MS_y.get() != "" and FS_x.get() != "" and SS_x.get() != "" and SS_y.get() != "" and \
                Qty_needed.get() != "" and Spoilage_given.get() != "" and Cost_per_Ream_given.get() != "" and \
                Cost_per_Plate_given.get() != "" and Cost_per_Separation_given.get() != "" and overhead_given.get() != \
                "" and profit_given.get() != "" and cost_of_impression_given.get() != "" and \
                number_of_period_given.get() != "" and num_of_periods_given.get() != "":
            try:
                ms_x = float(MS_x.get())
                ms_y = float(MS_y.get())
                fs_x = float(FS_x.get())
                fs_y = float(FS_y.get())
                ss_x = float(SS_x.get())
                ss_y = float(SS_y.get())
                qty_needed = float(Qty_needed.get())
                spoilage_gi = float(Spoilage_given.get())
                color = float(colour.get())
                c_per_r = float(Cost_per_Ream_given.get())
                c_per_p = float(Cost_per_Plate_given.get())
                c_per_s = float(Cost_per_Separation_given.get())
                c_per_fin = float(cost_of_finishing_given.get())
                c_per_imp = float(cost_of_impression_given.get())
                over_h = float(overhead_given.get())
                profit_g = float(profit_given.get())
                period_g = float(number_of_period_given.get())
                period_gs = float(num_of_periods_given.get())

                calender.set_values_period(ms_x, ms_y, fs_x, fs_y, qty_needed, ss_x, ss_y, spoilage_gi, period_g,
                                           period_gs)
                calender.set_values_period_m(over_h, c_per_r, c_per_p, color, c_per_s)
                calender.set_values_period_l(profit_g, c_per_fin, c_per_imp)

                # ParamsPeriod
                done = [

                    # ParamsPaper
                    " ",
                    "Paper Parameter"
                    ,
                    "===================================================================",
                    "Number of panel/s..........................{0:.2f}".format(calender.panels_to_view()),
                    "Number of period to view..................." + str(calender.number_of_periods_to_view()),
                    "Number of out.............................." + str(calender.number_of_out()),
                    "Working Size  Sheet........................{0:.2f}".format(calender.total_number_of_wss()),
                    "Stock Size Sheet...........................{0:.2f}".format(calender.number_of_sss()),
                    "Spoilage...................................{0:.2f}".format(calender.spoilage()),
                    "Total stock size sheet.....................{0:.2f}".format(calender.total_number_of_sss()),
                    "Number of reams............................{0:.2f}".format(calender.number_of_reams()),

                    # MaterialCostBook
                    " ",
                    " ",
                    "Material Cost",
                    "===================================================================",
                    "Cost of paper..............................{0:.2f}".format(calender.paper_cost()),
                    "Cost of plate..............................{0:.2f}".format(calender.plate_cost()),
                    "Cost of Separation.........................{0:.2f}".format(calender.separation_cost()),
                    "Cost of material...........................{0:.2f}".format(calender.material_cost()),
                    "Overhead cost..............................{0:.2f}".format(calender.over_head()),
                    "Total material cost........................{0:.2f}".format(calender.total_material_cost()),

                    # LabourCostBook
                    " ",
                    " ",
                    "Labour Cost",
                    "===================================================================",
                    "Number of impression.......................{0:.2f}".format(calender.num_impression()),
                    "Cost of impression.........................{0:.2f}".format(calender.cost_of_impression()),
                    "Cost of finishing..........................{0:.2f}".format(calender.cost_of_finishing()),
                    "Cost of labour.............................{0:.2f}".format(calender.cost_of_labour()),
                    "SubTotal...................................{0:.2f}".format(calender.sub_total()),
                    "Profit.....................................{0:.2f}".format(calender.profit_cost()),

                    " ",
                    " ",
                    "Grand Total",
                    "===================================================================",
                    "Grand total................................{0:.2f}".format(calender.grand_total()),

                    " ",
                    " ",
                    "Unit Cost",
                    "===================================================================",
                    "Unit cost..................................{0:.2f}".format(calender.unit_cost()),
                ]

                if len(done) == listbox.size():
                    listbox.delete(0, END)
                    for i in done:
                        listbox.insert(END, '           ' + str(i))
                else:
                    for i in done:
                        listbox.insert(END, '           ' + str(i))
                listbox.place(relwidth=0.98, relheight=1)

            except ValueError or TypeError:
                msg = ''
                if calender.wrong == '':
                    msg = "Please check your values"
                else:
                    msg = calender.wrong
                messagebox.showerror("Input Error", msg)

        else:
            messagebox.showerror("Required Fields", "Please include all fields")
            return

    result3 = Button(cal_slide_result, text="Result", bg=nav, command=calculate3)

    def period():
        listbox.delete(0, END)
        global MS_x
        global MS_y
        global FS_x
        global FS_y
        global SS_x
        global SS_y
        global Qty_needed
        global Spoilage_given
        global colour
        global Cost_per_Ream_given
        global Cost_per_Plate_given
        global Cost_per_Separation_given
        global overhead_given
        global num_of_pages_given
        global spine_given
        global change_button_book
        global change_button_paper
        global change_button_period

        change_button_book = False
        change_button_paper = False
        change_button_period = True

        change_colour()

        # Mounting machine size
        fs.grid(row=2, column=0, sticky=E)
        FS_x.grid(row=2, column=1)
        by_fs.grid(row=2, column=2)
        FS_y.grid(row=2, column=3)

        # Mounting machine size
        ms.grid(row=1, column=0, sticky=E)
        MS_x.grid(row=1, column=1)
        by_ms.grid(row=1, column=2)
        MS_y.grid(row=1, column=3)

        # Mounting Stock size
        ss.grid(row=3, column=0, sticky=E)
        SS_x.grid(row=3, column=1)
        by_ss.grid(row=3, column=2)
        SS_y.grid(row=3, column=3)

        # Mounting quantity
        qty.grid(row=4, column=0, sticky=E)
        Qty_needed.grid(row=4, column=1, columnspan=3)

        # Mounting spoilage_g
        spoilage.grid(row=5, column=0, sticky=E)
        Spoilage_given.grid(row=5, column=1, )

        # Mounting number of colours
        cover_colour.grid_forget()

        # Mounting number of colours
        page_colour.grid(row=6, column=0, sticky=E)

        # Mounting Number of Pages
        num_of_pages.grid_forget()
        num_of_pages_given.grid_forget()

        spine.grid_forget()
        spine_given.grid_forget()

        number_of_period.grid(row=9, column=0, sticky=E)
        number_of_period_given.grid(row=9, column=1)

        # Mounting Cost per Ream
        cost_per_ream.grid(row=0, column=0, sticky=E)
        Cost_per_Ream_given.grid(row=0, column=1)

        # Mounting Cost per Plate
        cost_per_plate.grid(row=1, column=0, sticky=E)
        Cost_per_Plate_given.grid(row=1, column=1)

        # Mounting Cost per Separation
        cost_per_separation.grid(row=2, column=0, sticky=E)
        Cost_per_Separation_given.grid(row=2, column=1)

        # Mounting Overhead
        overhead.grid(row=3, column=0, sticky=E)
        overhead_given.grid(row=3, column=1)

        # Mounting Cost per Film
        cost_per_film.grid_forget()
        cost_per_film_given.grid_forget()

        # Mounting partColour
        part_colour.grid_forget()
        part_colour_given.grid_forget()

        # Mounting Profit
        profit.grid(row=0, column=0, sticky=E)
        profit_given.grid(row=0, column=1)

        # Mounting Cost of finishing
        cost_of_finishing.grid(row=1, column=0)
        cost_of_finishing_given.grid(row=1, column=1)

        # Mounting Cost of impression
        cost_of_impression.grid(row=2, column=0)
        cost_of_impression_given.grid(row=2, column=1)

        # Demounting cover
        cover_1.grid_forget()
        cover_4.grid_forget()

        # Mounting Parameter
        parameters.grid(row=1, column=0, )

        # Mounting Material
        material.grid(row=2, column=0)

        # Mounting Material
        labour.grid(row=3, column=0, )

        # Mounting Number of Pages
        num_of_periods.grid(row=8, column=0, sticky=E)
        num_of_periods_given.grid(row=8, column=1)

        result.place_forget()
        result2.place_forget()
        result3.place(relheight=1, relwidth=1)

    button_paper = Button(nav_button, text="Paper Work", command=paper, bg=nav_paper)
    button_book = Button(nav_button, text="Book Work", command=book, bg=nav_book)
    button_period = Button(nav_button, text="Periodic Work", command=period, bg=nav_period)
    button_paper.place(relwidth=0.3333, relheight=1, )
    button_book.place(relx=0.333, relwidth=0.3333, relheight=1)
    button_period.place(relx=0.667, relwidth=0.333, relheight=1)

    def change_colour():
        global button_paper
        global button_book
        global button_period
        global change_button_paper
        global change_button_book
        global change_button_period

        if change_button_paper:
            button_paper = Button(nav_button, text="Paper Work", relief=SUNKEN, command=paper, bg=bg)
            button_paper.place(relwidth=0.333, relheight=1, )
            button_book = Button(nav_button, text="Book Work", command=book, bg=nav_book)
            button_book.place(relx=0.333, relwidth=0.333, relheight=1)
            button_period = Button(nav_button, text="Periodic Work", command=period, bg=nav_period)
            button_period.place(relx=0.667, relwidth=0.333, relheight=1)

        if change_button_book:
            button_paper = Button(nav_button, text="Paper Work", command=paper, bg=nav_paper)
            button_paper.place(relwidth=0.333, relheight=1, )
            button_book = Button(nav_button, text="Book Work", relief=SUNKEN, command=book, bg=bg)
            button_book.place(relx=0.333, relwidth=0.333, relheight=1)
            button_period = Button(nav_button, text="Periodic Work", command=period, bg=nav_period)
            button_period.place(relx=0.667, relwidth=0.333, relheight=1)

        if change_button_period:
            button_period = Button(nav_button, text="Periodic Work", relief=SUNKEN, command=period, bg=bg)
            button_period.place(relx=0.667, relwidth=0.333, relheight=1)
            button_paper = Button(nav_button, text="Paper Work", command=paper, bg=nav_paper)
            button_paper.place(relwidth=0.333, relheight=1, )
            button_book = Button(nav_button, text="Book Work", command=book, bg=nav_book)
            button_book.place(relx=0.333, relwidth=0.333, relheight=1)


welcome_button = Button(root, text="Welcome", command=work_place)
welcome_button.place(relx=0.5, rely=0.5)

root.mainloop()
