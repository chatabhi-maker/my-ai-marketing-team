import streamlit as st
import google.generativeai as genai

# Set up the web page title and icon
st.set_page_config(page_title="Abhinav's AI Agent Team", page_icon="🚀")

st.title("🕵️‍♂️ Multi-Agent Marketing Team")
st.write("Type a topic below. Watch the Researcher and Copywriter work together to build a LinkedIn post!")

# Add an input box for the user on the web page
topic_input = st.text_input("Enter your content topic:", "Why non-tech professionals should learn AI")

# 🔑 PASTE YOUR ACTUAL AIzaSy... KEY DIRECTLY INSIDE THESE QUOTES
MY_KEY = "AIzaSyAQ.Ab8RN6IImWb6Gb3LyoGZuZqC4BttA01vl7MtJH8EWu53rgnWrw"

if st.button("Generate Post 🚀"):
    if not MY_KEY or MY_KEY == "AIzaSyYOUR_REAL_GOOGLE_KEY_HERE":
        st.error("Please add your valid Google API key to line 14 inside the quotes!")
    else:
        try:
            # Configure the global connection using the stable library wrapper
            genai.configure(api_key=MY_KEY)
            
            # 🔄 CRITICAL FIX: Updated to the correct active model address for this library
            model = genai.GenerativeModel("models/gemini-2.5-flash")
            
            # --- AGENT 1: RESEARCH ---
            with st.spinner("🕵️‍♂️ Agent 1 (Researcher) is gathering data..."):
                research_response = model.generate_content(
                    f"You are a precise data researcher. Provide exactly 3 highly detailed facts about the topic: {topic_input}"
                )
                raw_research = research_response.text
            
            st.success("✅ Research Complete!")
            with st.expander("See Raw Research Notes"):
                st.write(raw_research)
                
            # --- AGENT 2: COPYWRITING ---
            with st.spinner("✍️ Agent 2 (Copywriter) is crafting the post..."):
                writer_response = model.generate_content(
                    f"You are a professional LinkedIn marketer. Create a high-energy, engaging post based on this raw data:\n\n{raw_research}"
                )
                final_post = writer_response.text
                
            st.success("🎉 Final Post Ready!")
            st.text_area("Copy your LinkedIn Post here:", value=final_post, height=300)
            
        except Exception as e:
            st.error(f"❌ Execution Error: {e}")
