import tkinter as tk

def createwindow(title):
    lives = 3
    root = tk.Tk()
    frame = tk.Frame(root)
    canvas = tk.Canvas(frame, width=600, height=400, bg='#aae3ff')
    frame.pack()
    canvas.pack()
    root.title(title)
    root.mainloop()

createwindow("pong") 
createwindow("nupdoop") 