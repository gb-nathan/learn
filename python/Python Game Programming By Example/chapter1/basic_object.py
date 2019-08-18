import tkinter as tk

class Game(tk.Frame):
    def __init__(self, window):
        super(Game, self).__init__(window)
        self.lives = 3
        self.width = 610
        self.height = 400
        self.canvas = tk.Canvas(self, bg='#aaaaff',
                                width=self.width,
                                height=self.height)
        self.canvas.pack()
        self.pack()
        self.canvas.create_rectangle(250, 300, 330, 320, fill='blue', tags='paddle')

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Hello, Pong!')
    game = Game(root)
    game.mainloop()