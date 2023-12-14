def transhis():
    OUTPUT_PATH2 = Path(__file__).parent
    ASSETS_PATH2 = OUTPUT_PATH2 / Path(r"C:\Users\alana\OneDrive\Desktop\dbms proj\Transactions\build\assets\frame0")


    def relative_to_assets4(path: str) -> Path:
        return ASSETS_PATH2 / Path(path)


    newwindow = Toplevel(window)

    newwindow.geometry("900x650")
    newwindow.configure(bg = "#1F43A0")


    canvas = Canvas(
        newwindow,
        bg = "#1F43A0",
        height = 650,
        width = 900,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_14 = PhotoImage(
        file=relative_to_assets4("image_14.png"))
    image_14 = canvas.create_image(
        500.0,
        45.0,
        image=image_image_14
    )

    canvas.create_text(
        94.0,
        16.0,
        anchor="nw",
        text="Transactions History",
        fill="#000000",
        font=("Inter Bold", 40 * -1)
    )

    button_image_14 = PhotoImage(
        file=relative_to_assets4("button_14.png"))
    button_14 = Button(
        newwindow,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_14.place(
        x=372.0,
        y=569.0,
        width=155.0,
        height=44.0
    )

    image_image_24 = PhotoImage(
        file=relative_to_assets4("image_24.png"))
    image_24 = canvas.create_image(
        450.0,
        370.0,
        image=image_image_24
    )

    image_image_34 = PhotoImage(
        file=relative_to_assets4("image_34.png"))
    image_34 = canvas.create_image(
        43.0,
        43.0,
        image=image_image_34
    )

    canvas.create_text(
        76.0,
        121.0,
        anchor="nw",
        text="Last 5 transactions :",
        fill="#FFFFFF",
        font=("Inter Bold", 30 * -1)
    )
    newwindow.resizable(False, False)
    newwindow.mainloop()
