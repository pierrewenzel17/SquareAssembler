from tkinter import Frame, Button, Menu, Toplevel, messagebox, IntVar, Label, Radiobutton, CENTER, TOP



class MenuView(Frame):

    def __init__(self, master, controller):
        super().__init__(master, background="white")
        self.controller = controller
##        self.onlineController = OnlineControlleur()

        self.menuBar = Menu(master)
        self.fileMenu = Menu(self.menuBar, tearoff=0)
        self.fileMenu.add_command(label="Nouveau", command=lambda: self.newGameChoiceFrame())
        self.fileMenu.add_command(label="Quitter", command=master.quit)
        self.menuBar.add_cascade(label="Jeu", menu=self.fileMenu)
        self.helpMenu = Menu(self.menuBar, tearoff=0)
        self.helpMenu.add_command(label="Aide", command=lambda: self.about())
        self.menuBar.add_cascade(label="A propos", menu=self.helpMenu)

        master.config(menu=self.menuBar)

    def about(self):
        messagebox.showinfo("information", self.controller.player.__str__())

    def newGameChoiceFrame(self):
        top = Toplevel()
        top.title("Choisir nouveau jeu")
        top.minsize(300, 200)
        radio_var = IntVar()
        radio_var.set(1)

        Label(top, text="Menu", font=("Courier", 25, "bold")).pack(side=TOP)
        Radiobutton(top, text="grille 10x10", variable=radio_var, value=1, relief='solid') \
            .place(relx=0.3, rely=0.3, anchor=CENTER)
        Radiobutton(top, text="grille 20x20", variable=radio_var, value=2, relief='solid') \
            .place(relx=0.7, rely=0.3, anchor=CENTER)
        Button(top, text="Jouer seul", width=30, relief='solid',
               command=lambda: [self.controller.new_game(radio_var.get()), top.destroy()]) \
            .place(relx=0.5, rely=0.5, anchor=CENTER)
        ''' Button(top, text="Créer une partie en ligne", width=30, relief='solid',
               command=lambda: self.onlineController.create_game(OnlineView())) \
            .place(relx=0.5, rely=0.7, anchor=CENTER)
            Button(top, text="Rejoindre une partie en ligne", width=30, relief='solid',
               command=lambda: self.onlineController.join_game(OnlineView())) \
            .place(relx=0.5, rely=0.9, anchor=CENTER)
            '''
        top.mainloop()
