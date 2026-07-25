import streamlit as st
from groq import Groq
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Finance RAG Chatbot",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------

st.title("📊 Finance RAG Chatbot")
st.write("Ask questions about Apple, Amazon, Google, NVIDIA, and Tesla annual reports.")

# -----------------------------
# Load Embedding Model
# -----------------------------

@st.cache_resource
def load_embedding():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

embedding_model = load_embedding()

# -----------------------------
# Load FAISS Database
# -----------------------------

@st.cache_resource
def load_vector_db():
    return FAISS.load_local(
        "vector_db",
        embedding_model,
        allow_dangerous_deserialization=True
    )

vector_db = load_vector_db()

# -----------------------------
# Groq Client
# -----------------------------

client = Groq(
    api_key="YOUR_GROQ_API_KEY"
)

# -----------------------------
# Chat History
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------------
# User Input
# -----------------------------

question = st.chat_input("Ask a financial question...")

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Retrieve relevant documents
    docs = vector_db.similarity_search(question, k=5)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    prompt = f"""
You are a financial analyst.

Answer ONLY using the following context.

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "Answer only from the provided financial reports."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    answer = response.choices[0].message.content

    # Assistant response
    with st.chat_message("assistant"):
        st.markdown(answer)

        st.markdown("### 📚 Sources")

        shown = set()

        for doc in docs:

            source = doc.metadata.get("source", "Unknown")
            page = doc.metadata.get("page", 0)

            filename = source.split("\\")[-1]

            if (filename, page) not in shown:
                st.write(f"• {filename} (Page {page+1})")
                shown.add((filename, page))

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )