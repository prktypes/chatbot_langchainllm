# 🤖 Offline ChatBot using LangChain, Hugging Face, and Streamlit

A privacy-first, fully local conversational AI assistant built using **LangChain**, **Hugging Face Transformers**, and **Streamlit**. This lightweight application leverages the **DialoGPT-medium** model for natural language generation and employs **LangChain's ConversationBufferMemory** to maintain contextual continuity in dialogue. Designed for offline use, the chatbot executes all inference locally, ensuring data privacy and zero API dependency after setup.

---

## 🚀 Key Features

- 🧠 **Transformer-based Language Modeling**: Utilizes `microsoft/DialoGPT-medium`, a pre-trained causal language model from Hugging Face for realistic, turn-based dialogue generation.
- 🧩 **LangChain Integration**: Implements `ConversationChain` and `ConversationBufferMemory` to enable persistent conversational context, mimicking multi-turn dialogue systems.
- ⚡ **Streamlit-Powered Frontend**: Rapid deployment of an interactive and responsive UI using Streamlit's reactive components and form-handling APIs.
- 🔐 **Offline and Private**: The entire pipeline runs locally; no external calls are made, protecting sensitive inputs and user data.
- 🔁 **Session State Management**: Streamlit's `session_state` is used for tracking user input and maintaining chat history.
- 🛠️ **Modular Python Architecture**: Separation of concerns between model setup, memory handling, and UI rendering for clean code structure and maintainability.

---

## 🖥️ Skills Demonstrated

> ✅ These are some of the real-world AI/ML and software development skills applied in this project:

- 🔄 **LangChain Chains & Memory Management**
- 🧠 **LLM Deployment using Hugging Face Transformers**
- 📦 **NLP Pipeline Creation using `transformers.pipeline`**
- ⚙️ **Stateful App Design with `streamlit.session_state`**
- 🖼️ **Frontend Integration for NLP Apps via Streamlit**
- 📚 **Prompt Engineering and Chat History Management**
- 🔌 **Environment Variable Handling and GitHub Secret Protection**
- 🛡️ **Privacy-focused Offline Model Deployment**

---

## 📸 UI Preview

![chatbot](https://github.com/user-attachments/assets/f2f26359-7ca1-4857-b7c1-58860756a402)
_Compact, browser-based UI with contextual multi-turn dialogue support._

---

## 🛠️ Local Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/offline-langchain-chatbot.git
cd offline-langchain-chatbot
