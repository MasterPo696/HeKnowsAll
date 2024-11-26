# README

## Description

This project is a Telegram bot designed to help users solve school curriculum tasks using the AI21 model. The bot provides answers in three styles: short, medium, and detailed. It is implemented using `aiogram` for message and command handling and `langchain_ai21` for interaction with the language model.

---

## Requirements

- **Python**: Version 3.9 or higher
- **Dependencies**:
  - `aiogram`
  - `langchain_ai21`
  - `langchain_core`
  - `datetime`
  - `random`

---

## Installation

1. **Clone the repository or download the files:**
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Create a virtual environment:**
   ```bash
   python3.9 -m venv venv
   source venv/bin/activate   # For Linux/MacOS
   venv\Scripts\activate      # For Windows
   ```

3. **Upgrade `pip` and install dependencies:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Create a file named `app/config.py` and add your bot token:
   ```python
   TOKEN = "Your_Bot_Token"
   ```

5. **Run the bot:**
   ```bash
   python bot.py
   ```

---

## Project Structure

- **`bot.py`**: The main file containing the bot's logic.
- **`app/config.py`**: Configuration file for storing the bot's token.
- **`texts.py`**: Contains text data, such as sticker sets.
- **`app/kb.py`**: Keyboard layouts for user interactions.

---

## Main Features

- **Command `/start`**: Initiates interaction with the bot. The user receives a welcome message and options to proceed.
- **Question Handling**: Users can ask a question, select the type of answer (`short`, `medium`, `long`), and the bot will generate a response using AI21.
- **Sticker Interaction**: The bot sends random stickers to create a friendly atmosphere.
- **State Management**: FSM (`aiogram.fsm`) is used to track the current dialogue state.

---

## Setting Up AI21

1. Register at [AI21 Studio](https://www.ai21.com/studio) and obtain an API key.
2. Add the API key to the code:
   ```python
   API_KEY = 'Your_API_Key'
   ```

---

## Dependencies

Example `requirements.txt` file content:

```
aiogram==3.x
langchain-ai21
langchain-core
python-dotenv
```

---

## Notes

- **Payment Timeout**: The code includes a placeholder for handling payment timeout, which is set to `10` seconds (adjustable in the `PAYMENT_TIMEOUT` variable). 
- **Error Handling**: Ensure proper error handling for API calls and user interactions to maintain a smooth experience.