import tkinter as tk
root = tk.Tk()
frame =tk. Frame(root)
frame.pack()

bottomframe = tk.Frame(root)
bottomframe.pack()

redbutton = tk.Button(frame, text="Red", fg="red")
redbutton.pack()

greenbutton = tk.Button(frame, text="Brown", fg="brown")
#greenbutton.pack( side = LEFT )

bluebutton = tk.Button(frame, text="Blue", fg="blue")
#bluebutton.pack( side = LEFT )

blackbutton = tk.Button(bottomframe, text="Black", fg="black")
#blackbutton.pack( side = BOTTOM)
root.mainloop()
