"""
Desktop GUI Application for People Database Management
"""
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from tkinter import font as tkfont
import sqlite3
from werkzeug.security import check_password_hash
from datetime import datetime

class PeopleDatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("People Database Management System")
        self.root.geometry("1200x700")
        self.root.configure(bg='#1a1a2e')
        
        self.current_user = None
        self.db_path = 'instance/people.db'
        
        # Show login screen
        self.show_login()
    
    def show_login(self):
        """ទំព័រ Login បែប Premium Card"""
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.root.configure(bg=self.colors['primary'])
        
        # Login Card Container
        login_frame = tk.Frame(self.root, bg='white', padx=40, pady=40, 
                               highlightbackground=self.colors['accent'], highlightthickness=2)
        login_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        tk.Label(login_frame, text="🔐 Login System", font=('Arial', 22, 'bold'), 
                 bg='white', fg=self.colors['primary']).grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Entry Styling
        tk.Label(login_frame, text="Username:", font=('Arial', 11), bg='white').grid(row=1, column=0, sticky='w')
        self.username_entry = tk.Entry(login_frame, font=('Arial', 12), width=28, bg='#f0f0f0', relief='flat')
        self.username_entry.grid(row=2, column=0, columnspan=2, pady=(5, 15))
        
        tk.Label(login_frame, text="Password:", font=('Arial', 11), bg='white').grid(row=3, column=0, sticky='w')
        self.password_entry = tk.Entry(login_frame, show='*', font=('Arial', 12), width=28, bg='#f0f0f0', relief='flat')
        self.password_entry.grid(row=4, column=0, columnspan=2, pady=(5, 20))
        
        # Premium Gold Button
        login_btn = tk.Button(login_frame, text="Login to System", font=('Arial', 12, 'bold'), 
                               bg=self.colors['accent'], fg='white', cursor='hand2',
                               activebackground=self.colors['primary'], activeforeground='white',
                               padx=40, pady=10, relief='flat', command=self.login)
        login_btn.grid(row=5, column=0, columnspan=2)
        
        self.password_entry.bind('<Return>', lambda e: self.login())
        self.username_entry.focus()
    
    def login(self):
        """Authenticate user"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Please enter username and password")
            return
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, password, role, province FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()
        
        if user and check_password_hash(user[2], password):
            self.current_user = {
                'id': user[0],
                'username': user[1],
                'role': user[3],
                'province': user[4]
            }
            self.log_action('login')
            self.show_main_app()
        else:
            messagebox.showerror("Error", "Invalid credentials")
    
    def show_main_app(self):
        """Display main application interface"""
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Top bar
        top_bar = tk.Frame(self.root, bg='#2196F3', height=60)
        top_bar.pack(fill='x')
        
        tk.Label(top_bar, text="👥 People Database Management", 
                font=('Arial', 18, 'bold'), bg='#2196F3', fg='white').pack(side='left', padx=20, pady=15)
        
        user_info = f"User: {self.current_user['username']} ({self.current_user['role']})"
        if self.current_user['province']:
            user_info += f" - {self.current_user['province']}"
        
        tk.Label(top_bar, text=user_info, font=('Arial', 10), 
                bg='#2196F3', fg='white').pack(side='right', padx=20)
        
        # Main container
        main_container = tk.Frame(self.root, bg='#f0f0f0')
        main_container.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Left panel - Search
        left_panel = tk.Frame(main_container, bg='white', relief='raised', bd=2)
        left_panel.pack(side='left', fill='both', padx=(0, 5), pady=0, expand=False)
        
        tk.Label(left_panel, text="🔍 Search Filters", font=('Arial', 14, 'bold'), 
                bg='white').pack(pady=10)
        
        # Search fields
        search_frame = tk.Frame(left_panel, bg='white')
        search_frame.pack(fill='both', padx=15, pady=5)
        
        fields = [
            ('ID:', 'id_entry'),
            ('Name:', 'name_entry'),
            ('Age:', 'age_entry'),
            ('Province:', 'province_entry'),
            ('District:', 'district_entry'),
            ('Commune:', 'commune_entry'),
            ('Village:', 'village_entry')
        ]
        
        for label, attr in fields:
            tk.Label(search_frame, text=label, font=('Arial', 10), bg='white').pack(anchor='w', pady=2)
            entry = tk.Entry(search_frame, font=('Arial', 10), width=25)
            
            # Disable province field for managers
            if attr == 'province_entry' and self.current_user['role'] == 'manager' and self.current_user['province']:
                entry.insert(0, self.current_user['province'])
                entry.config(state='disabled', bg='#FFF3E0', fg='#E65100', font=('Arial', 10, 'bold'))
            
            entry.pack(fill='x', pady=(0, 10))
            setattr(self, attr, entry)
        
        # Gender dropdown
        tk.Label(search_frame, text="Gender:", font=('Arial', 10), bg='white').pack(anchor='w', pady=2)
        self.gender_var = tk.StringVar(value='')
        gender_combo = ttk.Combobox(search_frame, textvariable=self.gender_var, 
                                    values=['', 'male', 'female'], state='readonly', width=23)
        gender_combo.pack(fill='x', pady=(0, 10))
        
        # Search button
        search_btn = tk.Button(search_frame, text="🔍 Search", font=('Arial', 11, 'bold'),
                              bg='#4CAF50', fg='white', command=self.search_people)
        search_btn.pack(fill='x', pady=10)
        
        # Clear button
        clear_btn = tk.Button(search_frame, text="Clear", font=('Arial', 10),
                             bg='#f44336', fg='white', command=self.clear_search)
        clear_btn.pack(fill='x')
        
        # Buttons
        btn_frame = tk.Frame(left_panel, bg='white')
        btn_frame.pack(fill='x', padx=15, pady=15)
        
        if self.current_user['role'] == 'super_admin':
            users_btn = tk.Button(btn_frame, text="👥 Manage Users", font=('Arial', 10),
                                 bg='#FF9800', fg='white', command=self.show_users)
            users_btn.pack(fill='x', pady=5)
        
        history_btn = tk.Button(btn_frame, text="📜 History", font=('Arial', 10),
                               bg='#9C27B0', fg='white', command=self.show_history)
        history_btn.pack(fill='x', pady=5)
        
        logout_btn = tk.Button(btn_frame, text="🚪 Logout", font=('Arial', 10),
                              bg='#607D8B', fg='white', command=self.logout)
        logout_btn.pack(fill='x', pady=5)
        
        # Right panel - Results
        right_panel = tk.Frame(main_container, bg='white', relief='raised', bd=2)
        right_panel.pack(side='right', fill='both', expand=True, padx=(5, 0))
        
        # Results header
        results_header = tk.Frame(right_panel, bg='white')
        results_header.pack(fill='x', padx=10, pady=10)
        
        tk.Label(results_header, text="📊 Search Results", font=('Arial', 14, 'bold'),
                bg='white').pack(side='left')
        
        self.result_count_label = tk.Label(results_header, text="Total: 0", 
                                           font=('Arial', 11), bg='white', fg='#666')
        self.result_count_label.pack(side='right')
        
        # Results table
        table_frame = tk.Frame(right_panel, bg='white')
        table_frame.pack(fill='both', expand=True, padx=10, pady=(0, 10))
        
        # Scrollbars
        vsb = ttk.Scrollbar(table_frame, orient="vertical")
        hsb = ttk.Scrollbar(table_frame, orient="horizontal")
        
        # Treeview
        columns = ('ID', 'Name', 'Gender', 'Age', 'Province', 'District', 'Commune', 'Village')
        self.tree = ttk.Treeview(table_frame, columns=columns, show='headings',
                                yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        
        vsb.config(command=self.tree.yview)
        hsb.config(command=self.tree.xview)
        
        # Column headings
        widths = [60, 150, 80, 60, 150, 120, 120, 120]
        for col, width in zip(columns, widths):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor='w' if col == 'Name' else 'center')
        
        # Pack scrollbars and tree
        vsb.pack(side='right', fill='y')
        hsb.pack(side='bottom', fill='x')
        self.tree.pack(fill='both', expand=True)
        
        # Pagination
        pagination_frame = tk.Frame(right_panel, bg='white')
        pagination_frame.pack(fill='x', padx=10, pady=(0, 10))
        
        self.page_var = tk.IntVar(value=1)
        self.total_pages_var = tk.IntVar(value=1)
        
        tk.Button(pagination_frame, text="◀ Previous", command=self.prev_page).pack(side='left', padx=5)
        tk.Label(pagination_frame, textvariable=self.page_var, font=('Arial', 10, 'bold'),
                bg='white').pack(side='left')
        tk.Label(pagination_frame, text=" / ", font=('Arial', 10), bg='white').pack(side='left')
        tk.Label(pagination_frame, textvariable=self.total_pages_var, font=('Arial', 10),
                bg='white').pack(side='left')
        tk.Button(pagination_frame, text="Next ▶", command=self.next_page).pack(side='left', padx=5)
        
        # Initial search
        self.search_people()

    
    def search_people(self):
        """Search people in database"""
        page = self.page_var.get()
        per_page = 100
        offset = (page - 1) * per_page
        
        # Build query
        query = "SELECT id, name, gender, age, province, district, commune, village FROM people WHERE 1=1"
        params = []
        
        # Province restriction for managers
        if self.current_user['role'] == 'manager' and self.current_user['province']:
            query += " AND province = ?"
            params.append(self.current_user['province'])
        
        # Search filters
        if self.id_entry.get():
            query += " AND id = ?"
            params.append(int(self.id_entry.get()))
        
        if self.name_entry.get():
            query += " AND name LIKE ?"
            params.append(f"%{self.name_entry.get()}%")
        
        if self.gender_var.get():
            query += " AND gender = ?"
            params.append(self.gender_var.get())
        
        if self.age_entry.get():
            query += " AND age = ?"
            params.append(int(self.age_entry.get()))
        
        if self.province_entry.get():
            query += " AND province LIKE ?"
            params.append(f"%{self.province_entry.get()}%")
        
        if self.district_entry.get():
            query += " AND district LIKE ?"
            params.append(f"%{self.district_entry.get()}%")
        
        if self.commune_entry.get():
            query += " AND commune LIKE ?"
            params.append(f"%{self.commune_entry.get()}%")
        
        if self.village_entry.get():
            query += " AND village LIKE ?"
            params.append(f"%{self.village_entry.get()}%")
        
        # Get total count
        count_query = query.replace("SELECT id, name, gender, age, province, district, commune, village", "SELECT COUNT(*)")
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute(count_query, params)
        total = cursor.fetchone()[0]
        
        # Get paginated results
        query += f" LIMIT {per_page} OFFSET {offset}"
        cursor.execute(query, params)
        results = cursor.fetchall()
        conn.close()
        
        # Update UI
        self.result_count_label.config(text=f"Total: {total:,}")
        total_pages = max(1, (total + per_page - 1) // per_page)
        self.total_pages_var.set(total_pages)
        
        # Clear tree
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Insert results
        for row in results:
            self.tree.insert('', 'end', values=row)
        
        self.log_action('search', details=f"Found {total} results")
    
    def clear_search(self):
        """Clear all search fields"""
        self.id_entry.delete(0, 'end')
        self.name_entry.delete(0, 'end')
        self.age_entry.delete(0, 'end')
        self.province_entry.delete(0, 'end')
        self.district_entry.delete(0, 'end')
        self.commune_entry.delete(0, 'end')
        self.village_entry.delete(0, 'end')
        self.gender_var.set('')
        self.page_var.set(1)
        self.search_people()
    
    def prev_page(self):
        """Go to previous page"""
        if self.page_var.get() > 1:
            self.page_var.set(self.page_var.get() - 1)
            self.search_people()
    
    def next_page(self):
        """Go to next page"""
        if self.page_var.get() < self.total_pages_var.get():
            self.page_var.set(self.page_var.get() + 1)
            self.search_people()
    
    def show_users(self):
        """Show user management window"""
        users_window = tk.Toplevel(self.root)
        users_window.title("User Management")
        users_window.geometry("900x600")
        users_window.configure(bg='#f0f0f0')
        
        # Header
        header = tk.Frame(users_window, bg='#2196F3', height=50)
        header.pack(fill='x')
        tk.Label(header, text="👥 User Management", font=('Arial', 16, 'bold'),
                bg='#2196F3', fg='white').pack(pady=10)
        
        # Create user form
        form_frame = tk.Frame(users_window, bg='white', relief='raised', bd=2)
        form_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(form_frame, text="Create New User", font=('Arial', 12, 'bold'),
                bg='white').grid(row=0, column=0, columnspan=4, pady=10)
        
        tk.Label(form_frame, text="Username:", bg='white').grid(row=1, column=0, padx=5, pady=5, sticky='e')
        username_entry = tk.Entry(form_frame, width=20)
        username_entry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="Password:", bg='white').grid(row=1, column=2, padx=5, pady=5, sticky='e')
        password_entry = tk.Entry(form_frame, width=20, show='*')
        password_entry.grid(row=1, column=3, padx=5, pady=5)
        
        tk.Label(form_frame, text="Role:", bg='white').grid(row=2, column=0, padx=5, pady=5, sticky='e')
        role_var = tk.StringVar(value='user')
        role_combo = ttk.Combobox(form_frame, textvariable=role_var, 
                                 values=['user', 'manager'], state='readonly', width=18)
        role_combo.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="Province:", bg='white').grid(row=2, column=2, padx=5, pady=5, sticky='e')
        province_var = tk.StringVar()
        
        provinces = [
            "Banteay Meanchey", "Battambang", "Kampong Cham",
            "Kampong Chhnang", "Kampong Speu", "Kampong Thom",
            "Kampot", "Kandal", "Koh Kong", "Kratie",
            "Mondul Kiri", "Phnom Penh", "Preah Vihear",
            "Prey Veng", "Pursat", "Ratanak Kiri",
            "Siemreap", "Preah Sihanouk", "Stung Treng",
            "Svay Rieng", "Takeo", "Oddar Meanchey",
            "Kep", "Pailin", "Tboung Khmum"
        ]
        
        province_combo = ttk.Combobox(form_frame, textvariable=province_var,
                                     values=provinces, state='readonly', width=25)
        province_combo.grid(row=2, column=3, padx=5, pady=5)
        
        def create_user():
            from werkzeug.security import generate_password_hash
            username = username_entry.get()
            password = password_entry.get()
            role = role_var.get()
            province = province_var.get() if role == 'manager' else None
            
            if not username or not password:
                messagebox.showerror("Error", "Username and password required")
                return
            
            if role == 'manager' and not province:
                messagebox.showerror("Error", "Province required for managers")
                return
            
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Check if username exists
            cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
            if cursor.fetchone():
                messagebox.showerror("Error", "Username already exists")
                conn.close()
                return
            
            # Check if province already has manager
            if role == 'manager':
                cursor.execute("SELECT username FROM users WHERE role = 'manager' AND province = ?", (province,))
                existing = cursor.fetchone()
                if existing:
                    messagebox.showerror("Error", f"Province already has manager: {existing[0]}")
                    conn.close()
                    return
            
            cursor.execute("INSERT INTO users (username, password, role, province) VALUES (?, ?, ?, ?)",
                         (username, generate_password_hash(password), role, province))
            conn.commit()
            conn.close()
            
            messagebox.showinfo("Success", "User created successfully")
            username_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            province_var.set('')
            refresh_users()
        
        create_btn = tk.Button(form_frame, text="➕ Create User", bg='#4CAF50', fg='white',
                              font=('Arial', 10, 'bold'), command=create_user)
        create_btn.grid(row=3, column=0, columnspan=4, pady=10)
        
        # Users list
        list_frame = tk.Frame(users_window, bg='white', relief='raised', bd=2)
        list_frame.pack(fill='both', expand=True, padx=10, pady=(0, 10))
        
        tk.Label(list_frame, text="All Users", font=('Arial', 12, 'bold'),
                bg='white').pack(pady=10)
        
        # Treeview
        tree_frame = tk.Frame(list_frame, bg='white')
        tree_frame.pack(fill='both', expand=True, padx=10, pady=(0, 10))
        
        vsb = ttk.Scrollbar(tree_frame, orient="vertical")
        columns = ('ID', 'Username', 'Role', 'Province', 'Created')
        users_tree = ttk.Treeview(tree_frame, columns=columns, show='headings',
                                 yscrollcommand=vsb.set)
        vsb.config(command=users_tree.yview)
        
        for col in columns:
            users_tree.heading(col, text=col)
            users_tree.column(col, width=150, anchor='center')
        
        vsb.pack(side='right', fill='y')
        users_tree.pack(fill='both', expand=True)
        
        def refresh_users():
            for item in users_tree.get_children():
                users_tree.delete(item)
            
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT id, username, role, province, created_at FROM users ORDER BY id")
            users = cursor.fetchall()
            conn.close()
            
            for user in users:
                users_tree.insert('', 'end', values=(
                    user[0], user[1], user[2], user[3] or '-',
                    user[4][:16] if user[4] else '-'
                ))
        
        def delete_user():
            selected = users_tree.selection()
            if not selected:
                messagebox.showwarning("Warning", "Please select a user to delete")
                return
            
            item = users_tree.item(selected[0])
            user_id = item['values'][0]
            username = item['values'][1]
            
            if user_id == self.current_user['id']:
                messagebox.showerror("Error", "Cannot delete yourself")
                return
            
            if messagebox.askyesno("Confirm", f"Delete user '{username}'?"):
                conn = sqlite3.connect(self.db_path)
                cursor = conn.cursor()
                cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "User deleted")
                refresh_users()
        
        btn_frame = tk.Frame(list_frame, bg='white')
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="🔄 Refresh", bg='#2196F3', fg='white',
                 command=refresh_users).pack(side='left', padx=5)
        tk.Button(btn_frame, text="🗑️ Delete Selected", bg='#f44336', fg='white',
                 command=delete_user).pack(side='left', padx=5)
        
        refresh_users()
    
    def show_history(self):
        """Show action history window"""
        history_window = tk.Toplevel(self.root)
        history_window.title("Action History")
        history_window.geometry("800x500")
        history_window.configure(bg='#f0f0f0')
        
        # Header
        header = tk.Frame(history_window, bg='#9C27B0', height=50)
        header.pack(fill='x')
        tk.Label(header, text="📜 Action History", font=('Arial', 16, 'bold'),
                bg='#9C27B0', fg='white').pack(pady=10)
        
        # Treeview
        tree_frame = tk.Frame(history_window, bg='white')
        tree_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        vsb = ttk.Scrollbar(tree_frame, orient="vertical")
        columns = ('ID', 'User', 'Action', 'Details', 'Timestamp')
        history_tree = ttk.Treeview(tree_frame, columns=columns, show='headings',
                                   yscrollcommand=vsb.set)
        vsb.config(command=history_tree.yview)
        
        widths = [50, 120, 100, 250, 150]
        for col, width in zip(columns, widths):
            history_tree.heading(col, text=col)
            history_tree.column(col, width=width, anchor='w' if col == 'Details' else 'center')
        
        vsb.pack(side='right', fill='y')
        history_tree.pack(fill='both', expand=True)
        
        # Load history
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        query = """
            SELECT h.id, u.username, h.action, h.details, h.timestamp
            FROM edit_history h
            JOIN users u ON h.user_id = u.id
        """
        
        if self.current_user['role'] == 'manager':
            query += " WHERE h.user_id = ?"
            cursor.execute(query + " ORDER BY h.timestamp DESC LIMIT 100", (self.current_user['id'],))
        else:
            cursor.execute(query + " ORDER BY h.timestamp DESC LIMIT 100")
        
        history = cursor.fetchall()
        conn.close()
        
        for row in history:
            history_tree.insert('', 'end', values=row)
    
    def log_action(self, action, person_id=None, details=None):
        """Log user action to database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO edit_history (user_id, person_id, action, details, timestamp)
            VALUES (?, ?, ?, ?, ?)
        """, (self.current_user['id'], person_id, action, details, datetime.now()))
        conn.commit()
        conn.close()
    
    def logout(self):
        """Logout current user"""
        self.log_action('logout')
        self.current_user = None
        self.show_login()


def main():
    root = tk.Tk()
    app = PeopleDatabaseApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
