from tkinter import *
from control import *
from flashcards import *

import urllib.request
from PIL import ImageTk, Image

def mainScreen():

    def game_screen():
        #main game screen

        #transition from start screen to game screen
        main_menu_frame.pack_forget()

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
            def toggle_name():
                flashcard_button.configure(text=name, command=toggle_desc)
                
                
            def toggle_desc():
                flashcard_button.configure(text=desc, command=toggle_name)

            
            #new screen so fade out
            game_frame.pack_forget()
            #create 3 buttons
            urllib.request.urlretrieve("https://www.clipartmax.com/png/middle/221-2210076_computer-icons-x-mark-check-mark-clip-art-red-x-icon.png", "image.png")
            exit_img = PhotoImage(Image.open("image.png"))

            exit_button = Button(learn_frame, image=exit_img, text="x", command=return_to_game).place(relx = 0.1, rely= 0.2, anchor=E)
            #get flashcard tuple
            name, desc = ("name","desc")
            flashcard_button = Button(learn_frame, text = name, command=toggle_desc)
            flashcard_button.pack()
            load_new_flashcard_button = Button(learn_frame, text=">", command=return_to_game)
            load_new_flashcard_button.pack()
            learn_frame.pack()
        def test():
            game_frame.pack_forget()
            
            test_frame.pack()
        
        #generate buttons for 2 gamemodes
        #create button for mode selection
        learnbutton = Button(game_frame, text="learn", command=learn).place(relx=0.5, rely=0.5, anchor=CENTER)
        testbutton = Button(game_frame, text="test", command=test).place(relx=0.6, rely=0.5, anchor=CENTER)
        game_frame.pack(fill=BOTH, expand=True)



    def start_screen():
        game_frame.pack_forget()
        for widget in game_frame.winfo_children():
            widget.destroy()
        main_menu_frame.pack(fill=BOTH, expand=True)

    #window
    root = Tk()
    root.geometry("1000x1000")
    root.title("Hackathon App")

    #start screen frame
    main_menu_frame = Frame(root, height=1000,width=1000)
    main_menu_frame.pack_propagate(0)
    main_menu_frame.pack(fill=BOTH, expand=True)

    #button to game_screen
    start_button = Button(main_menu_frame, text="Start", command=game_screen).place(relx=0.5, rely=0.5, anchor=CENTER)
    #exit
    quit_button = Button(main_menu_frame, text="Quit", command=root.quit).place(relx=0.5,rely=0.6, anchor=CENTER)

    #game screen
    game_frame = Frame(root, height=1000,width=1000)
    game_frame.pack_propagate(0)

    #learn screen
    learn_frame = Frame(root, height=1000,width=1000)
    learn_frame.pack_propagate(0)

    #test screen
    test_frame = Frame(root, height=1000,width=1000)
    #test_frame.pack_propagate(0)

    root.mainloop()





