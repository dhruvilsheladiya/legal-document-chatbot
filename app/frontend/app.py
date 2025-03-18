import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/upload/"

st.title("📜 Legal Document Chatbot")

uploaded_file = st.file_uploader("Upload a legal document (PDF)", type=["pdf"])

if uploaded_file is not None:
    with st.spinner("Processing..."):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post(API_URL, files=files)

        if response.status_code == 200:
            try:
                data = response.json()

                # Ensure 'summary' is available
                if "summary" in data:
                    st.subheader("🔍 Summary")
                    st.write(data["summary"])
                else:
                    st.error("Summary not found in response.")

                # Handle 'entities' properly
                if "entities" in data and isinstance(data["entities"], dict):
                    st.subheader("📌 Extracted Entities")
                    for entity, value in data["entities"].items():
                        st.write(f"**{entity}**: {value}")
                elif "entities" in data and isinstance(data["entities"], list):
                    st.subheader("📌 Extracted Entities")
                    for item in data["entities"]:
                        st.write(f"- {item}")
                else:
                    st.warning("No entities found.")
            
            except Exception as e:
                st.error(f"❌ Error processing response: {e}")
        else:
            st.error("❌ API error. Please try again.")
