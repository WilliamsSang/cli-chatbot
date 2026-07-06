# CLI ChatBot

A simple command-line AI chatbot built with Python and the OpenAI API.

## Features

- Chat with OpenAI models
- Conversation memory
- System prompt
- Automatic history trimming
- Save chat history to JSON
- Load previous conversations
- Object-oriented design

## Tech Stack

- Python
- OpenAI API
- JSON
- Git

## Project Structure

cli-chatbot/
├── main.py
├── README.md
├── .gitignore
├── .env
└── history.json

## Installation

```bash
pip install openai python-dotenv
```

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key
```

Run:

```bash
python3 main.py
```

## Current Version

v1.0.0

## Roadmap

### v1
- OpenAI Chat
- Conversation Memory
- JSON Storage
- Object-Oriented Refactor

### v2
- Weather API
- Tool Calling
- FastAPI

### v3
- Web UI
- Streaming Response
- Markdown Rendering

## Author

Boyuan Sang
McGill University
