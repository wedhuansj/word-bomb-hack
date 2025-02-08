import pyautogui as a, random as b, time as c
e='wordlist.txt'
with open(e,'r',encoding='utf-8')as f:g=[line.strip()for line in f]
b.shuffle(g)
h=set()
def i(j):return next((h.add(k)or k for k in(w for w in g if w not in h)if j in k),None)
print("Program is running. Type a prompt and press enter. Press Ctrl+C to stop.")
try:
    while 1:
        l=input().strip().lower()
        if l=="":h.clear();print("Used words have been reset.");continue
        m=i(l)
        if m:
            print(f"Matched word: {m}")
            a.hotkey('alt','tab');c.sleep(0.1)
            a.typewrite(m,interval=0.07) # Typing speed (this is adjustable)
            a.press('enter')
            c.sleep(0.1);a.hotkey('alt','tab')
        else:print("No unique word found for the given prompt.")
except KeyboardInterrupt:print("Program terminated by user.")
