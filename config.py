import streamlit as st

def setup_page():
    st.set_page_config(
        page_title="Aura Campus — Bienestar, Aprendizaje & Creatividad",
        page_icon="🌿",
        layout="wide"
    )
    
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');

        html, body, [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #fbfb2f3 0%, #f4f7f4 50%, #f2eff7 100%) !important;
            font-family: 'Plus Jakarta Sans', sans-serif;
            color: #2c3e35;
        }

        [data-testid="stSidebar"] {
            background-color: #f7f9f7 !important;
            border-right: 1px solid #e1e8e3;
        }

        h1, h2, h3 {
            color: #2d3748 !important;
            font-weight: 700 !important;
        }
        
        .main-header {
            font-size: 2.2rem;
            color: #2e4a3e;
            font-weight: 700;
            background: linear-gradient(120deg, #e8f5e9 0%, #f3e8ff 100%);
            padding: 1.5rem 2rem;
            border-radius: 20px;
            margin-bottom: 1.5rem;
            border: 1px solid #d8ebd9;
            box-shadow: 0 4px 20px rgba(0,0,0,0.03);
            text-align: center;
        }

        button[data-baseweb="tab"] {
            background-color: transparent !important;
            border-radius: 12px !important;
            padding: 10px 18px !important;
            font-weight: 600 !important;
            color: #526058 !important;
        }

        button[data-baseweb="tab"][aria-selected="true"] {
            background-color: #ffffff !important;
            color: #2e7d32 !important;
            box-shadow: 0 3px 10px rgba(0,0,0,0.05) !important;
        }

        .stTextArea textarea, .stTextInput input, .stSelectbox select {
            background-color: #ffffff !important;
            border: 1px solid #ccd7ce !important;
            border-radius: 14px !important;
        }

        .stButton button {
            border-radius: 14px !important;
            background-color: #e8f5e9 !important;
            color: #1b5e20 !important;
            font-weight: 600 !important;
            border: 1px solid #c8e6c9 !important;
            padding: 0.6rem 1.4rem !important;
        }

        .stButton button:hover {
            background-color: #c8e6c9 !important;
            color: #0b3d11 !important;
        }

        #MainMenu, footer, header {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)
