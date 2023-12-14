def transferacc():
    OUTPUT_PATH5 = Path(__file__).parent
    ASSETS_PATH5 = OUTPUT_PATH5 / Path(r"C:\Users\alana\OneDrive\Desktop\dbms proj\Transactions\build\assets\frame0")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH5 / Path(path)


    newwwindow = Toplevel(window)
    newwwindow.geometry("800x600")
    newwwindow.configure(bg = "#1F43A0")

    canvas = Canvas(
        newwwindow,
        bg = "#1F43A0",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_15 = PhotoImage(
        file=relative_to_assets("image_15.png"))
    image_15 = canvas.create_image(
        515.0,
        45.0,
        image=image_image_15
    )

    canvas.create_text(
        94.0,
        25.0,
        anchor="nw",
        text="Transfer to Another Account",
        fill="#000000",
        font=("Inter Bold", 40 * -1)
    )

    image_image_25 = PhotoImage(
        file=relative_to_assets("image_25.png"))
    image_25 = canvas.create_image(
        520.0,
        447.0,
        image=image_image_25
    )

    image_image_35 = PhotoImage(
        file=relative_to_assets("image_35.png"))
    image_35 = canvas.create_image(
        543.0,
        314.0,
        image=image_image_35
    )

    entry_image_15 = PhotoImage(
        file=relative_to_assets("entry_15.png"))
    entry_bg_15 = canvas.create_image(
        542.0,
        316.0,
        image=entry_image_15
    )
    entry_1 = Entry(
        newwwindow,
        bd=0,
        bg="#000000",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=423.0,
        y=297.0,
        width=238.0,
        height=36.0
    )

    canvas.create_text(
        393.0,
        428.0,
        anchor="nw",
        text="0",
        fill="#000000",
        font=("Inter", 22 * -1)
    )

    image_image_45 = PhotoImage(
        file=relative_to_assets("image_45.png"))
    image_45 = canvas.create_image(
        545.0,
        180.0,
        image=image_image_45
    )

    image_image_55 = PhotoImage(
        file=relative_to_assets("image_55.png"))
    image_55 = canvas.create_image(
        244.0,
        448.0,
        image=image_image_55
    )

    button_image_15 = PhotoImage(
        file=relative_to_assets("button_15.png"))
    button_15 = Button(
        newwwindow,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_15.place(
        x=325.0,
        y=526.0,
        width=155.0,
        height=44.0
    )

    canvas.create_text(
        46.0,
        284.0,
        anchor="nw",
        text="Enter amount to deposit :",
        fill="#FFFFFF",
        font=("Inter Bold", 26 * -1)
    )

    canvas.create_text(
        46.0,
        156.0,
        anchor="nw",
        text="Enter Account Number to\nTransfer to :",
        fill="#FFFFFF",
        font=("Inter Bold", 25 * -1)
    )

    image_image_65 = PhotoImage(
        file=relative_to_assets("image_65.png"))
    image_65 = canvas.create_image(
        50.0,
        45.0,
        image=image_image_65
    )

    button_image_25 = PhotoImage(
        file=relative_to_assets("button_25.png"))
    button_25 = Button(
        newwwindow,
        image=button_image_25,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_25.place(
        x=716.0,
        y=284.0,
        width=60.0,
        height=60.0
    )

    button_image_35 = PhotoImage(
        file=relative_to_assets("button_35.png"))
    button_35 = Button(
        newwwindow,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_35.place(
        x=716.0,
        y=150.0,
        width=60.0,
        height=60.0
    )

    entry_image_25 = PhotoImage(
        file=relative_to_assets("entry_25.png"))
    entry_bg_25 = canvas.create_image(
        
        543.0,
        181.0,
        image=entry_image_25
    )
    entry_25 = Entry(
        newwwindow,
        bd=0,
        bg="#000000",
        fg="#000716",
        highlightthickness=0
    )
    entry_25.place(
        x=424.0,
        y=162.0,
        width=238.0,
        height=36.0
    )
    newwwindow.resizable(False, False)
    newwwindow.mainloop()
