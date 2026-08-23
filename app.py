import streamlit as st
import google.generativeai as genai

# Set up the web page title and icon
st.set_page_config(page_title="Abhinav's AI Agent Team", page_icon="🚀")

st.title("🕵️‍♂️ Multi-Agent Marketing Team")
st.write("Type a topic below. Watch the Researcher and Copywriter work together to build a LinkedIn post!")

# Add an input box for the user on the web page
topic_input = st.text_input("Enter your content topic:", "Why non-tech professionals should learn AI")

# Securely grab the API key from your Streamlit Advanced Settings vault
try:
    RAW_KEY = st.secrets["GOOGLE_API_KEY"]
    
    # 🔄 CRITICAL CLOUD FIX: Strips out hidden outer quotation marks (" or ') 
    # that Streamlit Cloud accidentally glues into the key text string!
    MY_KEY = RAW_KEY.strip().replace('"', '').replace("'", "") if RAW_KEY else ""
except Exception:
    MY_KEY = ""

if st.button("Generate Post 🚀"):
    if not MY_KEY:
        st.error("❌ Setup Error: 'GOOGLE_API_KEY' was not found in your Streamlit Advanced Settings secrets box!")
    elif not MY_KEY.startswith("AIzaSy"):
        st.error(f"❌ Key Type Error: Your key starts with '{MY_KEY[:6]}' but must start with 'AIzaSy'. Please verify your Google API key string.")
    else:
        try:
            # Configure the global connection using the stable library wrapper
            genai.configure(api_key=MY_KEY)
            
            # Using the stable active model parameter layout
            model = genai.GenerativeModel("models/gemini-1.5-flash")
            
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
