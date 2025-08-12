# Virtual Auto Typer

A simple Python application with a graphical user interface (GUI) that takes input text and automatically types it after a 5-second delay. This is especially useful for websites or applications that block copy-paste operations.

## Features

- User-friendly GUI using Tkinter
- Adjustable typing speed (currently fixed at 0.05 seconds per character)
- 5-second delay to switch to the target input window before typing starts
- Cross-platform compatibility (Windows, macOS, Linux)
```
VirtualAutoTyper/
├── autokey.py
├── requirements.txt
└── README.md
```
## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/VirtualAutoTyper.git
   cd VirtualAutoTyper

2.(Optional) Create and activate a virtual environment:

```
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```
3.Install dependencies:
```pip install -r requirements.txt```

Usage
Run the application:
```python autokey.py```


1.Enter or paste the text you want to type automatically.
2.Click the Start Typing button.
3.You will have 5 seconds to switch to the target window where you want the text typed.
4.The application will simulate keyboard typing of the entered text.

Build Executable (.exe) for Windows
To convert the script into a standalone executable:
1.Install PyInstaller:
```pip install pyinstaller```
2.Run PyInstaller:
```
pyinstaller --onefile --windowed autokey.py
```
3.Find the executable file in the dist folder.

Notes
Make sure the target window (where the text will be typed) is active and ready before the 5-second delay ends.

Typing speed is currently fixed but can be adjusted in the script (pyautogui.typewrite interval parameter).

Running the executable does not require Python to be installed on the target machine.

License
This project is licensed under the MIT License.

