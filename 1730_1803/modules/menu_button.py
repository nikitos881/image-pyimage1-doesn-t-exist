import customtkinter as ctk
import modules.screen_app as s_app
from random import randint
import modules.find_path as m_path
import modules.create_json as m_json
from PIL import Image

width_input = 250
height_input = 60
rand_pic = randint(1, 2)
img_width = 230
img_height = 230

text1 = ctk.StringVar()
text2 = ctk.StringVar()
text3 = ctk.StringVar()

reg_dict1 = {}
reg_dict2 = {}
reg_dict3 = {}

reg_dict_1 = {}
reg_dict_2 = {}
reg_dict_3 = {}

font_size = ctk.CTkFont(
    family= "Arial",
    size= 20,
    weight= "bold"
)

def create_button(master, text, command, width= 100, height= 50, border_width= 2, corner_radius= 5 ,border_color= "black", fg_color= "green"):
    button = ctk.CTkButton(master= master,
                           width= width,
                           height= height,
                           border_width= border_width,
                           corner_radius= corner_radius,
                           border_color= border_color,
                           text= text,
                           fg_color= fg_color,
                           command= command
    )
    return button

def create_button_for_text(master, text, width= 100, height= 30, border_width= 2, corner_radius= 5 ,border_color= "black", fg_color= "black"):
    button_for_text = ctk.CTkButton(master= master,
                           width= width,
                           height= height,
                           border_width= border_width,
                           corner_radius= corner_radius,
                           border_color= border_color,
                           text= text,
                           fg_color= fg_color,
                           hover = False
    )
    return button_for_text

def create_button_registration(master, text, command, width= 100, height= 50, border_width= 2, corner_radius= 5 ,border_color= "grey", fg_color= "grey"):
    button_for_registration = ctk.CTkButton(master= master,
                           width= width,
                           height= height,
                           border_width= border_width,
                           corner_radius= corner_radius,
                           border_color= border_color,
                           text= text,
                           fg_color= fg_color,
                           command= command
    )
    return button_for_registration

def login():
    login_app = s_app.App(500, 500)
    login_app.title("Вхід")

    input_login = ctk.CTkEntry(
    master= login_app,
    width= width_input,
    height= height_input,
    fg_color= "white",
    text_color= "black",
    font= font_size,
    textvariable= text1
    ) 

    input_login_password = ctk.CTkEntry(
    master= login_app,
    width= width_input,
    height= height_input,
    fg_color= "white",
    text_color= "black",
    font= font_size,
    textvariable= text2
    ) 
    

    input_login.place(
        x= 250,
        y= 70,
        anchor= ctk.CENTER
    )
    input_login_password.place(
        x= 250,
        y= 200,
        anchor= ctk.CENTER
    )

    login_text = create_button_for_text(master= login_app, text= "Логін: ")
    login_text.place(x= 250, y= 17, anchor= ctk.CENTER)

    password_text = create_button_for_text(master= login_app, text= "Пароль: ")
    password_text.place(x= 250, y= 147, anchor= ctk.CENTER)

    login_button = create_button_registration(master = login_app, text= "Увійти",command = login_button)
    login_button.place(x= 250, y= 400, anchor= ctk.CENTER)

    def login_button():
        app= s_app.App(500, 500)
        app.title("Додаток з отримання картинок")

    login_app.mainloop()

def register():
    register_app = s_app.App(500, 500)
    register_app.title("Регестрація")
       
    input_register_email = ctk.CTkEntry(
    master= register_app,
    width= width_input,
    height= height_input,
    fg_color= "white",
    text_color= "black",
    font= font_size,
    textvariable= text1
    ) 

    input_register_password = ctk.CTkEntry(
    master= register_app,
    width= width_input,
    height= height_input,
    fg_color= "white",
    text_color= "black",
    font= font_size,
    textvariable= text2
    ) 
    
    input_register_accept = ctk.CTkEntry(
    master= register_app,
    width= width_input,
    height= height_input,
    fg_color= "white",
    text_color= "black",
    font= font_size,
    textvariable= text3
    ) 
    
    input_register_email.place(
        x= 250,
        y= 70,
        anchor= ctk.CENTER
    )
    input_register_password.place(
        x= 250,
        y= 200,
        anchor= ctk.CENTER
    )
    input_register_accept.place(
        x= 250,
        y= 330,
        anchor= ctk.CENTER
    )

    email_text = create_button_for_text(master= register_app, text= "Пошта: ")
    email_text.place(x= 250, y= 17, anchor= ctk.CENTER)

    password_text = create_button_for_text(master= register_app, text= "Пароль: ")
    password_text.place(x= 250, y= 147, anchor= ctk.CENTER)

    password_accept_text = create_button_for_text(master= register_app, text= "Підтвердження паролю: ")
    password_accept_text.place(x= 250, y= 277, anchor= ctk.CENTER)

    def registration_button():
        global reg_dict1
        reg_dict1 = {"mail" : input_register_email.get(),
                     "password" : input_register_password.get(),
                     "accept" : input_register_accept.get()}
        m_json.create_json(reg_dict1)
        m_json.read_json(reg_dict_1)
        #print(reg_dict1)
        app= s_app.App(500, 500)
        app.title("Додаток з отримання картинок")

        def image_message():
            # global random_picture
            # if random_picture == 1:
            #     image_message1 = ctk.CTkImage(
            #         light_image= Image.open(m_path.find_path("images/image1.png")),
            #         size= (img_width, img_height)
            #     )
            #     image_label1 = ctk.CTkLabel(master= app, text= "", image= image_message1)
            #     image_label1.place(relx= 0.5, rely= 0.3, anchor= ctk.CENTER)
            #     random_picture= (1,2)

            # elif random_picture == 2:
            #     image_message2 = ctk.CTkImage(
            #         light_image= Image.open(m_path.find_path("images/image2.png")),
            #         size= (img_width, img_height)
            #     )
            #     image_label2 = ctk.CTkLabel(master= app, text= "", image= image_message2)
            #     image_label2.place(relx= 0.5, rely= 0.3, anchor= ctk.CENTER)
            #     random_picture= (1,2)
            global rand_pic
            if rand_pic == 1:
                image_message1 = ctk.CTkImage(
                   dark_image= Image.open(m_path.find_path("images/image1.png")), 
                  size= (img_width, img_height)
                )       

                image_lable1 = ctk.CTkLabel(master= app, text= "", image= image_message1)
                image_lable1.place(relx = 0.50, rely = 0.30, anchor = ctk.CENTER)
                rand_pic = randint(1,3)
            elif rand_pic == 2:
                image_message2 = ctk.CTkImage(
                    dark_image= Image.open(m_path.find_path("images/image2.png")), 
                    size= (img_width, img_height)
                )       

                image_lable2 = ctk.CTkLabel(master= app, text= "", image= image_message2)
                image_lable2.place(relx = 0.50, rely = 0.30, anchor = ctk.CENTER)
                rand_pic = randint(1,3)
        

        get_picture_button = create_button_registration(master= app, text= "Получити зображення", command= image_message)
        get_picture_button.place(x= 250, y= 400, anchor= ctk.CENTER)

        app.mainloop()

    registration_button = create_button_registration(master= register_app, text= "Зареєструватися", command= registration_button)
    registration_button.place(x= 250, y= 400, anchor= ctk.CENTER)

    register_app.mainloop()

bt_login = create_button(master= s_app.start_app, text= "Login", command= login)
bt_register = create_button(master= s_app.start_app, text= "Register", command= register)

bt_register.place(relx= 0.45, rely= 0.5, anchor= ctk.CENTER)
bt_login.place(relx= 0.45, rely= 0.3, anchor= ctk.CENTER)




# input_register= ctk.CTkEntry(
#     master= s_app.start_app,
#     width= 100,
#     height= 50,
#     fg_color= "orange",
#     text_color = "black",
#     border_color ="black",
#     font= 10,
#     textvariable= text
    
# )
 
# text_input = ctk.CTkEntry(
#     master= m_app.main_app.FRAME3,
#     width= width_input,
#     height= height_input,
#     fg_color= "white",
#     text_color= "black",
#     font= font_size,
#     textvariable= text



