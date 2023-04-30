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

        def return_from_test_mode():
            test_frame.pack_forget()
            for widget in test_frame.winfo_children():
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
            exit_img = ImageTk.PhotoImage(file="images/exit.png")
            refLabel = Label(image=exit_img) 
            refLabel.image = exit_img # Making a copy so image isn't deleted during garbage collection

            next_img = ImageTk.PhotoImage(file="images/right.png")
            refLabel = Label(image=next_img) 
            refLabel.image = next_img # Making a copy so image isn't deleted during garbage collection

            
            exit_button = CTkButton(master=learn_frame, 
                                    text= "", 
                                    image=exit_img, 
                                    command=return_to_game)
            flashcard_button = CTkButton(learn_frame, 
                                         corner_radius=0, 
                                         height=50, 
                                         width=70,
                                         border_spacing=10, 
                                         text=info[0][0], 
                                         text_color=("gray10", "gray90"), 
                                         hover_color=("gray70", "gray30"),
                                         command=toggle_desc,
                                         wraplength=80, 
                                         justify=LEFT,
                                         font=("Helvetica", 40))
            load_new_flashcard_button = CTkButton(master=learn_frame, 
                                                  text = "", 
                                                  image=next_img, 
                                                  command= changeCard)

            #place buttons
            exit_button.place(relx=0.1, rely=0.7, anchor=SW)
            flashcard_button.place(relx=0.5, rely=0.2, anchor=N)
            load_new_flashcard_button.place(relx=0.9, rely=0.7, anchor=SE)

            learn_frame.pack()
        def test():
            game_frame.pack_forget()
            
            test_frame.pack()
        
        #generate buttons for 2 gamemodes
        #create button for mode selection
        learnbutton = CTkButton(master=game_frame, text="learn", command=learn).place(relx=0.4, rely=0.5, anchor=CENTER)
        testbutton = CTkButton(master=game_frame, text="test", command=test).place(relx=0.6, rely=0.5, anchor=CENTER)
        game_frame.pack(fill=BOTH, expand=True)



    def start_screen():
        game_frame.pack_forget()
        for widget in game_frame.winfo_children():
            widget.destroy()
        main_menu_frame.pack(fill=BOTH, expand=True)

    #window
    set_appearance_mode("System")  # Modes: system (default), light, dark
    set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
    root = CTk()
    root.geometry("1000x1000")
    root.title("Hackathon App")


    #start screen frame
    main_menu_frame = CTkFrame(master=root, height=1000,width=1000)
    main_menu_frame.pack_propagate(0)
    main_menu_frame.pack(fill=BOTH, expand=True)

    #button to main menu
    start_button = CTkButton(master=main_menu_frame, text="Start", command=game_screen).place(relx=0.4, rely=0.5, anchor=CENTER)
    #exit
    quit_button = CTkButton(master=main_menu_frame, text="Quit", command=root.quit).place(relx=0.6,rely=0.5, anchor=CENTER)
    #title image 
    title_img = ImageTk.PhotoImage(Image.open("images/title.png"))
    title_label = CTkLabel(main_menu_frame, image=title_img).place(relx=0.5, rely=0.2, anchor=CENTER)

    #game screen
    game_frame = CTkFrame(master=root, height=1000,width=1000)
    game_frame.pack_propagate(0)

    #learn screen
    learn_frame = CTkFrame(master=root, height=1000,width=1000)
    learn_frame.pack_propagate(0)

    #test screen
    test_frame = CTkFrame(master=root, height=1000,width=1000)
    #test_frame.pack_propagate(0)

    root.mainloop()





