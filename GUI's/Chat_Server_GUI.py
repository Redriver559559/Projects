#WIP, Very broken

import tkinter as tk
import datetime

root = tk.Tk()
root.title('Testing')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

username = 'test1234'

class App:
    def __init__(self):
       self.current_line = 1
       self.current_length = 0
       self.temp_input = []

    def get_time(self):
        """Gets the users current time and returns a time object"""
        time = datetime.datetime.now()
        return (time.strftime("%m/%d/%Y %#I:%M %p"))
        #return (''.join(random.sample(['1','2','3','4','5'],k=5))+'-'*14+'>'+('\n'*(self.current_line-1)))

    def display_message(self, message):
        message = '\n'.join(message)
        time = self.get_time()
        space = (info_box.cget('width')-21-len(username))
        if len(chat_box.get('1.0', tk.END)) > 1:
            message = '\n'+message
            time = '\n'+time
        chat_box.configure(state=tk.NORMAL)
        chat_box.insert(tk.END, message)
        chat_box.see(tk.END)
        chat_box.configure(state=tk.DISABLED)

        info_box.configure(state=tk.NORMAL)
        info_box.insert(tk.END, f"{time}{' '*space}[{username}]"+(('\n'+' '*33+'⌊')*(len(self.temp_input)-1)))
        info_box.see(tk.END)
        info_box.configure(state=tk.DISABLED)
        self.temp_input = []

    def send_message(self):
        """WIP"""
        pass

    def check_input(self, event):
        key = event.keysym
        state = event.state
        #total length of the input box, it is 2 columns wide
        total_input_length = chat_box.cget('width') + info_box.cget('width')+5
        if self.current_length >= total_input_length:
            self.current_line += 1
            text_input.configure(height=self.current_line)
            text_input.insert(tk.END, '\n')
            self.current_length = 0
        
        #if the user hits the return button then check for shift+return or normal
        if key == 'Return':
            if state == 8:
                #normal return state, gets the text and the lines and displays the input
                non_empty_lines = 0
                for i in range(1, self.current_line+1):
                    line = (text_input.get(f'{i}.0', f'{i}.{total_input_length}'))
                    self.temp_input.append(line)
                    if len(line) != 0:
                        non_empty_lines += 1
                if non_empty_lines < 2:
                    self.temp_input = [x for x in self.temp_input if len(x) > 0]
                
                self.display_message(self.temp_input)
                text_input.delete('1.0', tk.END)
                self.current_line = 1
                text_input.configure(height=self.current_line)

            elif state == 9:
                #shift return adds a new empty line
                text_input.insert(tk.END, '\n')
                self.current_line += 1
                text_input.configure(height=self.current_line)
            self.current_length = 0
            return 'break'
        #this is kind of working but its very messy
        elif key == 'BackSpace':
            if self.current_length >= 0:
                self.current_length -= 1
            if self.current_length < 0:
                if self.current_line > 1:
                    self.current_line -= 1
                    text_input.configure(height=self.current_line)
                    self.current_length = len(text_input.get(f'{self.current_line}.0', 'insert'))-1
        #need to add a delete key and much more
        else:
            self.current_length += 1

    def move_textbox(self, *args):
        info_box.yview(*args)
        chat_box.yview(*args)

    def mousewheel_scroll(self, event):
        y = -1*(event.delta//120)
        info_box.yview_scroll(y, 'units')
        chat_box.yview_scroll(y, 'units')
        return 'break'

app = App()

frame1 = tk.Frame(root)
frame1.rowconfigure(0, weight=1)
frame1.columnconfigure(1, weight=1)

text_scroll = tk.Scrollbar(frame1)
text_scroll.configure(command=app.move_textbox)
chat_box = tk.Text(frame1, yscrollcommand=text_scroll.set)
chat_box.configure(bg='black', foreground='white', insertbackground='white', border=10, state=tk.DISABLED)
chat_box.tag_configure('highlighted', background='yellow', foreground='black')
chat_box.bind('<MouseWheel>', app.mousewheel_scroll)

info_box = tk.Text(frame1, yscrollcommand=text_scroll.set, width=35)
info_box.configure(bg='black', foreground='white', insertbackground='white', border=10, state=tk.DISABLED)
info_box.tag_configure('highlighted', background='yellow', foreground='black')
info_box.bind('<MouseWheel>', app.mousewheel_scroll)

text_input = tk.Text(frame1, bg='black', foreground='white', insertbackground='white')
text_input.bind('<Key>', app.check_input)
text_input.configure(height=1)
text_input.grid(column=0, row=1, sticky='nsew', columnspan=2)

frame1.grid(column=0, row=0, sticky='nsew')

chat_box.grid(column=1, row=0, sticky='nsew')
info_box.grid(column=0, row=0, sticky='nsew')
text_scroll.grid(column=2, row=0, sticky='nsew')

root.mainloop()
