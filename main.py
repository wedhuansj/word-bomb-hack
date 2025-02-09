import tkinter as t, random as r
e='wordlist.txt'
with open(e,'r',encoding='utf-8')as f:g=[line.strip()for line in f]
r.shuffle(g)
h=set()
def i(j):return next((h.add(k)or k for k in[w for w in g if w not in h]if j in k),None)
def p(e=None):
    l=q.get().strip().lower()
    if l=="":h.clear();o.config(text="Used words have been reset.");return
    m=i(l)
    o.config(text=f"Matched word: {m}")if m else o.config(text="No unique word found for the given prompt.")
    q.delete(0,t.END)
a=t.Tk()
a.title("Character Display and Prompt Input")
a.geometry("400x200")
o=t.Label(a,text="",wraplength=380,font=("Helvetica",16))
o.pack(pady=10)
q=t.Entry(a,width=50,font=("Helvetica",16))
q.pack(pady=10)
q.bind("<Return>",p)
a.mainloop()
