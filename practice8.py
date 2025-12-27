import tkinter as tk
from tkinter import messagebox

def mohasebe():
    mablagh = entry_total.get()
    nafarat = entry_people.get()
  
    if mablagh == "" or nafarat == "":
        messagebox.showwarning("خطا", "فیلد ")
        return  
    if not mablagh.isdigit() or not nafarat.isdigit():
        messagebox.showwarning("خطا", "عدد وارد شود")
        return

    mablagh = int(mablagh)
    nafarat = int(nafarat)

    if nafarat == 0:
        messagebox.showwarning("خطا", "ههئئ وارد کنیدد")
        return

    natije = mablagh / nafarat
    messagebox.showinfo("نتیجه", f"سهم هر نفر: {natije} تومان")
root = tk.Tk()
root.title("تقسیم هزینه")
root.geometry("300x200")

tk.Label(root, text="Total Bill").pack(pady=5)
entry_total = tk.Entry(root)
entry_total.pack()

tk.Label(root, text="Number of People").pack(pady=5)
entry_people = tk.Entry(root)
entry_people.pack()

btn = tk.Button(root, text="محاسبه سهم", command=mohasebe)
btn.pack(pady=15)

root.mainloop()
