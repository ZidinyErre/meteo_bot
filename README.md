# meteo_bot
This script scrap the information from a french meteo service 
and send the information we need in the terminal and you're mail adress. 

## Prerequisites
- Python 3.10+
- Google Chrome
-  GitHub account 

## setup

Clone the repository:
```bash
git clone https://github.com/your-username/your-project.git
cd your-project
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows

pip install -r requirements.txt
```
## Usage

Run the script:
```bash
python index.py
``` 

## last information 

I use smtp protocol to send the mail and also gitignore and a .env file to hide
sensitive information. 
I also use app security key of my google account , that's why i stop the project because i don't like 
to play with my mail account.
All the variables appear in the terminal and in the mail but the two functions i create doesn't appear in mail part. 

