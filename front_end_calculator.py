import tkinter as tk
import functions as fun


class DataWindow(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry("680x610")
        self.title("DataWindow")
        self.resizable(False, False)

        # the container is where we stack frames on top of each other. Wanted page will raise above the others.
        container = tk.Frame(self)
        container.place(relwidth=1, relheight=1)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Phase1, Phase2, Phase3):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location on top of each other. Top one is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        # menubar on all frames
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0, font=("italic", 9))
        file_menu.add_command(label="New")
        file_menu.add_separator()
        file_menu.add_command(label="Open Simulation")
        file_menu.add_command(label="Save Simulation")
        file_menu.add_separator()
        file_menu.add_command(label="Export Data")
        menubar.add_cascade(label="File", menu=file_menu)

        parameters_menu = tk.Menu(menubar, tearoff=0, font=("italic", 9))
        parameters_menu.add_command(label="Copy parameters to phase 1")
        parameters_menu.add_command(label="Copy parameters to phase 2")
        parameters_menu.add_command(label="Copy parameters to phase 3")
        menubar.add_cascade(label="Copy parameters", menu=parameters_menu)

        window_menu = tk.Menu(menubar, tearoff=0, font=("italic", 9))
        window_menu.add_command(label="Graph    Ctrl+G")
        menubar.add_cascade(label="Window", menu=window_menu)

        fun.show_frame(self, "Phase1")


class Phase1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        fun.frame_visual(self)

        # Phase window
        phase_window = tk.Frame(self)
        phase_window.config(highlightbackground="grey", highlightthickness=1)
        phase_window.place(relx=0.83, rely=0.45, relwidth=0.26, relheight=0.15, anchor="n")
        phase_label = tk.Label(phase_window, text="Phase", font=("Italic", 9, "bold"))
        phase_label.pack(side="top", expand=True, anchor="n")
        numeration_label = tk.Label(phase_window, text="1", font=("Italic", 28, "bold"), fg="purple")
        back_button = tk.Button(phase_window, text="<< back", font=("Italic", 10, "bold"))
        next_button = tk.Button(phase_window, text="next >>", font=("Italic", 10, "bold"),
                                command=lambda: fun.show_frame(controller, "Phase2"))
        numeration_label.place(relx=0.5, rely=0.2, relwidth=0.9, relheight=0.5, anchor="n")
        back_button.place(relx=0.25, rely=0.75, relwidth=0.43, relheight=0.22, anchor="n")
        next_button.place(relx=0.75, rely=0.75, relwidth=0.43, relheight=0.22, anchor="n")
        # print(fun.from_entry20.get())


class Phase2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        fun.frame_visual(self)

        # Phase window
        phase_window = tk.Frame(self)
        phase_window.config(highlightbackground="grey", highlightthickness=1)
        phase_window.place(relx=0.83, rely=0.45, relwidth=0.26, relheight=0.15, anchor="n")
        phase_label = tk.Label(phase_window, text="Phase", font=("Italic", 9, "bold"))
        phase_label.pack(side="top", expand=True, anchor="n")
        numeration_label = tk.Label(phase_window, text="2", font=("Italic", 28, "bold"), fg="purple")
        back_button = tk.Button(phase_window, text="<< back", font=("Italic", 10, "bold"),
                                command=lambda: fun.show_frame(controller, "Phase1"))
        next_button = tk.Button(phase_window, text="next >>", font=("Italic", 10, "bold"),
                                command=lambda: fun.show_frame(controller, "Phase3"))
        numeration_label.place(relx=0.5, rely=0.2, relwidth=0.9, relheight=0.5, anchor="n")
        back_button.place(relx=0.25, rely=0.75, relwidth=0.43, relheight=0.22, anchor="n")
        next_button.place(relx=0.75, rely=0.75, relwidth=0.43, relheight=0.22, anchor="n")


class Phase3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        fun.frame_visual(self)

        # Phase window
        phase_window = tk.Frame(self)
        phase_window.config(highlightbackground="grey", highlightthickness=1)
        phase_window.place(relx=0.83, rely=0.45, relwidth=0.26, relheight=0.15, anchor="n")
        phase_label = tk.Label(phase_window, text="Phase", font=("Italic", 9, "bold"))
        phase_label.pack(side="top", expand=True, anchor="n")
        numeration_label = tk.Label(phase_window, text="3", font=("Italic", 28, "bold"), fg="purple")
        back_button = tk.Button(phase_window, text="<< back", font=("Italic", 10, "bold"),
                                command=lambda: fun.show_frame(controller, "Phase2"))
        next_button = tk.Button(phase_window, text="next >>", font=("Italic", 10, "bold"))
        numeration_label.place(relx=0.5, rely=0.2, relwidth=0.9, relheight=0.5, anchor="n")
        back_button.place(relx=0.25, rely=0.75, relwidth=0.43, relheight=0.22, anchor="n")
        next_button.place(relx=0.75, rely=0.75, relwidth=0.43, relheight=0.22, anchor="n")


if __name__ == "__main__":
    app = DataWindow()
    app.mainloop()
