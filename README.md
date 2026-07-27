# 📊 Finance RAG Chatbot

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://finance-rag-chatbot-nupur32.streamlit.app/)

An interactive **Retrieval-Augmented Generation (RAG)** chatbot built with **Streamlit**, **LangChain**, **FAISS**, and **Groq Cloud API** (running Llama-3.1-8b-instant). It allows users to ask financial questions and retrieve precise answers sourced directly from the annual reports of **Apple, Amazon, Google, NVIDIA, and Tesla**.

---

## 🚀 Live Demo
Access the live application directly on Streamlit Community Cloud:
👉 **[finance-rag-chatbot-nupur32.streamlit.app](https://finance-rag-chatbot-nupur32.streamlit.app/)**

---

## 🛠️ Features
- **Retrieval-Augmented Generation (RAG):** Combines the generation capabilities of Large Language Models (LLMs) with document retrieval.
- **Accurate Grounding:** Restricts model responses strictly to the facts provided in the official financial documents.
- **Source Citation:** Automatically lists the source documents and page numbers where the information was found.
- **Vector Database:** Uses **FAISS** with `sentence-transformers/all-MiniLM-L6-v2` embeddings for fast semantic lookup.
- **Groq LLM Acceleration:** Leverages **Llama-3.1-8b-instant** on Groq for ultra-fast response times.

---

## 💻 Local Setup & Execution

### 1. Clone the Repository
```bash
git clone https://github.com/NUPUR32/Finance-RAG-Chatbot.git
cd Finance-RAG-Chatbot
```

### 2. Install Dependencies
Ensure you have Python 3.8+ installed. Install the required Python packages:
```bash
pip install -r requirements.txt
```

### 3. Configure API Key
Create a `.env` file in the root directory (using `.env.example` as a template):
```env
GROQ_API_KEY=your_actual_groq_api_key_here
```
Or export it as an environment variable in your terminal:
- **Windows (PowerShell):** `$env:GROQ_API_KEY="your_key"`
- **Linux/macOS:** `export GROQ_API_KEY="your_key"`

### 4. Run the Streamlit Application
```bash
streamlit run app.py
```

---

## ☁️ Deploying to Streamlit Community Cloud

To deploy this app yourself:
1. Fork this repository to your GitHub account.
2. Go to [share.streamlit.io](https://share.streamlit.io/) and log in with GitHub.
3. Click **New app**, select your repository, branch (`main`), and main file path (`app.py`).
4. In **Advanced Settings**, add your `GROQ_API_KEY` under the secrets section:
   ```toml
   GROQ_API_KEY = "your_actual_groq_api_key_here"
   ```
5. Click **Deploy**!