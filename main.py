import matplotlib.pyplot as plt

from FuzzyNumber import TrapNumber


def go(plot_area, operator):
    fuzzy_a = TrapNumber(
        float(text_a.get("1.0", "end-1c")),
        float(text_b.get("1.0", "end-1c")),
        float(text_c.get("1.0", "end-1c")),
        float(text_d.get("1.0", "end-1c"))
    )

    fuzzy_b = TrapNumber(
        float(text_i.get("1.0", "end-1c")),
        float(text_j.get("1.0", "end-1c")),
        float(text_k.get("1.0", "end-1c")),
        float(text_l.get("1.0", "end-1c"))
    )

    if operator == '+':
        result = fuzzy_a + fuzzy_b
    elif operator == '-':
        result = fuzzy_a - fuzzy_b
    elif operator == '*':
        result = fuzzy_a * fuzzy_b
    elif operator == '/':
        result = fuzzy_a / fuzzy_b

    plot_area.cla()
    plot_area.plot(result.xs(), result.ys(), 'r', fuzzy_a.xs(), fuzzy_a.ys(), 'bo-', fuzzy_b.xs(), fuzzy_b.ys(), 'go-')
    canvas.draw()

if __name__ == '__main__':
    import Tkinter as Tk
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

    root = Tk.Tk()
    root.wm_title("FuzzyCalc")

    a = TrapNumber(1, 2, 3, 4)
    b = TrapNumber(4, 5, 6, 7)

    f = Figure(figsize=(5, 4), dpi=100)
    plt = f.add_subplot(111)

    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.show()
    canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

    canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

    frame = Tk.Frame(bg="white", colormap="new")
    frame.pack(side=Tk.BOTTOM)

    frame_controls = Tk.Frame(bg="white", colormap="new")
    frame_controls.pack(side=Tk.BOTTOM)

    frame_trap_b = Tk.Frame(bg="white", colormap="new")
    frame_trap_b.pack(side=Tk.BOTTOM)

    frame_trap_a = Tk.Frame(bg="white", colormap="new")
    frame_trap_a.pack(side=Tk.BOTTOM)

    l1 = Tk.Label(master=frame_trap_a, text="Trapeze A", fg="blue")
    l1.pack(side=Tk.LEFT)
    text_a = Tk.Text(master=frame_trap_a, width=5, height=1)
    text_a.insert('end', "1")
    text_a.pack(side=Tk.LEFT)

    text_b = Tk.Text(master=frame_trap_a, width=5, height=1)
    text_b.pack(side=Tk.LEFT)
    text_b.insert('end', "2")

    text_c = Tk.Text(master=frame_trap_a, width=5, height=1)
    text_c.pack(side=Tk.LEFT)
    text_c.insert('end', "3")

    text_d = Tk.Text(master=frame_trap_a, width=5, height=1)
    text_d.pack(side=Tk.LEFT)
    text_d.insert('end', "4")

    button = Tk.Button(master=frame_controls, text="Sum", command=lambda: go(plt, '+'))
    button.pack(side=Tk.LEFT)
    button = Tk.Button(master=frame_controls, text="Sub", command=lambda: go(plt, '-'))
    button.pack(side=Tk.LEFT)
    button = Tk.Button(master=frame_controls, text="Mul", command=lambda: go(plt, '*'))
    button.pack(side=Tk.LEFT)
    button = Tk.Button(master=frame_controls, text="Div", command=lambda: go(plt, '/'))
    button.pack(side=Tk.LEFT)

    l1 = Tk.Label(master=frame_trap_b, text="Trapeze B", fg="forest green")
    l1.pack(side=Tk.LEFT)
    text_i = Tk.Text(master=frame_trap_b, width=5, height=1)
    text_i.pack(side=Tk.LEFT)
    text_i.insert('end', "5")

    text_j = Tk.Text(master=frame_trap_b, width=5, height=1)
    text_j.pack(side=Tk.LEFT)
    text_j.insert('end', "6")

    text_k = Tk.Text(master=frame_trap_b, width=5, height=1)
    text_k.pack(side=Tk.LEFT)
    text_k.insert('end', "10")

    text_l = Tk.Text(master=frame_trap_b, width=5, height=1)
    text_l.pack(side=Tk.LEFT)
    text_l.insert('end', "18")

    Tk.mainloop()
