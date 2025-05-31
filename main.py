import streamlit as st
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
from langchain.llms import HuggingFacePipeline
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# --- Must be the first Streamlit command ---
st.set_page_config(page_title="Offline ChatBot", page_icon="🤖")

# --- Sidebar Info ---
st.sidebar.title("🤖 LangChain LLM Chatbot")
st.sidebar.markdown(
    """
    - **Model:** GPT-2 (local)
    - **Framework:** LangChain + HuggingFace
    - **Usage:** Type your message and press Enter.
    - **Clear Chat:** Use the button below to reset.
    """
)
if st.sidebar.button("Clear Chat"):
    st.session_state["chat_history"] = []
    if "memory" in st.session_state:
        st.session_state["memory"].clear()

# --- Model Setup ---
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=150,
    temperature=0.7,
    do_sample=True
)
local_llm = HuggingFacePipeline(pipeline=pipe)

# --- Memory & Conversation ---
if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(memory_key="history")
memory = st.session_state["memory"]

conversation = ConversationChain(
    llm=local_llm,
    memory=memory,
    verbose=False
)

# --- Main UI ---
st.title("💬 Offline ChatBot")
st.markdown(
    "<style>div[data-testid='stChatMessage']{margin-bottom:8px;} .user-bubble{background:#DCF8C6;padding:10px;border-radius:10px 10px 0 10px;display:inline-block;} .bot-bubble{background:#F1F0F0;padding:10px;border-radius:10px 10px 10px 0;display:inline-block;}</style>",
    unsafe_allow_html=True,
)

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# --- Chat Input ---
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message...", key="user_input", placeholder="Say hello!")
    submitted = st.form_submit_button("Send")

if submitted and user_input.strip():
    response = conversation.predict(input=user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response.strip()))

# --- Chat Display ---
st.markdown("---")
for speaker, message in st.session_state["chat_history"]:
    if speaker == "You":
        st.markdown(
            f"<div class='user-bubble'><b>{speaker}:</b> {message}</div>",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"<div class='bot-bubble'><b>{speaker}:</b> {message}</div>",
            unsafe_allow_html=True,
        )
