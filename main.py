import pyautogui as a, random as b, time as c, keyboard as d
e='wordlist.txt'
with open(e,'r',encoding='utf-8')as f:g=[line.strip()for line in f]
b.shuffle(g)
h=set()
def i(j):
    for k in[w for w in g if w not in h]:
        if j in k:h.add(k);return k
    return None
print("Program is running. Type a prompt and press enter. Press Ctrl+C to stop.")
try:
    while True:
        l=input().strip().lower()
        if l=="":h.clear();print("Used words have been reset.");continue
        m=i(l)
        if m:
            print(f"Matched word: {m}")
            a.hotkey('alt','tab')
            c.sleep(0.3)
            for n in m:
                if b.random()<0.1:
                    d.write(chr(ord(n)+1))
                    c.sleep(0.3) # Time to wait before typing backspace (this is adjustable)
                    d.press_and_release('backspace')
                d.write(n)
                c.sleep(b.uniform(0.07,0.09)) # Typing speed (this is adjustable)
            d.press_and_release('enter')
            c.sleep(0.3)
            a.hotkey('alt','tab')
        else:print("No unique word found for the given prompt.")
except KeyboardInterrupt:print("Program terminated by user.")
