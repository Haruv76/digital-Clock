import tkinter as tk
from datetime import datetime

BG = "#0f172a"
FG = "#e2e8f0"
FONT_TIME = ("Consolas", 64, "bold")
FONT_DATE = ("Consolas", 16)

def update_time():
    now = datetime.now()
    time_fmt = "%H:%M:%S" if var_24h.get() else "%I:%M:%S %p"
    date_fmt = "%A, %d %B %Y"
    lbl_time.config(text=now.strftime(time_fmt))
    lbl_date.config(text=now.strftime(date_fmt))
    root.after(1000, update_time)

def toggle_topmost():
    root.attributes("-topmost", var_top.get())

root = tk.Tk()
root.title("Digital Clock")
root.configure(bg=BG)

WIDTH, HEIGHT = 520, 220
x = (root.winfo_screenwidth() // 2) - (WIDTH // 2)
y = (root.winfo_screenheight() // 2) - (HEIGHT // 2)
root.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")
root.minsize(420, 200)

lbl_time = tk.Label(root, text="", font=FONT_TIME, fg=FG, bg=BG)
lbl_time.pack(pady=(24, 0))

lbl_date = tk.Label(root, text="", font=FONT_DATE, fg=FG, bg=BG)
lbl_date.pack(pady=(4, 16))

bar = tk.Frame(root, bg=BG)
bar.pack(pady=(0, 8))

var_24h = tk.BooleanVar(value=True)
chk_24h = tk.Checkbutton(
    bar, text="24h format", variable=var_24h,
    fg=FG, bg=BG, activebackground=BG, activeforeground=FG,
    selectcolor=BG, highlightthickness=0
)
chk_24h.pack(side="left", padx=8)

var_top = tk.BooleanVar(value=False)
chk_top = tk.Checkbutton(
    bar, text="Always on top", variable=var_top,
    command=toggle_topmost,
    fg=FG, bg=BG, activebackground=BG, activeforeground=FG,
    selectcolor=BG, highlightthickness=0
)
chk_top.pack(side="left", padx=8)

btn_quit = tk.Button(bar, text="Quit", command=root.destroy)
btn_quit.pack(side="left", padx=8)

update_time()
root.mainloop()
