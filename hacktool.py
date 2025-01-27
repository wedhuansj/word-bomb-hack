import pyautogui, random, time, keyboard
word_list_path='wordlist.txt'
with open(word_list_path,'r',encoding='utf-8')as f:word_list=[line.strip()for line in f]
random.shuffle(word_list)
used_words=set()
def find_unique_word(prompt):
 for word in[w for w in word_list if w not in used_words]:
  if prompt in word:used_words.add(word);return word
 return None
print("Program is running. Type a prompt and press enter. Press Ctrl+C to stop.")
try:
 while True:
  prompt=input().strip().lower()
  if prompt=="":used_words.clear();print("Used words have been reset.");continue
  matched_word=find_unique_word(prompt)
  if matched_word:
   print(f"Matched word: {matched_word}")
   pyautogui.hotkey('alt','tab')
   time.sleep(0.3)
   for letter in matched_word:
    if random.random()<0.1:
     keyboard.write(chr(ord(letter)+1))
     time.sleep(0.3) # the time that wait then type backspace (you can change this)
     keyboard.press_and_release('backspace')
    keyboard.write(letter)
    time.sleep(random.uniform(0.07,0.09)) # speed type (you can change this)
   keyboard.press_and_release('enter')
   time.sleep(0.3)
   pyautogui.hotkey('alt','tab')
  else:print("No unique word found for the given prompt.") 
except KeyboardInterrupt:print("Program terminated by user.")
