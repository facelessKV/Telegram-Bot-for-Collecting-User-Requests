📝 Telegram Bot for Collecting User Requests

Need an easy way to collect and manage user requests? This bot allows users to submit requests directly via Telegram, storing them for review and action!
Whether you’re handling customer inquiries, support tickets, or general feedback, this bot streamlines the process.

✅ What does it do?

 • 📩 Collects user requests via simple Telegram commands
 • 📋 Organizes and stores all submissions for easy access
 • 🔔 Sends notifications for new requests
 • 🏷️ Supports request categorization for better management

🔧 Features

✅ Easy-to-use request submission system
✅ Organized request tracking for efficient handling
✅ Notifications to ensure no request goes unnoticed

📩 Want to automate user request collection?

Contact me on Telegram, and I’ll help you set up this bot to manage user inquiries seamlessly! 🚀

======================================
HOW TO LAUNCH A TELEGRAM BOT TO COLLECT APPLICATIONS
======================================

This document contains step-by-step instructions for installing and running a Telegram bot on a Windows or Linux computer.

======================================
1. PREPARATION (THE SAME FOR WINDOWS AND LINUX)
======================================

1.1. GETTING A BOT TOKEN:

1) Open Telegram and find the bot @BotFather
2) Send a command to /newbot
3) Enter the name of the bot (for example, "Application Collection Bot")
4) Enter the bot's username (must end with "bot", for example "my_request_bot")
5) BotFather will give you a token like "1234567890:ABCDefGhIJKlmnOPQRstUVwxYZ". Save it!

1.2. RECEIVING THE CHAT ID OF THE ADMINISTRATOR (WHERE THE REQUESTS WILL BE RECEIVED):

1) Find the @userinfobot bot in Telegram
2) Send him any message.
3) The bot will reply to you with your ID, which is a number, for example, "123456789"
4) Write down this ID, which will be your ADMIN_CHAT_ID

======================================
2. INSTALLATION ON WINDOWS
======================================

2.1. INSTALLING PYTHON:

1) Download Python 3.10.6 from the official website:
https://www.python.org/downloads/release/python-3106 /
(scroll down and select "Windows installer (64-bit)")

2) Run the downloaded file. IMPORTANT: check the box "Add Python to PATH" at the bottom of the installer window!

3) Click "Install Now" and wait for the installation to complete

2.2. DOWNLOADING AND CONFIGURING THE BOT:

1) Create a "TelegramBot" folder on your desktop

2) Place the file with the bot code (for example, bot.py ) to this folder

3) Open Notepad: press Win+R, type "notepad" and press Enter

4) Write in your notebook:
   BOT_TOKEN=your_token_bot
   ADMIN_CHAT_ID=your_id_chata

   Replace "your_token_bot" with the token received from BotFather
   Replace "your_id_chata" with the ID received from @userinfobot

5) Save the file as ".env" in the same folder where it is located
bot.py IMPORTANT: when saving, select "File type: All files (*.*)" and enter the file name exactly as ".env"

2.3. INSTALLING DEPENDENCIES:

1) Click the Start button, type "cmd" and press Enter

2) In the command prompt that opens, enter the commands:
   cd %USERPROFILE%\Desktop\TelegramBot
   pip install aiogram==3.2.0 python-dotenv

3) Wait for the installation to complete

2.4. LAUNCHING THE BOT:

1) In the same command prompt, type:
   python bot.py

2) If everything is done correctly, you will see a message about the launch of the bot.
   The bot will work while the command prompt window is open.

3) To stop the bot, press Ctrl+C in the command prompt window

======================================
3. INSTALLATION ON LINUX
======================================

3.1. INSTALLING PYTHON:

1) Open a terminal (usually a keyboard shortcut Ctrl+Alt+T)

2) Enter the following commands one at a time:
   sudo apt update
   sudo apt install python3.10 python3-pip python3.10-venv

3.2. DOWNLOADING AND CONFIGURING THE BOT:

1) Create a folder for the bot with the command:
   mkdir ~/telegram_bot
   cd ~/telegram_bot

2) Create a file with the bot code:
   nano bot.py

3) Paste the bot code into the editor that opens

4) Press Ctrl+O, then Enter to save, then Ctrl+X to exit

5) Create an environment file:
   nano .env

6) Write in the file:
   BOT_TOKEN=your_token_bot
   ADMIN_CHAT_ID=your_id_chata

   Replace "your_token_bot" with the token received from BotFather
   Replace "your_id_chata" with the ID received from @userinfobot

7) Press Ctrl+O, then Enter to save, then Ctrl+X to exit

3.3. CREATING A VIRTUAL ENVIRONMENT AND INSTALLING DEPENDENCIES:

1) Create a virtual environment:
   python3 -m venv venv

2) Activate the virtual environment:
   source venv/bin/activate

3) Install dependencies:
   pip install aiogram==3.2.0 python-dotenv

3.4. LAUNCHING THE BOT:

1) If the virtual environment is active (there will be "(venv)" at the beginning of the line), enter:
   python3 bot.py

2) If you have closed the terminal, then you need to start the bot.:
   cd ~/telegram_bot
   source venv/bin/activate
   python3 bot.py

3) To stop the bot, press Ctrl+C in the terminal

======================================
4. USING A BOT
======================================

1) Find your Telegram bot by the username that you specified when creating it

2) Send the /start command to start filling out the form

3) Follow the instructions of the bot to fill out the form

4) If you need to cancel the filling, send the command /cancel

5) After confirming the application, the data will be sent to the account of the administrator (you)

======================================
5. POSSIBLE PROBLEMS AND THEIR SOLUTIONS
======================================

PROBLEM: "There is no such file or directory"
SOLUTION: Make sure you are in the correct folder. Use the cd command to navigate to the desired folder.

PROBLEM: "ModuleNotFoundError: No module named 'aiogram'"
SOLUTION: Restart dependency installation: pip install aiogram==3.2.0 python-dotenv

PROBLEM: "The file cannot be saved.env"
SOLUTION: In Windows, make sure that when saving, select "File Type: All files (*.*)"

PROBLEM: "The bot is not responding to messages"
SOLUTION: Make sure that in the file .env is the correct bot token.

PROBLEM: "The admin is not receiving applications"
decision: Check the correct ADMIN_CHAT_ID in the .env file
