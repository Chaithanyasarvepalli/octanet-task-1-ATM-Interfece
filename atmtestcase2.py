import tkinter as tk
import tkinter.font as font
import random
import sqlite3

class ATMApp:
    def __init__(self, root):
        self.root = root
        self.root.title('CRP Bank')
        self.root.geometry('460x390')
        self.root.configure(bg='navy')
        # Set background color
        
        self.tim40 = font.Font(family='Times', size=40, weight='bold', slant='italic', underline=1)
        self.cour20 = font.Font(family='Courier', size=20, weight='bold')
        self.cour15 = font.Font(family='Courier', size=15, weight='bold')

        self.setup_database()
        self.user_id = self.create_user()
        
        self.main_window()

    def setup_database(self):
        self.conn = sqlite3.connect('atm.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                               user_id INTEGER PRIMARY KEY,
                               balance REAL DEFAULT 0.0)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                               trans_id INTEGER PRIMARY KEY AUTOINCREMENT,
                               user_id INTEGER,
                               trans TEXT,
                               FOREIGN KEY (user_id) REFERENCES users (user_id))''')
        self.conn.commit()

    def create_user(self):
        user_id = random.randrange(1000, 10000)
        self.cursor.execute('INSERT INTO users (user_id) VALUES (?)', (user_id,))
        self.conn.commit()
        return user_id

    def main_window(self):
        self.title_label = tk.Label(self.root, text='CRP Bank', font=self.tim40, fg='red', bg='navy')
        self.title_label.pack(pady=10)

        self.intro = tk.Label(self.root, text=f'\nWelcome User {self.user_id}', font=self.cour20, fg='green', bg='navy')
        self.intro.pack()

        self.option_label = tk.Label(self.root, text='\nSelect your account type', font=self.cour15, fg='grey', bg='navy')
        self.option_label.pack()

        bottom_frame = tk.Frame(self.root, bg='navy')
        bottom_frame.pack(side=tk.BOTTOM)
        right_frame = tk.Frame(self.root, bg='navy')
        right_frame.pack(side=tk.RIGHT)

        note = tk.Label(bottom_frame, text='NOTE: Use only EXIT button to exit', font=self.cour15, fg='red', bg='navy')
        note.pack(pady=10)
        savings = tk.Button(right_frame, text='Savings', font=self.cour15, bg='light blue', fg='white', command=self.enter_pin)
        savings.pack(padx=30, pady=10)
        current = tk.Button(right_frame, text='Current', font=self.cour15, bg='light blue', fg='white', command=self.enter_pin)
        current.pack(padx=30, pady=10)

    def enter_pin(self):
        self.root.withdraw()
        self.enter_pin_win = tk.Toplevel(self.root)
        self.enter_pin_win.geometry('460x390')
        self.enter_pin_win.configure(bg='navy')  # Set background color

        lbl = tk.Label(self.enter_pin_win, text='Enter your PIN', font=self.cour20, fg='red', bg='navy')
        lbl.pack(pady=20)

        self.entry_box = tk.Entry(self.enter_pin_win, font=self.cour15, show='*', justify='center', bg='white')
        self.entry_box.pack()

        bf = tk.Frame(self.enter_pin_win, bg='navy')
        bf.pack(side=tk.BOTTOM)

        bf0 = tk.Frame(self.enter_pin_win, bg='navy')
        bf0.pack(side=tk.BOTTOM)

        bf1 = tk.Frame(self.enter_pin_win, bg='navy')
        bf1.pack(side=tk.BOTTOM)

        bf2 = tk.Frame(self.enter_pin_win, bg='navy')
        bf2.pack(side=tk.BOTTOM)

        bf3 = tk.Frame(self.enter_pin_win, bg='navy')
        bf3.pack(side=tk.BOTTOM)

        bf4 = tk.Frame(self.enter_pin_win, bg='navy')
        bf4.pack(side=tk.BOTTOM)

        btn1 = tk.Button(bf4, text='1', font=self.cour15, command=lambda: self.set_input_text('1'), bg='light blue', fg='white')
        btn1.pack(side=tk.LEFT, pady=10)

        btn2 = tk.Button(bf4, text='2', font=self.cour15, command=lambda: self.set_input_text('2'), bg='light blue', fg='white')
        btn2.pack(side=tk.LEFT, padx=10)

        btn3 = tk.Button(bf4, text='3', font=self.cour15, command=lambda: self.set_input_text('3'), bg='light blue', fg='white')
        btn3.pack(side=tk.LEFT)

        btn4 = tk.Button(bf3, text='4', font=self.cour15, command=lambda: self.set_input_text('4'), bg='light blue', fg='white')
        btn4.pack(side=tk.LEFT)

        btn5 = tk.Button(bf3, text='5', font=self.cour15, command=lambda: self.set_input_text('5'), bg='light blue', fg='white')
        btn5.pack(side=tk.LEFT, padx=10)

        btn6 = tk.Button(bf3, text='6', font=self.cour15, command=lambda: self.set_input_text('6'), bg='light blue', fg='white')
        btn6.pack(side=tk.LEFT)

        btn7 = tk.Button(bf2, text='7', font=self.cour15, command=lambda: self.set_input_text('7'), bg='light blue', fg='white')
        btn7.pack(side=tk.LEFT, pady=10)

        btn8 = tk.Button(bf2, text='8', font=self.cour15, command=lambda: self.set_input_text('8'), bg='light blue', fg='white')
        btn8.pack(side=tk.LEFT, padx=10)

        btn9 = tk.Button(bf2, text='9', font=self.cour15, command=lambda: self.set_input_text('9'), bg='light blue', fg='white')
        btn9.pack(side=tk.LEFT)

        btn0 = tk.Button(bf1, text='0', font=self.cour15, command=lambda: self.set_input_text('0'), bg='light blue', fg='white')
        btn0.pack(side=tk.LEFT, padx=10)

        enter_btn = tk.Button(bf0, text='ENTER', font=self.cour15, fg='green', command=self.option_func, bg='light blue')
        enter_btn.pack(side=tk.LEFT, pady=10, padx=10)

        exit_btn = tk.Button(bf0, text='EXIT', font=self.cour15, fg='red', command=lambda: [self.enter_pin_win.destroy(), self.root.deiconify()], bg='light blue')
        exit_btn.pack(side=tk.RIGHT, padx=10)

        clear_btn = tk.Button(bf0, text='CLEAR', font=self.cour15, fg='orange', command=self.text_delete, bg='light blue')
        clear_btn.pack(side=tk.LEFT)

        note = tk.Label(bf, text='Note: Enter pin either from keyboard or keypad', fg='red', bg='navy')
        note.pack()

    def set_input_text(self, text):
        self.entry_box.insert('end', text)

    def text_delete(self):
        self.entry_box.delete(0, 'end')

    def option_func(self):
        self.enter_pin_win.withdraw()
        self.option_win = tk.Toplevel(self.root)
        self.option_win.geometry('460x390')
        self.option_win.configure(bg='navy')  # Set background color

        text_title = tk.Label(self.option_win, text='\nCRP Bank', font=self.tim40, bg='navy',fg='red')
        text_title.pack()

        rf = tk.Frame(self.option_win, bg='navy')
        rf.pack(side=tk.RIGHT)

        lf = tk.Frame(self.option_win, bg='navy')
        lf.pack(side=tk.LEFT)

        withdrawal_btn = tk.Button(rf, text=' WITHDRAWAL ', font=self.cour15, command=self.withdrawal_func, bg='light blue', fg='white')
        withdrawal_btn.pack(padx=40, pady=10)

        deposit_btn = tk.Button(rf, text='  DEPOSIT  ', font=self.cour15, command=self.deposit_func, bg='light blue', fg='white')
        deposit_btn.pack(padx=40, pady=10)

        balance_btn = tk.Button(rf, text='BALANCE INQ', font=self.cour15, command=self.balance_func, bg='light blue', fg='white')
        balance_btn.pack(padx=40, pady=10)

        change_pin_btn = tk.Button(lf, text='CHANGE PIN', font=self.cour15, command=self.change_pin_func, bg='light blue', fg='white')
        change_pin_btn.pack(padx=40, pady=10)

        history_btn = tk.Button(lf, text='TRANS HISTORY', font=self.cour15, command=self.transaction_history_func, bg='light blue', fg='white')
        history_btn.pack(padx=40, pady=10)

        exit_btn = tk.Button(lf, text='   EXIT   ', font=self.cour15, fg='red', command=lambda: [self.option_win.destroy(), self.enter_pin_win.deiconify()], bg='light blue')
        exit_btn.pack(padx=40, pady=10)

    def withdrawal_func(self):
        self.option_win.withdraw()
        self.withdrawal_win = tk.Toplevel(self.root)
        self.withdrawal_win.geometry('460x390')
        self.withdrawal_win.configure(bg='navy')  # Set background color

        lbl = tk.Label(self.withdrawal_win, text='Enter amount to withdraw', font=self.cour20, fg='red', bg='navy')
        lbl.pack(pady=20)

        self.money_entry = tk.Entry(self.withdrawal_win, font=self.cour15, justify='center')
        self.money_entry.pack()

        bf = tk.Frame(self.withdrawal_win, bg='navy')
        bf.pack(side=tk.BOTTOM)

        enter_btn = tk.Button(bf, text='ENTER', font=self.cour15, fg='green', command=self.process_withdrawal, bg='light blue')
        enter_btn.pack(side=tk.LEFT, pady=10, padx=10)

        exit_btn = tk.Button(bf, text='EXIT', font=self.cour15, fg='red', command=lambda: [self.withdrawal_win.destroy(), self.option_win.deiconify()], bg='light blue')
        exit_btn.pack(side=tk.RIGHT, padx=10)

    def process_withdrawal(self):
        amt = self.money_entry.get()
        if not amt.isdigit() or int(amt) <= 0:
            self.show_message_win('Invalid amount. Please enter a valid amount.')
        else:
            amt = int(amt)
            current_balance = self.get_balance()
            if amt > current_balance:
                self.show_message_win('Insufficient funds.')
            else:
                new_balance = current_balance - amt
                self.update_balance(new_balance)
                self.add_transaction(f'Withdrawal: ${amt}')
                self.show_message_win(f'You have withdrawn ${amt} successfully')

    def deposit_func(self):
        self.option_win.withdraw()
        self.deposit_win = tk.Toplevel(self.root)
        self.deposit_win.geometry('460x390')
        self.deposit_win.configure(bg='navy')  # Set background color

        lbl = tk.Label(self.deposit_win, text='Enter amount to deposit', font=self.cour20, fg='red', bg='navy')
        lbl.pack(pady=20)

        self.money_entry = tk.Entry(self.deposit_win, font=self.cour15, justify='center')
        self.money_entry.pack()

        bf = tk.Frame(self.deposit_win, bg='navy')
        bf.pack(side=tk.BOTTOM)

        enter_btn = tk.Button(bf, text='ENTER', font=self.cour15, fg='green', command=self.process_deposit, bg='light blue')
        enter_btn.pack(side=tk.LEFT, pady=10, padx=10)

        exit_btn = tk.Button(bf, text='EXIT', font=self.cour15, fg='red', command=lambda: [self.deposit_win.destroy(), self.option_win.deiconify()], bg='light blue')
        exit_btn.pack(side=tk.RIGHT, padx=10)

    def process_deposit(self):
        amt = self.money_entry.get()
        if not amt.isdigit() or int(amt) <= 0:
            self.show_message_win('Invalid amount. Please enter a valid amount.')
        else:
            amt = int(amt)
            current_balance = self.get_balance()
            new_balance = current_balance + amt
            self.update_balance(new_balance)
            self.add_transaction(f'Deposit: ${amt}')
            self.show_message_win(f'You have deposited ${amt} successfully')

    def show_message_win(self, message):
        self.message_win = tk.Toplevel(self.root)
        self.message_win.geometry('460x390')
        self.message_win.configure(bg='navy')  # Set background color

        text_lbl = tk.Label(self.message_win, text=f'\n{message}\n', font=self.cour20, bg='navy')
        text_lbl.pack()

        exit_btn = tk.Button(self.message_win, text=' EXIT ', font=self.cour15, fg='red', command=lambda: [self.message_win.destroy(), self.option_win.deiconify()], bg='light blue')
        exit_btn.pack(padx=40, pady=20)

    def balance_func(self):
        self.option_win.withdraw()
        current_balance = self.get_balance()
        self.show_message_win(f'Your current balance is ${current_balance}')
        self.add_transaction('Balance Inquiry')

    def change_pin_func(self):
        self.option_win.withdraw()
        self.show_message_win('PIN change functionality not implemented yet')

    def transaction_history_func(self):
        self.option_win.withdraw()
        self.history_win = tk.Toplevel(self.root)
        self.history_win.geometry('460x390')
        self.history_win.configure(bg='navy')  # Set background color

        hist_lbl = tk.Label(self.history_win, text='\nTransaction History\n', font=self.cour20, fg='red', bg='navy')
        hist_lbl.pack()

        history = self.get_transaction_history()
        history_text = '\n'.join(history) if history else 'No transactions yet.'
        history_lbl = tk.Label(self.history_win, text=history_text, font=self.cour15, bg='navy')
        history_lbl.pack()

        exit_btn = tk.Button(self.history_win, text=' EXIT ', font=self.cour15, fg='red', command=lambda: [self.history_win.destroy(), self.option_win.deiconify()], bg='light blue')
        exit_btn.pack(padx=40, pady=20)

    def add_transaction(self, transaction):
        self.cursor.execute('INSERT INTO transactions (user_id, trans) VALUES (?, ?)', (self.user_id, transaction))
        self.conn.commit()

    def get_transaction_history(self):
        self.cursor.execute('SELECT trans FROM transactions WHERE user_id = ?', (self.user_id,))
        transactions = self.cursor.fetchall()
        return [trans[0] for trans in transactions]

    def get_balance(self):
        self.cursor.execute('SELECT balance FROM users WHERE user_id = ?', (self.user_id,))
        balance = self.cursor.fetchone()[0]
        return balance

    def update_balance(self, new_balance):
        self.cursor.execute('UPDATE users SET balance = ? WHERE user_id = ?', (new_balance, self.user_id))
        self.conn.commit()

if __name__ == '__main__':
    root = tk.Tk()
    app = ATMApp(root)
    root.mainloop()
