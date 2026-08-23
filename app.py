import os
import sys
import subprocess

# 🚀 FORCE CLOUD INSTALLATION OF THE MISSION-CRITICAL PACKAGES LIVE
try:
    import google.generativeai as genai
except ModuleNotFoundError:
    print("📦 Library missing! Forcing server installation of google-generativeai...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "google-generativeai"])
    import google.generativeai as genai

import streamlit as st

# --- REST OF YOUR WORKING CODE CONTINUES EXACTLY THE SAME ---

st.set_page_config(page_title="Abhinav's AI Agent Team", page_icon="🚀")

st.title("🕵️‍♂️ Multi-Agent Marketing Team")
st.write("Type a topic below. Watch the Researcher and Copywriter work together to build a LinkedIn post!")

topic_input = st.text_input("Enter your content topic:", "Why non-tech professionals should learn AI")

MY_KEY = st.secrets["GOOGLE_API_KEY"]

if st.button("Generate Post 🚀"):
    if not MY_KEY:
        st.error("Please add your valid Google API key to Streamlit Advanced Settings!")
    else:
        genai.configure(api_key=MY_KEY)
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        with st.spinner("🕵️‍♂️ Agent 1 (Researcher) is gathering data..."):
            research_response = model.generate_content(
                f"You are a precise data researcher. Provide exactly 3 highly detailed facts about the topic: {topic_input}"
            )
            raw_research = research_response.text
        
        st.success("✅ Research Complete!")
        with st.expander("See Raw Research Notes"):
            st.write(raw_research)
            
        with st.spinner("✍️ Agent 2 (Copywriter) is crafting the post..."):
            writer_response = model.generate_content(
                f"You are a professional LinkedIn marketer. Create a high-energy, engaging post based on this raw data:\n\n{raw_research}"
            )
            final_post = writer_response.text
            
        st.success("🎉 Final Post Ready!")
        st.text_area("Copy your LinkedIn Post here:", value=final_post, height=300)
