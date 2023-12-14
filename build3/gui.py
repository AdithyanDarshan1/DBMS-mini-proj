def withdraw():
    OUTPUT_PATH3 = Path(__file__).parent
    ASSETS_PATH3 = OUTPUT_PATH3 / Path(r"C:\Users\alana\OneDrive\Desktop\dbms proj\Transactions\build3\assets\frame0")

    def relative_to_assets3(path: str) -> Path:
        return ASSETS_PATH3 / Path(path)

    newindow = Tk()

    newindow.geometry("450x500")
    newindow.configure(bg = "#1F43A0")


    canvas = Canvas(
        newindow,
        bg = "#1F43A0",
        height = 500,
        width = 450,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_13 = PhotoImage(
        file=relative_to_assets3("image_13.png"))
    image_13 = canvas.create_image(
        225.0,
        45.0,
        image=image_image_13
    )

    canvas.create_text(
        94.0,
        19.0,
        anchor="nw",
        text="Withdraw",
        fill="#000000",
        font=("Inter Bold", 40 * -1)
    )

    image_image_23 = PhotoImage(
        file=relative_to_assets3("image_23.png"))
    image_23 = canvas.create_image(
        191.0,
        355.0,
        image=image_image_23
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets3("entry_13.png"))
    entry_bg_1 = canvas.create_image(
        194.0,
        355.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#000000",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        newindow,
        x=85.0,
        y=335.0,
        width=218.0,
        height=39.0
    )

    button_image_13 = PhotoImage(
        file=relative_to_assets3("button_13.png"))
    button_1 = Button(
        image=button_image_13,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_13.place(
        newindow,
        x=346.0,
        y=331.0,
        width=49.0,
        height=49.0
    )

    canvas.create_text(
        63.0,
        259.0,
        anchor="nw",
        text="Enter amount to withdraw :",
        fill="#FFFFFF",
        font=("Inter Bold", 25 * -1)
    )

    button_image_23 = PhotoImage(
        file=relative_to_assets3("button_23.png"))
    button_23 = Button(
        newindow,
        image=button_image_23,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_23.place(
        x=148.0,
        y=424.0,
        width=155.0,
        height=44.0
    )

    image_image_33 = PhotoImage(
        file=relative_to_assets3("image_33.png"))
    image_33 = canvas.create_image(
        226.0,
        207.0,
        image=image_image_33
    )

    canvas.create_text(
        88.0,
        186.0,
        anchor="nw",
        text="0",
        fill="#000000",
        font=("Inter", 26 * -1)
    )

    image_image_43 = PhotoImage(
        file=relative_to_assets3("image_43.png"))
    image_43 = canvas.create_image(
        50.0,
        48.0,
        image=image_image_43
    )

    image_image_53 = PhotoImage(
        file=relative_to_assets3("image_53.png"))
    image_53 = canvas.create_image(
        212.0,
        142.0,
        image=image_image_53
    )
    newindow.resizable(False, False)
    newindow.mainloop()
