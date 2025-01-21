import os
import streamlit as st

from dotenv import load_dotenv



def main():
  load_dotenv()
  api_key = os.getenv('HF_TOKEN')
      if api_key:
          st.write(f"API Key loaded (but not shown): *******")
      else:
          st.write("API Key not loaded! Ensure you have a '.env' file with API_KEY set.")
  st.title('The Agent test')

if __name__ == '__main__':
    main()
