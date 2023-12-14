def deposit():
    OUTPUT_PATH2 = Path(__file__).parent
    ASSETS_PATH2 = OUTPUT_PATH2 / Path(r"C:\Users\alana\OneDrive\Desktop\dbms proj\Transactions\build2\assets\frame0")


    def relative_to_assets2(path: str) -> Path:
        return ASSETS_PATH2 / Path(path)


    nwindow = Tk()

    nwindow.geometry("450x500")
    nwindow.configure(bg = "#1F43A0")

    canvas = Canvas(
        nwindow,
        bg = "#1F43A0",
        height = 500,
        width = 450,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets2("image_1.png"))
    image_1 = canvas.create_image(
        225.0,
        46.0,
        image=image_image_1
    )

    canvas.create_text(
        94.0,
        17.0,
        anchor="nw",
        text="Deposit",
        fill="#000000",
        font=("Inter Bold", 40 * -1)
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets2("image_2.png"))
    image_2 = canvas.create_image(
        191.0,
        355.0,
        image=image_image_2
    )

    canvas.create_text(
        75.0,
        268.0,
        anchor="nw",
        text="Enter amount to deposit",
        fill="#FFFFFF",
        font=("Inter Bold", 25 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets2("button_1.png"))
    button_1 = Button(
        nwindow,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=146.0,
        y=424.0,
        width=155.0,
        height=44.0
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets2("image_3.png"))
    image_3 = canvas.create_image(
        222.0,
        223.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets2("image_4.png"))
    image_4 = canvas.create_image(
        213.0,
        151.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets2("image_5.png"))
    image_5 = canvas.create_image(
        50.0,
        47.0,
        image=image_image_5
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets2("button_2.png"))
    button_2 = Button(
        nwindow,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=346.0,
        y=331.0,
        width=49.0,
        height=49.0
    )

    canvas.create_text(
        88.0,
        201.0,
        anchor="nw",
        text="0",
        fill="#000000",
        font=("Inter", 26 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets2("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        194.0,
        355.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        nwindow,
        bd=0,
        bg="#000000",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=85.0,
        y=335.0,
        width=218.0,
        height=39.0
    )
    nwindow.resizable(False, False)
    nwindow.mainloop()
