# Word Bomb Hack - Character Display and Prompt Input Script

This repository contains a Python script that displays characters and has a box for inputting prompts. The script uses the `tkinter` library for the GUI and `pyautogui` for simulating key presses. Additionally, it includes instructions for using the script to hack Word Bomb in Roblox.

## Features

- Displays matched words based on user input
- Clears used words and resets the display
- GUI with larger text and Enter key submission

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/wedhuansj/word-bomb-hack.git
    ```
2. Navigate to the project directory:
    ```bash
    cd word-bomb-hack
    ```
3. Install the required packages:
    ```bash
    pip install pyautogui keyboard
    ```

## Usage

1. **Edit main.py**:
    Open the `main.py` file and make any changes you like to the script.

2. **Choose Language for Word List**:
    Navigate to the `worddata` folder.
    Select your desired language file and rename it to `wordlist.txt`.
    Replace the existing `wordlist.txt` in the directory with the chosen file.

3. **Setup**:
    Arrange the Command Prompt (cmd) and Roblox Player windows side by side.

4. **Run the script**:
    Execute `main.py` to start the program.
    ```bash
    python main.py
    ```
    When it’s your turn in the game, type the prompt in the Command Prompt window and enjoy.
    To reset the used word list, simply press Enter with a blank prompt.
    Press Ctrl+C in the Command Prompt to stop the program.
