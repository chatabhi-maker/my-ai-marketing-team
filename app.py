import sys
sys.path.insert(0, '/home/adminuser/venv/lib/python3.14/site-packages')

import streamlit as st
from google import genai

# ... (rest of your working code remains exactly the same)

# Set up the web page title and icon
st.set_page_config(page_title="Abhinav's AI Agent Team", page_icon="🚀")

st.title("🕵️‍♂️ Multi-Agent Marketing Team")
st.write("Type a topic below. Watch the Researcher and Copywriter work together to build a LinkedIn post!")

# Add an input box for the user on the web page
topic_input = st.text_input("Enter your content topic:", "Why non-tech professionals should learn AI")

# Paste your working Google AI Studio Key here!
MY_KEY = st.secrets["GOOGLE_API_KEY"] 

if st.button("Generate Post 🚀"):
    if not MY_KEY or MY_KEY == "AIzaSy...":
        st.error("Please add your valid Google API key to line 13 in the code!")
    else:
        client = genai.Client(api_key=MY_KEY)
        
        # --- AGENT 1: RESEARCH ---
        with st.spinner("🕵️‍♂️ Agent 1 (Researcher) is gathering data..."):
            researcher_chat = client.chats.create(
                model="gemini-3.5-flash-lite",  # 🔄 Swapped to high-limit lite model
                config={"system_instruction": "You are a precise data researcher. Provide exactly 3 highly detailed facts about the topic."}
            )
            research_response = researcher_chat.send_message(f"Research this topic: {topic_input}")
            raw_research = research_response.text
        
        st.success("✅ Research Complete!")
        with st.expander("See Raw Research Notes"):
            st.write(raw_research)
            
        # --- AGENT 2: COPYWRITING ---
        with st.spinner("✍️ Agent 2 (Copywriter) is crafting the post..."):
            writer_chat = client.chats.create(
                model="gemini-3.5-flash-lite",  # 🔄 Swapped to high-limit lite model
                config={"system_instruction": "You are a professional LinkedIn marketer. Create a high-energy post based on raw data."}
            )
            writer_response = writer_chat.send_message(f"Convert this research into a top-tier LinkedIn post:\n\n{raw_research}")
            final_post = writer_response.text
            
        st.success("🎉 Final Post Ready!")
        st.text_area("Copy your LinkedIn Post here:", value=final_post, height=300)
