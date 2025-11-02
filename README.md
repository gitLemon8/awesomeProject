# Credits & Resources
This project was developed for Task 5.3D with help and reference of the following materials and tutorials:
- YouTube Tutorial: https://www.youtube.com/watch?v=a-q5y8zosWk
- GitHub Repository: https://github.com/ncorbuk/Python-Keylogger

# Prerequisites
This keylogger requires atleast Python 3 and the following libraries
- pynput
- pyinstaller

# Installation and Packaging
## 1. Install the required libraries
```bash
cd "YourWorkingDirectory"
python3 -m pip install pynput
python3 -m pip install pyinstaller
```
## 2. Create Executable
```bash
python3 -m PyInstaller keylogger.py
```
## 3. Run
Run the code and you can see the log in `theLog.txt` file
<img width="910" height="228" alt="image" src="https://github.com/user-attachments/assets/d329c25b-6d43-46bd-80c9-5a6e6bbbb921" />

# Termination
Stop the code or log
- ESC
- CTRL + C
