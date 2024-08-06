import tkinter.font as tkfont


def configure():
    # family = "Segoe UI"
    family = "Helvetica"
    default_font = tkfont.nametofont("TkDefaultFont")
    default_font.configure(size=13, family=family)
    text_font = tkfont.nametofont("TkTextFont")
    text_font.configure(size=11, family=family)
    fixed_font = tkfont.nametofont("TkFixedFont")
    fixed_font.configure(size=11, family=family)
