import tkinter as tk

root = tk.Tk()
root.geometry("300x300")
root.title("Cookie clicker")

cookieCount = tk.IntVar()
def buttonPressed():
    global cookieCount
    cookieCount.set(cookieCount.get() + 1)

tk.Label(root, text="Cookie clicker").pack()
tk.Button(root, text="Add cookie", command=buttonPressed).pack()
tk.Label(root, text="Cookie count: ").pack()

tk.Label(root, textvariable=cookieCount).pack()


root.mainloop()
