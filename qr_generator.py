import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import qrcode


class App(ctk.CTk):
    def __init__(self):
        # window
        super().__init__(fg_color="#fff")
        ctk.set_appearance_mode("light")
        self.geometry("400x400")
        self.title("")
        self.iconbitmap("./empty.ico")

        # creating the widgets
        self.create_widgets()
        self.create_layout()
        self.maxsize(400, 400)
        self.minsize(400, 400)
        # starting the app
        self.mainloop()

    def create_widgets(self):
        # creating the frame
        self.frame = ctk.CTkFrame(master=self, corner_radius=20, fg_color="#021FB3")
        self.qr_string = tk.StringVar(value="")
        self.qr_string.trace("w", self.generate_qr)
        self.input = ctk.CTkEntry(
            master=self.frame, border_width=0, textvariable=self.qr_string
        )

        self.save_button = ctk.CTkButton(
            master=self.frame,
            text="save",
            command=self.save,
        )

        # creating the Qr image
        self.canvas = tk.Canvas(
            master=self,
            width=200,
            height=200,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        self.image = Image.open("Placeholder.png").resize((200, 200))
        self.image_tk = ImageTk.PhotoImage(image=self.image)
        self.canvas.create_image(0, 0, image=self.image_tk, anchor="nw")

    def create_layout(self):
        # the frame layout
        self.frame.rowconfigure((0, 1), weight=1, uniform="a")
        self.frame.columnconfigure((0, 3), weight=1, uniform="b")
        self.frame.columnconfigure(1, weight=4, uniform="b")
        self.frame.columnconfigure(2, weight=2, uniform="b")

        # placing inside the frame
        self.input.grid(
            row=0,
            column=1,
            sticky="ew",
        )
        self.save_button.grid(row=0, column=2, sticky="ew", padx=10)
        self.frame.place(relx=0.5, rely=1, relwidth=1, relheight=0.4, anchor="center")

        # placing the canvas
        self.canvas.place(
            relx=0.5, rely=0.4, relheight=0.5, relwidth=0.5, anchor="center"
        )

    def update_image(self, image):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=image, anchor="nw")

    def generate_qr(self, *args):
        if self.qr_string.get():
            self.image = qrcode.make(self.qr_string.get()).resize((200, 200))
            self.image_tk = ImageTk.PhotoImage(image=self.image)
            self.update_image(self.image_tk)

    def save(self):
        if self.image:
            filename = tk.filedialog.asksaveasfile(mode="w", defaultextension=".jpg")
            if filename:
                self.image.save(filename)
                self.qr_string.set("")


class EntryField(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, corner_radius=20, fg_color="#021FB3")


App()
