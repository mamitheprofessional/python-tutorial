import tkinter as tk
from tkinter import ttk, messagebox

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ürün Takip Sistemi")
        self.root.geometry("1000x700")
        self.root.resizable(False, False)
        # Expense list
        self.expenses = []
        # UI Setup
        self.setup_ui()

    def setup_ui(self):
        # Style
        style = ttk.Style(self.root)
        style.theme_use('clam')
        # Set custom styles
        style.configure('TFrame', background='#f2f2f2')
        style.configure('TButton', font=('Helvetica', 12), background='#4CAF50', foreground='white')
        style.configure('TLabel', font=('Helvetica', 12), background='#f2f2f2', foreground='#333333')
        style.configure('TEntry', font=('Helvetica', 12), foreground='#333333')
        style.configure('Treeview', font=('Helvetica', 10), background='#e6e6e6', foreground='#333333',
        fieldbackground='#e6e6e6')
        style.configure('Treeview.Heading', font=('Helvetica', 12, 'bold'), background='#4CAF50',
        foreground='white')
        # Title Label
        title_label = ttk.Label(self.root, text="Ürün Ekleme Sistemi", font=("Helvetica", 18, "bold"),
        background='#4CAF50', foreground='white')
        title_label.pack(pady=20, padx=20, fill=tk.X)
        # Form Frame
        form_frame = ttk.Frame(self.root, padding="10 10 10 10")
        form_frame.pack(pady=20, padx=20, fill=tk.X)
        ttk.Label(form_frame, text="Ürün Adı:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
        self.description_entry = ttk.Entry(form_frame, width=30)
        self.description_entry.grid(row=0, column=1, padx=10, pady=10)
        ttk.Label(form_frame, text="Fiyat:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
        self.amount_entry = ttk.Entry(form_frame, width=30)
        self.amount_entry.grid(row=1, column=1, padx=10, pady=10)
        add_button = ttk.Button(form_frame, text="Ürün Ekle", command=self.add_expense)
        add_button.grid(row=2, column=0, columnspan=2, pady=20)
        # Treeview for displaying expenses
        columns = ("Description", "Amount")
        self.tree = ttk.Treeview(self.root, columns=columns, show='headings')
        self.tree.heading("Description", text="Ürün Adı")
        self.tree.heading("Amount", text="Fiyat ($)")
        self.tree.column("Description", anchor=tk.W, width=400)
        self.tree.column("Amount", anchor=tk.W, width=100)
        self.tree.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        # Total Amount Frame
        total_frame = ttk.Frame(self.root, padding="10 10 10 10")
        total_frame.pack(pady=10, padx=20, fill=tk.X)
        ttk.Label(total_frame, text="Toplam Fiyat:").grid(row=0, column=0, padx=10, pady=0, sticky=tk.E)
        self.total_label = ttk.Label(total_frame, text="$0.00")
        self.total_label.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
        clear_button = ttk.Button(total_frame, text="Hepsini Temizle", command=self.clear_expenses)
        clear_button.grid(row=0, column=2, padx=10, pady=10, sticky=tk.W)

    def add_expense(self):

        description = self.description_entry.get()
        amount = self.amount_entry.get()
        if description and amount:
            try:
                amount = float(amount)
                self.expenses.append((description, amount))
                self.update_treeview()
                self.update_total()
                self.description_entry.delete(0, tk.END)
                self.amount_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter a valid amount.")

        else:
            messagebox.showerror("Missing Information", "Please fill out all fields.")


    def clear_expenses(self):
        self.expenses.clear()
        self.update_treeview()
        self.update_total()

    def update_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for expense in self.expenses:
            self.tree.insert('', tk.END, values=expense)

    def update_total(self):
        total = sum(amount for _, amount in self.expenses)
        self.total_label.config(text=f"${total:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()