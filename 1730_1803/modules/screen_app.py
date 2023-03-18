import customtkinter as ctk
import modules.button_pressed as b_pressed


# class My_Frame(ctk.CTkFrame):
#     def __init__(self, text, master, width, height, border_width, **kwargs):
#         super().__init__(master= master,
#                          width= width,
#                          height= height,
#                          border_width= border_width,
#                          **kwargs
#         )
#         self.LABEL = ctk.CTkLabel(self, text= text)
#         self.LABEL.place(x= 10, y= 30)

class App(ctk.CTk):
    def __init__(self, app_width, app_height):
        super().__init__()
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        self.SCREEN_WIDTH = self.winfo_screenwidth()
        self.SCREEN_HEIGHT = self.winfo_screenheight()

        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{0}+{0}")
        self.resizable(False, False)
        self.title("Додаток")
        # self.FRAME1 = My_Frame(text= "", master= self, width= 500, height= 500, border_width= 0)

start_app = App(500,500)

#

