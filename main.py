import tkinter as tk
from tkinter import ttk, messagebox
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from market_logic import MarketSystem
C_THEME = "#27ae60"      
C_BTN = "#e1e1e1"
C_BG = "#f0f0f0"
FONT_STD = ("Arial", 10)
FONT_BOLD = ("Arial", 10, "bold")
FONT_BIG = ("Arial", 14, "bold")

class MarketApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Manav Projem")
        self.root.geometry("1250x850")
        self.root.configure(bg=C_BG)

        self.sys = MarketSystem()

        self.style = ttk.Style()
        self.style.theme_use('default') 
        self.style.configure("Treeview", font=FONT_STD, rowheight=25)
        self.style.configure("Treeview.Heading", font=FONT_BOLD)

        self.show_selector()
    def show_selector(self):
        self.clear()

        fr = tk.Frame(self.root, bg=C_BG)
        fr.place(relwidth=1, relheight=1)

        tk.Label(fr, text="INVENTORY MANAGEMENT SYSTEM", font=("Arial", 22, "bold"), bg=C_BG, fg=C_THEME).pack(pady=(80, 40))
        tk.Label(fr, text="Select Login Type:", font=("Arial", 12), bg=C_BG).pack(pady=(0, 20))
        
        btn_fr = tk.Frame(fr, bg=C_BG)
        btn_fr.pack()

        tk.Button(btn_fr, text="CUSTOMER", font=FONT_BOLD, bg=C_BTN, width=18, height=4, bd=3, relief="raised", 
                  command=self.screen_customer).pack(side="left", padx=15)
        
        tk.Button(btn_fr, text="STAFF", font=FONT_BOLD, bg=C_BTN, width=18, height=4, bd=3, relief="raised", 
                  command=self.login_staff).pack(side="left", padx=15)
        
        tk.Button(btn_fr, text="MANAGER", font=FONT_BOLD, bg=C_BTN, width=18, height=4, bd=3, relief="raised", 
                  command=self.login_manager).pack(side="left", padx=15)

        tk.Label(fr, text="Industrial Engineering Project - 2025", bg=C_BG, fg="gray").pack(side="bottom", pady=20)

    def login_staff(self):
        self.clear()
        f = tk.Frame(self.root, bg=C_BG)
        f.place(relx=0.5, rely=0.5, anchor="center")
        
        tk.Label(f, text="Staff Login", font=FONT_BIG, bg=C_BG, fg=C_THEME).pack(pady=10)
        tk.Label(f, text="Username:", bg=C_BG).pack(anchor="w")
        self.ent_user = ttk.Entry(f, font=FONT_STD)
        self.ent_user.pack(pady=5)
        tk.Label(f, text="Password:", bg=C_BG).pack(anchor="w")
        self.ent_pass = ttk.Entry(f, show="*", font=FONT_STD)
        self.ent_pass.pack(pady=5)
        tk.Button(f, text="Login", command=self.check_staff, width=15, bg=C_BTN).pack(pady=10)
        tk.Button(f, text="Back", command=self.show_selector, width=15, bg=C_BTN).pack()

    def login_manager(self):
        self.clear()
        f = tk.Frame(self.root, bg=C_BG)
        f.place(relx=0.5, rely=0.5, anchor="center")
        tk.Label(f, text="Manager Login", font=FONT_BIG, bg=C_BG, fg=C_THEME).pack(pady=10)
        tk.Label(f, text="Username:", bg=C_BG).pack(anchor="w")
        self.ent_user = ttk.Entry(f, font=FONT_STD)
        self.ent_user.pack(pady=5)
        tk.Label(f, text="Password:", bg=C_BG).pack(anchor="w")
        self.ent_pass = ttk.Entry(f, show="*", font=FONT_STD)
        self.ent_pass.pack(pady=5)
        tk.Button(f, text="Login", command=self.check_manager, width=15, bg=C_BTN).pack(pady=10)
        tk.Button(f, text="Back", command=self.show_selector, width=15, bg=C_BTN).pack()
    def check_staff(self):
        users = ["per1", "per2", "per3", "per4", "per5"]
        u = self.ent_user.get().lower()
        p = self.ent_pass.get()

        if u in users and p == "merve123":
            self.screen_staff()
        else:
            messagebox.showerror("Error", "Wrong credentials.")

    def check_manager(self):
        if self.ent_user.get() == "merve" and self.ent_pass.get() == "merve1234":
            self.screen_manager()
        else:
            messagebox.showerror("Error", "Wrong admin credentials.")
    def screen_customer(self):
        self.clear()
        h = tk.Frame(self.root, bg=C_THEME, height=60)
        h.pack(fill="x")
        tk.Label(h, text="SHOPPING SCREEN", bg=C_THEME, fg="white", font=FONT_BIG).pack(side="left", padx=20)
        tk.Button(h, text="EXIT", bg=C_BTN, command=self.show_selector).pack(side="right", padx=20)
        cont = tk.Frame(self.root, bg=C_BG, padx=20, pady=20)
        cont.pack(fill="both", expand=True)
        lf = tk.LabelFrame(cont, text="Select Product", font=FONT_BOLD, bg=C_BG)
        lf.pack(side="left", fill="both", expand=True, padx=10)
        
        tk.Label(lf, text="Item:", bg=C_BG).pack(anchor="w", padx=10, pady=5)
        p_names = [p.name for p in self.sys.product_list]
        self.cb_prod = ttk.Combobox(lf, values=p_names, state="readonly")
        self.cb_prod.pack(fill="x", padx=10)
        tk.Label(lf, text="Amount:", bg=C_BG).pack(anchor="w", padx=10, pady=5)
        self.ent_qty = ttk.Entry(lf)
        self.ent_qty.pack(fill="x", padx=10)
        tk.Button(lf, text="Add to Cart", bg=C_BTN, command=self.cust_add).pack(fill="x", padx=10, pady=20)

        rf = tk.LabelFrame(cont, text="My Cart", font=FONT_BOLD, bg=C_BG)
        rf.pack(side="right", fill="both", expand=True, padx=10)
        
        self.lst_cart = tk.Listbox(rf, font=FONT_STD)
        self.lst_cart.pack(fill="both", expand=True, padx=10, pady=10)
        
        tk.Button(rf, text="CHECKOUT", bg=C_BTN, font=FONT_BOLD, command=self.cust_checkout).pack(fill="x", padx=10, pady=10)
    def screen_staff(self):
        self.clear()
        h = tk.Frame(self.root, bg=C_THEME, height=60)
        h.pack(fill="x")
        tk.Label(h, text="STAFF INVENTORY", bg=C_THEME, fg="white", font=FONT_BIG).pack(side="left", padx=20)
        tk.Button(h, text="EXIT", bg=C_BTN, command=self.show_selector).pack(side="right", padx=20)
        
        cont = tk.Frame(self.root, bg=C_BG, padx=20, pady=20)
        cont.pack(fill="both", expand=True)
        f_left = tk.Frame(cont, bg=C_BG)
        f_left.pack(side="left", fill="both", expand=True, padx=(0, 10))
        cols = ("Name", "Stock", "Status")
        self.tree_staff = ttk.Treeview(f_left, columns=cols, show="headings")
        self.tree_staff.heading("Name", text="Product")
        self.tree_staff.heading("Stock", text="Stock")
        self.tree_staff.heading("Status", text="Status")
        self.tree_staff.pack(fill="both", expand=True)
        self.tree_staff.tag_configure("crit", background="#ffcccc")
        
        tk.Button(f_left, text="REFRESH LIST", bg=C_BTN, command=self.refresh_staff).pack(fill="x", pady=5)

        f_right = tk.Frame(cont, bg=C_BG)
        f_right.pack(side="right", fill="both", expand=True, padx=(10, 0))

        f_manual = tk.LabelFrame(f_right, text="Manual Restock", font=FONT_BOLD, bg=C_BG, pady=10, padx=10)
        f_manual.pack(fill="x", pady=(0, 10))

        tk.Label(f_manual, text="Product:", bg=C_BG).pack(side="left")
        p_names = [p.name for p in self.sys.product_list]
        self.cb_restock = ttk.Combobox(f_manual, values=p_names, state="readonly", width=15)
        self.cb_restock.pack(side="left", padx=5)

        tk.Label(f_manual, text="Qty:", bg=C_BG).pack(side="left")
        self.ent_restock_qty = ttk.Entry(f_manual, width=5)
        self.ent_restock_qty.pack(side="left", padx=5)

        tk.Button(f_manual, text="ADD STOCK", bg=C_BTN, command=self.staff_manual_add).pack(side="left", padx=10)

        f_graph = tk.LabelFrame(f_right, text="Stock Levels", font=FONT_BOLD, bg=C_BG)
        f_graph.pack(fill="both", expand=True)

        self.fig_st = Figure(figsize=(5, 4), dpi=100)
        self.ax_st = self.fig_st.add_subplot(111)
        self.cvs_st = FigureCanvasTkAgg(self.fig_st, f_graph)
        self.cvs_st.get_tk_widget().pack(fill="both", expand=True)

        self.refresh_staff()
    def screen_manager(self):
        self.clear()

        sb = tk.Frame(self.root, bg=C_THEME, width=250)
        sb.pack(side="left", fill="y")
        
        cont = tk.Frame(self.root, bg=C_BG)
        cont.pack(side="right", fill="both", expand=True)
        
        tk.Label(sb, text="MANAGER\nPANEL", bg=C_THEME, fg="white", font=("Arial", 16, "bold"), pady=30).pack()

        tk.Button(sb, text="Get Report", bg=C_BTN, font=FONT_BOLD, bd=2, pady=10, 
                  command=self.show_report).pack(fill="x", padx=10, pady=5)

        sim_frame = tk.LabelFrame(sb, text="Simulation", bg=C_THEME, fg="white", font=FONT_BOLD)
        sim_frame.pack(fill="x", padx=10, pady=20)
        
        tk.Label(sim_frame, text="Customer Count:", bg=C_THEME, fg="white").pack(anchor="w", padx=5)
        tk.Label(sim_frame, text="(EMPTY=RANDOM)", bg=C_THEME, fg="#ecf0f1", font=("Arial", 8)).pack(anchor="w", padx=5)
        
        self.ent_sim_count = ttk.Entry(sim_frame)
        self.ent_sim_count.pack(fill="x", padx=5, pady=5)
        
        tk.Button(sim_frame, text="RUN SIMULATION", bg=C_BTN, font=FONT_BOLD, bd=2, pady=5, 
                  command=self.run_sim).pack(fill="x", padx=5, pady=5)

        tk.Button(sb, text="LOGOUT", bg="#e74c3c", fg="white", font=FONT_BOLD, bd=2, pady=10, 
                  command=self.show_selector).pack(fill="x", padx=10, side="bottom", pady=20)

        tk.Label(cont, text="Overview", font=FONT_BIG, bg=C_BG).pack(pady=20)
        
        self.tree_mgr = ttk.Treeview(cont, columns=("N", "S", "T"), show="headings")
        self.tree_mgr.heading("N", text="Product")
        self.tree_mgr.heading("S", text="Stock")
        self.tree_mgr.heading("T", text="Threshold")
        self.tree_mgr.pack(fill="both", expand=True, padx=20, pady=10)
        self.refresh_mgr()

        gf = tk.Frame(cont, bg="white", padx=10, pady=10, relief="groove", bd=2)
        gf.pack(fill="x", padx=20, pady=20)
        tk.Label(gf, text="Open Graph for:", bg="white").pack(side="left")
        self.cb_graph = ttk.Combobox(gf, values=[p.name for p in self.sys.product_list], state="readonly")
        self.cb_graph.pack(side="left", padx=10)
        tk.Button(gf, text="OPEN", bg=C_BTN, command=self.popup_graph).pack(side="left")








    def clear(self):
        for w in self.root.winfo_children(): w.destroy()

    def cust_add(self):
        n = self.cb_prod.get()
        q = self.ent_qty.get()

        if n == "" or q == "":
            return
        if q.isdigit():
            if self.sys.add_to_cart(n, int(q)):
                self.lst_cart.insert(tk.END, f"{n} - {q}")
            else:
                messagebox.showerror("Error", "Not enough stock.")
        else:
            messagebox.showerror("Error", "Please enter a number.")

    def cust_checkout(self):
        if self.lst_cart.size() == 0: return
        log = self.sys.checkout_step1()
        self.lst_cart.delete(0, tk.END)
        messagebox.showinfo("Success", "Order Placed.\n" + log)
        self.sys.check_auto_order_step2()

    def staff_manual_add(self):
        n = self.cb_restock.get()
        q = self.ent_restock_qty.get()
        
        if n == "" or q == "": return

        if q.isdigit():
            val = int(q)
            self.sys.manual_add_stock(n, val)
            messagebox.showinfo("Info", f"Added {val} to {n}.")
            self.refresh_staff()
        else:
            messagebox.showerror("Error", "Invalid number.")

    def refresh_staff(self):
        for i in self.tree_staff.get_children(): self.tree_staff.delete(i)
        names, stocks, colors = [], [], []
        
        for p in self.sys.product_list:
            tg = "crit" if p.stock <= p.threshold else ""
            st = "CRITICAL" if p.stock <= p.threshold else "OK"
            self.tree_staff.insert("", "end", values=(p.name, p.stock, st), tags=(tg))

            names.append(p.name)
            stocks.append(p.stock)
            if p.stock <= p.threshold:
                colors.append('red')
            else:
                colors.append('green')

        self.ax_st.clear()
        self.ax_st.bar(names, stocks, color=colors)
        self.ax_st.set_title("Warehouse Levels")
        self.ax_st.tick_params(axis='x', rotation=45, labelsize=8) 
        self.fig_st.tight_layout()
        self.cvs_st.draw()

    def refresh_mgr(self):
        for i in self.tree_mgr.get_children(): self.tree_mgr.delete(i)
        for p in self.sys.product_list:
            self.tree_mgr.insert("", "end", values=(p.name, p.stock, p.threshold))

    def popup_graph(self):
        n = self.cb_graph.get()
        if n == "": return
        p = next((x for x in self.sys.product_list if x.name == n), None)
        if not p: return
        top = tk.Toplevel(self.root)
        top.title(f"Graph: {n}")
        top.geometry("600x400")
        
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot(p.history, marker="o", linestyle="-", color="blue")
        ax.axhline(y=p.threshold, color="red", linestyle="--", label="Threshold")
        ax.set_title(f"{n} Stock History")
        ax.legend()
        ax.grid(True)
        
        cvs = FigureCanvasTkAgg(fig, top)
        cvs.get_tk_widget().pack(fill="both", expand=True)

    def show_report(self):
        r = self.sys.get_report()
        top = tk.Toplevel(self.root)
        top.title("Report")
        t = tk.Text(top, padx=10, pady=10)
        t.pack(fill="both", expand=True)
        t.insert(tk.END, r)

    def run_sim(self):
        val = self.ent_sim_count.get()

        if val == "" or not val.isdigit():
            count = random.randint(50, 300)
            msg = f"Random Sim: {count} customers."
        else:

            count = int(val)
            msg = f"Manual Sim: {count} customers."

        for _ in range(count): self.sys.simulate_step()
        
        self.refresh_mgr()
        messagebox.showinfo("Simulation", f"{msg}\nData updated.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MarketApp(root)
    root.mainloop()
