import tkinter as tk

def highlight_selected():
    try:
        text_box1.tag_add('highlighted', tk.SEL_FIRST,  tk.SEL_LAST)
    except tk.TclError:
        #nothing is selected
        return

def highlight_keywords():
    #removes all tags from prevouis text
    text_box1.tag_remove('highlighted', '1.0', tk.END)
    keyword = word_box.get()
    text = text_box1.get('1.0', tk.END).split('\n')
    for line_number, line in enumerate(text):
        #splits the lines into a list of words
        words = line.split(' ')
        keyword_count = words.count(keyword)
        if keyword_count > 0:
            for index, word in enumerate(words):
                if word == keyword:
                    #joins all text in the line and adds them
                    new_text = ' '.join(words[:index])
                    word_start = f'{line_number+1}.{len(new_text)+1}'
                    # + 1 is for the space, so it starts at the next word
                    word_end = f'{line_number+1}.{len(new_text)+len(keyword)+1}'
                    text_box1.tag_add('highlighted', word_start, word_end)
                    #finally adds a tag at the specified index rang
            
root = tk.Tk()
root.title('Text Highlighter Example')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
frame1 = tk.Frame(root)
frame1.rowconfigure(0, weight=1)
frame1.columnconfigure(0, weight=1)

text_scroll = tk.Scrollbar(frame1)
text_box1 = tk.Text(frame1, yscrollcommand=text_scroll.set)
text_box1.configure(bg='black', foreground='white', insertbackground='white')
text_box1.tag_configure('highlighted', background='yellow', foreground='black')
word_box = tk.Entry(frame1)
word_box.configure(bg='black', foreground='white', insertbackground='white')
get_text = tk.Button(frame1, text='Highlight Selected', command=highlight_selected)
highlight_button = tk.Button(frame1, text='Highlight Keywords', command=highlight_keywords)

frame1.grid(column=0, row=0, sticky='nsew')
get_text.grid(column=0, row=1, sticky='nsew')
highlight_button.grid(column=0, row=2, sticky='nsew')
text_box1.grid(column=0, row=0, sticky='nsew')
word_box.grid(column=0, row=3, sticky='nsew')
text_scroll.grid(column=1, row=0, sticky='nsew')
text_scroll.config(command=text_box1.yview)

root.mainloop()
