from tkinter import *
def mainScreen():

    def game_screen():
        #main game screen

        #transition from start screen to game screen
        main_menu_frame.pack_forget()
        second_frame.pack(fill=BOTH, expand=True)

        #run gameplay loop

        #get english words

        #get english descriptions

        #add and/or update labels and buttons

        #check if user answer is correct, return True or False


        #ask user if they would like to play again
        #if yes, restart loop, if no, jump to start screen
        start_screen()

    def start_screen():
        second_frame.pack_forget()
        for widget in second_frame.winfo_children():
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
    second_frame = Frame(root, height=1000,width=1000)
    second_frame.pack_propagate(0)

    root.mainloop()





