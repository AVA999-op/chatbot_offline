# Offline Chatbot

A simple offline chatbot built with Python, Streamlit, and Ollama. The application provides an interactive chat interface and uses a locally running language model to generate responses.

The project demonstrates how to integrate a local large language model (LLM) into a Python application without relying on a cloud-based AI API.

## Features

- Interactive chat interface built with Streamlit
- Local language model integration using Ollama
- Conversation history maintained during the current session
- AI-generated responses using the Qwen 2.5 Coder 7B model
- Local inference without sending prompts to a cloud-based AI API

## Technologies Used

- Python
- Streamlit
- Requests
- Ollama
- Qwen 2.5 Coder 7B

## Requirements

- Python 3.9 or a compatible version supported by the installed dependencies
- Ollama installed and running on your machine
- The `qwen2.5-coder:7b` model downloaded locally

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/AVA999-op/chatbot_offline.git
cd chatbot_offline
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment.

Windows:

```bash
venv\Scripts\activate
```

Linux and macOS:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Ollama

Install Ollama and download the required model:

```bash
ollama pull qwen2.5-coder:7b
```

Make sure Ollama is running locally and available at:

```text
http://localhost:11434
```

### 5. Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to interact with the chatbot.

## Project Structure

```text
chatbot_offline/
├── app.py
├── utils.py
├── requirements.txt
└── README.md
```

- `app.py`: Implements the Streamlit chat interface and manages conversation history.
- `utils.py`: Sends prompts to the local Ollama API and retrieves generated responses.
- `requirements.txt`: Lists the required Python packages.
- `README.md`: Provides project documentation and setup instructions.

## How It Works

1. The user enters a message through the Streamlit chat interface.
2. The application stores the message in the current session history.
3. The prompt is sent to the locally running Ollama service.
4. The selected language model generates a response.
5. The response is displayed in the chat interface and added to the session history.

## Privacy and Offline Usage

Once Ollama and the required model are installed, the chatbot can generate responses locally without depending on a cloud-based AI API. An internet connection may be required for the initial installation and model download.

## Future Improvements

- Add configurable model selection.
- Improve error handling when Ollama is unavailable.
- Add a conversation reset option.
- Support persistent conversation history.
- Improve prompt formatting and response generation.
- Add configurable model parameters.

## Author

AVA999-op

GitHub: [@AVA999-op](https://github.com/AVA999-op)

## License

No license is specified in this README. Please check the repository for an existing license before reusing or distributing the code.
