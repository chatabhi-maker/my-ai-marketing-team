import streamlit as st
from google import genai

# 1. Set up the web page title and icon
st.set_page_config(page_title="Abhinav's AI Agent Team", page_icon="🚀")

st.title("🕵️‍♂️ Multi-Agent Marketing Team")
st.write("Type a topic below. Watch the Researcher and Copywriter work together to build a LinkedIn post!")

# 2. Add an input box for the user on the web page
topic_input = st.text_input("Enter your content topic:", "Why non-tech professionals should learn AI")

# 3. Securely fetch your new AQ. key from your secrets manager box
try:
    RAW_KEY = st.secrets["GOOGLE_API_KEY"]
    MY_KEY = RAW_KEY.strip() if RAW_KEY else ""
except Exception:
    MY_KEY = ""

if st.button("Generate Post 🚀"):
    if not MY_KEY:
        st.error("❌ Setup Error: 'GOOGLE_API_KEY' was not found in your Streamlit Advanced Settings secrets box!")
    else:
        try:
            # Connect using the modern client orchestration layer
            client = genai.Client(api_key=MY_KEY)
            
            # --- AGENT 1: RESEARCH ---
            with st.spinner("🕵️‍♂️ Agent 1 (Researcher) is gathering data..."):
                chat_researcher = client.chats.create(
                    model="gemini-3.6-flash",  # 🔄 Updated to the active 3.6 model wrapper,
                    config={"system_instruction": "You are a precise data researcher. Provide exactly 3 highly detailed facts about the topic."}
                )
                research_response = chat_researcher.send_message(f"Research this topic: {topic_input}")
                raw_research = research_response.text
            
            st.success("✅ Research Complete!")
            with st.expander("See Raw Research Notes"):
                st.write(raw_research)
                
            # --- AGENT 2: COPYWRITING ---
            with st.spinner("✍️ Agent 2 (Copywriter) is crafting the post..."):
                chat_writer = client.chats.create(
                   model="gemini-3.6-flash",  # 🔄 Updated to the active 3.6 model wrapper,
                    config={"system_instruction": "You are a professional LinkedIn marketer. Create a high-energy post based on raw data."}
                )
                writer_response = chat_writer.send_message(f"Convert this research into a top-tier LinkedIn post:\n\n{raw_research}")
                final_post = writer_response.text
                
            st.success("🎉 Final Post Ready!")
            st.text_area("Copy your LinkedIn Post here:", value=final_post, height=300)
            
        except Exception as e:
            st.error(f"❌ Connection Failed: {e}")
