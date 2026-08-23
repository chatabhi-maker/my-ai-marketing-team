import streamlit as st
import google.generativeai as genai

# Set up the web page title and icon
st.set_page_config(page_title="Abhinav's AI Agent Team", page_icon="🚀")

st.title("🕵️‍♂️ Multi-Agent Marketing Team")
st.write("Type a topic below. Watch the Researcher and Copywriter work together to build a LinkedIn post!")

# Add an input box for the user on the web page
topic_input = st.text_input("Enter your content topic:", "Why non-tech professionals should learn AI")

# 🔑 CRITICAL KEY STEP: Clean and parse the password input text string
RAW_KEY = "AIzaSyAQ.Ab8RN6JUkvsI3lp3oOrIXYMraCF0c1Zb754S-SCwgzhD8Hying"

# Automatically strips hidden spaces or newline gaps that break validation checkpoints
MY_KEY = RAW_KEY.strip() if RAW_KEY else ""

if st.button("Generate Post 🚀"):
    if not MY_KEY or "YOUR_REAL_GOOGLE_KEY_HERE" in MY_KEY:
        st.error("❌ Setup Error: Please replace the placeholder text on line 14 with your actual Google API key!")
    elif not MY_KEY.startswith("AIzaSy"):
        st.error("❌ Key Type Error: This doesn't look like a Google API key. Google keys must start with 'AIzaSy'. Please verify your string.")
    else:
        try:
            # Configure the global server connection wrapper
            genai.configure(api_key=MY_KEY)
            
            # Utilizing the modern, universally active stable production model endpoints
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
            st.error(f"❌ Connection or Key Validation Failed: {e}")
            st.info("💡 Troubleshooting Tip: If you still see a 400 error here, head to aistudio.google.com, delete your old key, create a fresh one, and replace line 14.")
