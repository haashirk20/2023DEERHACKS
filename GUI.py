from tkinter import *
from control import *
from flashcards import *
from customtkinter import *
from tkinter.font import Font
import urllib.request
from PIL import ImageTk, Image

def mainScreen():

    def game_screen():
        #main game screen

        #transition from start screen to game screen
        main_menu_frame.pack_forget()

        #get wordslist
        extract_info_from_CSV("words.csv")

        def return_to_game():
            learn_frame.pack_forget()
            for widget in learn_frame.winfo_children():
                widget.destroy()
        
            game_frame.pack(fill=BOTH, expand=True)
        

        def learn():
            #get first card
            info = []
            name_desc = newCard(get_random_flashcard())
            info.append(name_desc)
            def toggle_name():
                flashcard_button.configure(text=info[0][0], command=toggle_desc)
                
            def toggle_desc():
                flashcard_button.configure(text=info[0][1], command=toggle_name)

            def changeCard():
                name_desc = newCard(get_random_flashcard())
                info.clear()
                info.append(name_desc)
                toggle_name()

            #new screen so fade out
            game_frame.pack_forget()
            #create 3 buttons
            exit_img = ImageTk.PhotoImage(file="images/left.png")
            refLabel = Label(image=exit_img) 
            refLabel.image = exit_img # Making a copy so image isn't deleted during garbage collection

            next_img = ImageTk.PhotoImage(file="images/right.png")
            refLabel = Label(image=next_img) 
            refLabel.image = next_img # Making a copy so image isn't deleted during garbage collection

            
            exit_button = CTkButton(master=learn_frame, 
                                    corner_radius=5, 
                                    height=20, 
                                    width=30,
                                    border_spacing=10, 
                                    text="",
                                    image=exit_img,
                                    hover_color=("gray70", "gray30"),
                                    command=return_to_game,
                                    font=("Arial", 10))
            flashcard_button = CTkButton(learn_frame, 
                                    corner_radius=5, 
                                    height=20, 
                                    width=50,
                                    border_spacing=10, 
                                    text=info[0][0], 
                                    text_color=("gray10", "gray90"), 
                                    hover_color=("gray70", "gray30"),
                                    command=toggle_desc,
                                    font=("Arial", 30))
            load_new_flashcard_button = CTkButton(master=learn_frame, 
                                    corner_radius=5, 
                                    height=20, 
                                    width=30,
                                    text="",
                                    border_spacing=10, 
                                    image=next_img,
                                    hover_color=("gray70", "gray30"),
                                    command=changeCard,
                                    font=("Arial", 10))

            #place buttons
            exit_button.place(relx=0.1, rely=0.7, anchor=SW)
            flashcard_button.pack(side=TOP, fill=X, pady=200)
            load_new_flashcard_button.place(relx=0.9, rely=0.7, anchor=SE)

            learn_frame.pack(fill=BOTH, expand=True)
        def test():
            game_frame.pack_forget()
            def return_to_game():
                test_frame.pack_forget()
                for widget in test_frame.winfo_children():
                    widget.destroy()
            
                game_frame.pack(fill=BOTH, expand=True)

            inst1Label = CTkLabel(test_frame, text="", image=inst1_img)
            inst2Label = CTkLabel(test_frame, text="", image=inst2_img)
            inst3Label = CTkLabel(test_frame, text="", image=inst3_img)
            back_button = CTkButton(master=test_frame,
                                    corner_radius=5,
                                    height=20,
                                    width=30,
                                    border_spacing=10,
                                    text="",
                                    image=back_img,
                                    hover_color=("gray70", "gray30"),
                                    command=return_to_game,
                                    )
            
            back_button.place(relx=0.1, rely=0.8, anchor=SW)
            inst1Label.place(relx=0.5, rely=0.1, anchor=N)
            inst2Label.place(relx=0.5, rely=0.25, anchor=N)
            inst3Label.place(relx=0.5, rely=0.4, anchor=N)
            test_frame.pack(fill=BOTH, expand=True)
            
        def start_screen():
            game_frame.pack_forget()
            main_menu_frame.pack(fill=BOTH, expand=True)

        
        #generate buttons for 2 gamemodes
        #create button for mode selection
        learnbutton = CTkButton(master=game_frame, 
                                text="", 
                                image=learning_img,
                                command=learn).place(relx=0.5, rely=0.4, anchor=CENTER)
        testbutton = CTkButton(master=game_frame, 
                                text="", 
                                image=about_img,
                                command=test).place(relx=0.5, rely=0.6, anchor=CENTER)
        backButton = CTkButton(master=game_frame,
                                corner_radius=5,
                                height=20,
                                width=30,
                                border_spacing=10,
                                text="",
                                image=back_img,
                                command=start_screen,
                                ).place(relx=0.5, rely=0.8, anchor=CENTER)
            
        game_frame.pack(fill=BOTH, expand=True)

    #window
    set_appearance_mode("System")  # Modes: system (default), light, dark
    set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
    root = CTk()
    root.geometry("800x600")
    root.title("Hackathon App")

    #initialize images
    title_img = ImageTk.PhotoImage(Image.open("images/title.png"))
    start_img = ImageTk.PhotoImage(Image.open("images/start!.png"))
    quit_img = ImageTk.PhotoImage(Image.open("images/quit.png"))
    learning_img = ImageTk.PhotoImage(Image.open("images/startlearning!.png"))
    about_img = ImageTk.PhotoImage(Image.open("images/HowTo.png"))
    inst1_img = ImageTk.PhotoImage(Image.open("images/inst1.png"))
    inst2_img = ImageTk.PhotoImage(Image.open("images/inst2.png"))
    inst3_img = ImageTk.PhotoImage(Image.open("images/inst3.png"))
    back_img = ImageTk.PhotoImage(Image.open("images/back.png"))
    
    #start screen frame
    main_menu_frame = CTkFrame(master=root, height=800,width=600)
    main_menu_frame.pack_propagate(0)
    main_menu_frame.pack(fill=BOTH, expand=True)

    #main menu buttons
    start_button = CTkButton(master=main_menu_frame, 
                             text="", 
                             image=start_img, 
                             command=game_screen).place(relx=0.3, rely=0.5, anchor=CENTER)
    quit_button = CTkButton(master=main_menu_frame, 
                            text="", 
                            image=quit_img,
                            command=root.quit).place(relx=0.7,rely=0.5, anchor=CENTER)
    
    #title
    title_label = CTkLabel(main_menu_frame, 
                           image=title_img,
                           text="").place(relx=0.5, rely=0.2, anchor=CENTER)

    #game screen
    game_frame = CTkFrame(master=root, height=800,width=600)
    game_frame.pack_propagate(0)

    #learn screen
    learn_frame = CTkFrame(master=root, height=800,width=600)
    learn_frame.pack_propagate(0)

    #test screen
    test_frame = CTkFrame(master=root, height=800,width=600)
    #test_frame.pack_propagate(0)

    root.mainloop()