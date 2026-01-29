# Fast Prototyping of a GenAI App with Streamlit

This repository contains the projects developed during the **DeepLearning.AI** course: *"Fast Prototyping of GenAI Apps with Streamlit"*. The goal of this project is to demonstrate the evolution from a basic data processing tool to a fully integrated AI-powered data assistant (using the Avalanche dataset).

## 🚀 Project Overview

The project is divided into two main stages of development, showcasing how to build, scale, and integrate LLMs into data applications.

### 📁 [01-GenAi-Data-Ingestion-and-Cleaning] GenAI-Data Ingestion & Cleaning App
This module focuses on the fundamentals of Streamlit and local data handling.
* **Key Features:** CSV data ingestion, automated text cleaning using Regex, and interactive data visualization (Bar Charts).
* **Tech Stack:** Streamlit, Pandas, Python (Regex).
* **Learning Goal:** Understanding state management (`st.session_state`) and building a responsive UI layout.

GenAI-Data Ingestion & Cleaning App/GenAI- Dashboard.png


### 📁 [02-GenAi-Data-Assistant] GenAI-Data_Assistant_App
The final stage of the application, transforming the prototype into a cloud-native AI assistant.
* **Key Features:**
    * **Snowflake Integration:** Direct connection to cloud data warehouses.
    * **Cortex AI:** Leveraging the `claude-3-5-sonnet` model directly within Snowflake for high-performance inference.
    * **Natural Language Querying:** A chatbot interface that allows users to ask questions about their data in plain English.
* **Tech Stack:** Streamlit, Snowflake (Snowpark & Cortex), Matplotlib, Claude 3.5 Sonnet.
* **Learning Goal:** Implementing RAG (Retrieval-Augmented Generation) patterns and deploying enterprise-grade GenAI apps.

GenAI-Data_Assistant_App/Avalanche_App-Data-Assistant.png


### 📁 [03-GenAi-Advanced-Rag-and-Chatbot] GenAI-Advanced_RAG_Chatbot
The advanced stage focusing on enterprise-grade features and RAG architecture.
* **Key Features:**
    * **Cortex Search:** Implementation of a RAG pipeline with semantic search.
    * **Advanced UI:** Multi-tab interface for data exploration and AI interaction.
    * **Chat History:** Persistent conversation memory using `st.session_state`.
    * **Model Selection:** Support for multiple LLMs (Claude 3.5, Mistral, Llama 3).
* **Tech Stack:** Snowflake Cortex Search, Streamlit Tabs & Chat Elements.

#### App Interace from Folder 03
![Streamlit Snowflake Dashboard](GenAI-Advanced_RAG_Chatbot/GenAI-RAG chatbot 1/assets/deploy-to-streamlit-in-snowflake-2.png)
![Streamlit Snowflake Dashboard](GenAI-Advanced_RAG_Chatbot/GenAI-RAG chatbot 2/assets/Integrating RAG Chatbot with Data.png)
---

## 🛠️ Setup & Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Cooldude1301/fast-prototyping-of-genai-apps-with-streamlit] or [https://github.com/Cooldude1301/Avalanche_Sentilytics]
    ```

2.  **Install Dependencies:**
    Each folder contains its specific logic. Ensure you have the necessary libraries installed:
    ```bash
    pip install streamlit pandas snowflake-snowpark-python matplotlib
    ```

3.  **Snowflake Configuration:**
    For the Data Assistant, ensure your `.streamlit/secrets.toml` is configured with your Snowflake credentials (do not commit this file to GitHub!).

---
*Disclaimer: This project was built as part of the DeepLearning.AI course curriculum.*
