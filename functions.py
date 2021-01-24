import tkinter as tk


def show_frame(self, page_name):
    # Show a frame for the given page name
    frame = self.frames[page_name]
    frame.tkraise()


def disable_button(disabled_button_list, var, new_button_var):
    for el in disabled_button_list:
        el.config(state=tk.DISABLED if var.get() == 0 else tk.NORMAL)
    new_button_var.set(1)  # default option for revealed button


def frame_visual(self):
    font_style = "Italic"
    font_size = 8

    # labels collum window
    labels_window = tk.Frame(self)
    labels_window.place(relx=0.16, rely=0.03, relwidth=0.3, relheight=0.94, anchor="n")

    label1 = tk.Label(labels_window, text="Metabolism", font=(font_style, font_size))
    label2 = tk.Label(labels_window, text="External work", font=(font_style, font_size))
    label3 = tk.Label(labels_window, text="Air temperature", font=(font_style, font_size))
    label4 = tk.Label(labels_window, text="Relative Humidity", font=(font_style, font_size))
    label5 = tk.Label(labels_window, text="Radiation", font=(font_style, font_size))
    label6 = tk.Label(labels_window, text="Effective wind speed", font=(font_style, font_size))
    label7 = tk.Label(labels_window, text="Heat transfer coefficient underclothing", font=(font_style, font_size))
    label8 = tk.Label(labels_window, text="Air gap between under and outer clothing", font=(font_style, font_size))
    label9 = tk.Label(labels_window, text="Heat transfer coefficient outer clothing", font=(font_style, font_size))
    label10 = tk.Label(labels_window, text="Water vapour resistance outer clothing", font=(font_style, font_size))
    label11 = tk.Label(labels_window, text="Regain outer clothing", font=(font_style, font_size))
    label12 = tk.Label(labels_window, text="Regain underclothing", font=(font_style, font_size))
    label13 = tk.Label(labels_window, text="Ventilation through clothing", font=(font_style, font_size))
    label14 = tk.Label(labels_window, text="Fraction of area uncovered (nude)", font=(font_style, font_size))
    label15 = tk.Label(labels_window, text="Factor of area increase by clothing", font=(font_style, font_size))
    label16 = tk.Label(labels_window, text="Fraction of area irradiated", font=(font_style, font_size))
    label17 = tk.Label(labels_window, text="Reflection coefficient outer clothing UV", font=(font_style, font_size))
    label18 = tk.Label(labels_window, text="Transmission coefficient outer clothing UV", font=(font_style, font_size))
    label19 = tk.Label(labels_window, text="Reflection coefficient underclothing UV", font=(font_style, font_size))
    label20 = tk.Label(labels_window, text="Transmission coefficient underclothing UV", font=(font_style, font_size))
    label21 = tk.Label(labels_window, text="Transmission coefficient outer clothing IR", font=(font_style, font_size))
    label22 = tk.Label(labels_window, text="Reflection coefficient underclothing IR", font=(font_style, font_size))
    label23 = tk.Label(labels_window, text="Time interval", font=(font_style, font_size))
    label24 = tk.Label(labels_window, text="Weight", font=(font_style, font_size))
    label25 = tk.Label(labels_window, text="Height", font=(font_style, font_size))
    label26 = tk.Label(labels_window, text="Fat %", font=(font_style, font_size))
    label27 = tk.Label(labels_window, text="Training status", font=(font_style, font_size))
    label28 = tk.Label(labels_window, text="Acclimation status", font=(font_style, font_size))

    labels_list = [label1, label2, label3, label4, label5, label6, label7, label8, label9, label9, label10, label11,
                   label12, label13, label14, label15, label16, label17, label18, label19, label20, label21, label22,
                   label23, label24, label25, label26, label27, label28]
    for label in labels_list:
        label.pack(side="top", expand=True, anchor="w")

    # "from" collum window
    from_label = tk.Label(self, text="from", font=(font_style, font_size))
    from_label.place(relx=0.35, rely=0.01, relwidth=0.08, relheight=0.015, anchor="n")
    from_window = tk.Frame(self)
    from_window.place(relx=0.37, rely=0.03, relwidth=0.08, relheight=0.94, anchor="n")

    from_list = ["from_entry1", "from_entry2", "from_entry3", "from_entry4", "from_entry5", "from_entry6",
                 "from_entry7", "from_entry8", "from_entry9", "from_entry10", "from_entry11", "from_entry12",
                 "from_entry13", "from_entry14", "from_entry15", "from_entry16", "from_entry17", "from_entry18",
                 "from_entry19", "from_entry20", "from_entry21", "from_entry22", "from_entry23", "from_entry24",
                 "from_entry25", "from_entry26", "from_entry27", "from_entry28"]
    for i in range(0, len(from_list)):
        from_list[i] = tk.Entry(from_window, font=(font_style, font_size))
    for el in from_list:
        el.pack(side="top", expand=True, anchor="w")

    # "to" collum window
    to_label = tk.Label(self, text="to", font=(font_style, font_size))
    to_label.place(relx=0.47, rely=0.01, relwidth=0.08, relheight=0.015, anchor="n")
    to_window = tk.Frame(self)
    to_window.place(relx=0.49, rely=0.03, relwidth=0.08, relheight=0.94, anchor="n")

    to_list = ["to_entry1", "to_entry2", "to_entry3", "to_entry4", "to_entry5", "to_entry6", "to_entry7", "to_entry8",
               "to_entry9", "to_entry10", "to_entry11", "to_entry12", "to_entry13", "to_entry14", "to_entry15",
               "to_entry16", "to_entry17", "to_entry18", "to_entry19", "to_entry20", "to_entry21", "to_entry22",
               "to_entry23", "to_entry24", "to_entry25", "to_entry26", "to_entry27", "to_entry28"]
    for i in range(0, len(to_list)):
        if to_list[i] == "to_entry23":
            to_list[i] = tk.Label(to_window, font=(font_style, font_size))
        else:
            to_list[i] = tk.Entry(to_window, font=(font_style, font_size))
    for el in to_list:
        el.pack(side="top", expand=True, anchor="w")

    # "step" collum window
    step_label = tk.Label(self, text="step", font=(font_style, font_size))
    step_label.place(relx=0.59, rely=0.009, relwidth=0.08, relheight=0.02, anchor="n")
    step_window = tk.Frame(self)
    step_window.place(relx=0.61, rely=0.03, relwidth=0.08, relheight=0.94, anchor="n")

    step_list = ["step_entry1", "step_entry2", "step_entry3", "step_entry4", "step_entry5", "step_entry6",
                 "step_entry7", "step_entry8", "step_entry9", "step_entry10", "step_entry11", "step_entry12",
                 "step_entry13", "step_entry14", "step_entry15", "step_entry16", "step_entry17", "step_entry18",
                 "step_entry19", "step_entry20", "step_entry21", "step_entry22", "step_entry23", "step_entry24",
                 "step_entry25", "step_entry26", "step_entry27", "step_entry28"]
    for i in range(0, len(step_list)):
        if step_list[i] == "step_entry23":
            step_list[i] = tk.Label(step_window, font=(font_style, font_size))
        else:
            step_list[i] = tk.Entry(step_window, font=(font_style, font_size))
    for el in step_list:
        el.pack(side="top", expand=True, anchor="w")

    # Simulation time window
    simulation_time_window = tk.Frame(self)
    simulation_time_window.config(highlightbackground="grey", highlightthickness=1)
    simulation_time_window.place(relx=0.83, rely=0.03, relwidth=0.26, relheight=0.12, anchor="n")

    simulation_time_label = tk.Label(simulation_time_window, text="Simulation Time", font=(font_style, 9, "bold"))
    simulation_time_from_label = tk.Label(simulation_time_window, text="from", font=(font_style, font_size))
    simulation_time_to_label = tk.Label(simulation_time_window, text="to", font=(font_style, font_size))
    simulation_time_step_label = tk.Label(simulation_time_window, text="step", font=(font_style, font_size))
    simulation_time_from_entry = tk.Entry(simulation_time_window)
    simulation_time_to_entry = tk.Entry(simulation_time_window)
    simulation_time_step_entry = tk.Entry(simulation_time_window)

    simulation_time_label.pack(side="top", expand=True, anchor="n")
    simulation_time_from_label.place(relx=0.15, rely=0.35, relwidth=0.2, relheight=0.2, anchor="n")
    simulation_time_to_label.place(relx=0.5, rely=0.35, relwidth=0.2, relheight=0.2, anchor="n")
    simulation_time_step_label.place(relx=0.85, rely=0.35, relwidth=0.2, relheight=0.2, anchor="n")
    simulation_time_from_entry.place(relx=0.15, rely=0.65, relwidth=0.2, relheight=0.2, anchor="n")
    simulation_time_to_entry.place(relx=0.5, rely=0.65, relwidth=0.2, relheight=0.2, anchor="n")
    simulation_time_step_entry.place(relx=0.85, rely=0.65, relwidth=0.2, relheight=0.2, anchor="n")

    # Export options window
    export_window = tk.Frame(self)
    export_window.config(highlightbackground="grey", highlightthickness=1)
    export_window.place(relx=0.83, rely=0.18, relwidth=0.26, relheight=0.24, anchor="n")
    export_label = tk.Label(export_window, text="Export options", font=("Italic", 9, "bold"))
    export_label.pack(side="top", expand=True, anchor="n")
    option_menu_list = ["Metabolisme", "Lichaamstemp.", "Rectaaltemp.", "Huidtemp.", "Warmteopslag", "Zweetprod.",
                        "Huidacc.", "Onderkl. acc.", "Kledingacc.", "Huidverdamping", "Luchtverdamping",
                        "Onderkl. temp.", "Kledingtemp.", "huidtemp bedekt dl."]
    temperature_var = tk.StringVar()
    temperature_var.set(option_menu_list[4])  # default one
    temp_var = tk.IntVar()
    threshold_var = tk.IntVar()
    temperature_menu = tk.OptionMenu(export_window, temperature_var, *option_menu_list)
    temperature_menu.place(relx=0.5, rely=0.15, relwidth=0.8, relheight=0.13, anchor="n")

    high_temp_radio = tk.Radiobutton(export_window, variable=temp_var, value=1, text="High temperature")
    low_temp_radio = tk.Radiobutton(export_window, variable=temp_var, value=2, text="Low temperature")
    temp_entry = tk.Entry(export_window)
    temp_entry.insert(0, 38.5)
    disabled_buttons_list = [high_temp_radio, low_temp_radio, temp_entry]
    threshold_checkbutton = tk.Checkbutton(export_window, text="Test on threshold:", variable=threshold_var,
                                           command=lambda: disable_button(disabled_buttons_list, threshold_var,
                                                                          temp_var))
    high_temp_radio.config(state=tk.DISABLED if threshold_var.get() == 0 else tk.NORMAL)
    low_temp_radio.config(state=tk.DISABLED if threshold_var.get() == 0 else tk.NORMAL)
    temp_entry.config(state=tk.DISABLED if threshold_var.get() == 0 else tk.NORMAL)
    high_temp_radio.place(relx=0.5, rely=0.55, relwidth=0.8, relheight=0.13, anchor="n")
    low_temp_radio.place(relx=0.5, rely=0.65, relwidth=0.8, relheight=0.13, anchor="n")
    temp_entry.place(relx=0.5, rely=0.8, relwidth=0.4, relheight=0.12, anchor="n")
    threshold_checkbutton.place(relx=0.5, rely=0.4, relwidth=0.8, relheight=0.13, anchor="n")

    # Simulate button
    simulate_button = tk.Button(self, text="Simulate", font=(font_style, font_size))
    simulate_button.place(relx=0.83, rely=0.62, relwidth=0.15, relheight=0.03, anchor="n")

    # Cool picture?
    # Set defaults / Clear memory buttons
    def set_defaults():
        default_list = ["", "", "", "", "", "", "", "", "", "", "", "", 25, 0.2, 1.1, 0.25, 0.1, 0.1, 0.1, 0.1, 0.1,
                        0.1, 1, 83, 1.85, 15, 50, 50]
        for index in range(0, len(default_list)):
            if index == 22:
                from_list[index].delete(0, tk.END)
                from_list[index].insert(0, default_list[index])
            else:
                step_list[index].delete(0, tk.END)
                from_list[index].delete(0, tk.END)
                to_list[index].delete(0, tk.END)
                from_list[index].insert(0, default_list[index])
                to_list[index].insert(0, default_list[index])
        simulation_time_from_entry.delete(0, tk.END)
        simulation_time_to_entry.delete(0, tk.END)
        simulation_time_step_entry.delete(0, tk.END)
        temp_entry.delete(0, tk.END)
        temp_entry.insert(0, 38.5)

    set_defaults_button = tk.Button(self, text="Set defaults", font=(font_style, font_size),
                                    command=lambda: set_defaults())
    set_defaults_button.place(relx=0.77, rely=0.92, relwidth=0.12, relheight=0.03, anchor="n")
    clear_memory_button = tk.Button(self, text="Clear memory", font=(font_style, font_size))
    clear_memory_button.place(relx=0.9, rely=0.92, relwidth=0.12, relheight=0.03, anchor="n")

    return_list = []
    from_list.append(simulation_time_from_entry)
    to_list.append(simulation_time_to_entry)
    step_list.append(simulation_time_step_entry)
    for el in from_list:
        return_list.append(el.get())
    for el in to_list:
        try:
            return_list.append(el.get())
        except AttributeError:
            return_list.append("")
    for el in step_list:
        try:
            return_list.append(el.get())
        except AttributeError:
            return_list.append("")
    print(len(return_list))
    print(return_list)
    return return_list
