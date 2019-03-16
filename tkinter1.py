from tkinter import *

def appInterface(window):
    frame = Frame(window, borderwidth=1, width=400, height=200, relief=GROOVE, bg="pink");
    frame.pack(padx=10, pady=10, fill=X);

if __name__ == "__main__":
    app = Tk();
    app.title("First Window");
    app.geometry("500x500");
    appInterface(app);
    app.mainloop();