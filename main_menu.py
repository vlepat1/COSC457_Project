
import tkinter as tk
from tkinter import font as tkfont

#Main class that handles the frame changes by stacking frames on top of one another
class frame_change(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family = 'Helvetica', size = 12)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}
        for F in (main_interface, employee_interface, pat_interface, pat_choices):
            page_name = F.__name__
            frame = F(parent = container, controller = self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("main_interface")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

#Main Menu class
class main_interface(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text = "Welcome to Hospital Databse \n Select a which option to search: ", font = controller.title_font)
        label.grid(columnspan = 2, rowspan = 2)

        emp_button = tk.Button(self, text = 'Employee', width = 10, command = lambda: controller.show_frame("employee_interface"))
        emp_button.grid(row = 3, column = 0)
        patient_button = tk.Button(self, text = 'Patient', width = 10, command = lambda: controller.show_frame("pat_interface")) 
        patient_button.grid(row = 3, column = 1)       

#Class shows the employee interface
#Provides buttons to provide info on specific employee's
class employee_interface(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text = "Select a type of employee:  ", font = controller.title_font)
        label.grid(columnspan = 2)

        nurse_button = tk.Button(self, text = 'Nurse', width = 10)
        nurse_button.grid(row = 2, column = 0)
        nurse_button = tk.Button(self, text = 'Doctor', width = 10)
        nurse_button.grid(row = 2, column = 1)
        nurse_button = tk.Button(self, text = 'Receptionist', width = 10)
        nurse_button.grid(row = 3, column = 0)
        nurse_button = tk.Button(self, text = 'Janitor', width = 10)
        nurse_button.grid(row = 3, column = 1)
        nurse_button = tk.Button(self, text = 'Technician', width = 10)
        nurse_button.grid(row = 4, column = 0)
        return_button = tk.Button(self, text = 'Return to Main Menu', width = 10, command = lambda: controller.show_frame("main_interface"))
        return_button.grid(row = 5, columnspan = 2)

#Class shows the patient interface
#Provides a list of patients to click from 
class pat_interface(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text = 'Select a patient:', font = controller.title_font)
        label.grid(columnspan = 2)

        pat1_button = tk.Button(self, text = 'Doe, John', width = 10, command = lambda: controller.show_frame("pat_choices"))
        pat1_button.grid(row = 2, column = 0)
        pat2_button = tk.Button(self, text = 'Long, Jake', width = 10, command = lambda: controller.show_frame("pat_choices"))
        pat2_button.grid(row = 2, column = 1)
        pat3_button = tk.Button(self, text = 'Diez, Joe', width = 10, command = lambda: controller.show_frame("pat_choices"))
        pat3_button.grid(row = 3, column = 0)
        pat4_button = tk.Button(self, text = 'Smith, Jason', width = 10, command = lambda: controller.show_frame("pat_choices"))
        pat4_button.grid(row = 3, column = 1)
        pat5_button = tk.Button(self, text = 'Kazama, Jin', width = 10, command = lambda: controller.show_frame("pat_choices"))
        pat5_button.grid(row = 4, column = 0)
        return_button = tk.Button(self, text = 'Return to Main Menu', width = 10, command = lambda: controller.show_frame("main_interface"))
        return_button.grid(columnspan = 2)

class pat_choices(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text = 'What information do you \n want about this patient:', font = controller.title_font)
        label.grid(columnspan = 2, rowspan = 2)

        info_button = tk.Button(self, text = 'Patient Info.', width = 10)
        info_button.grid(row = 2, column = 0)
        acc_button = tk.Button(self, text = 'Account Info.', width = 10)
        acc_button.grid(row = 2, column = 1)
        appt_button = tk.Button(self, text = 'Appointments', width = 10)
        appt_button.grid(row = 3, column = 0)
        bill_button = tk.Button(self, text = 'Bill', width = 10)
        bill_button.grid(row = 3, column = 1)
        rec_button = tk.Button(self, text = 'Records', width = 10)
        rec_button.grid(row = 4, column = 0)
        return_button = tk.Button(self, text = 'Return to select Patient', command = lambda: controller.show_frame("pat_interface"))
        return_button.grid(columnspan = 2)

if __name__ == "__main__":
    app = frame_change()
    app.mainloop()