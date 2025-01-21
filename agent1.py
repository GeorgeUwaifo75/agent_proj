import os
import streamlit as st

from dotenv import load_dotenv

from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel


def main():
  load_dotenv()
  api_key = os.getenv('HF_TOKEN')
  if api_key:
      st.write(f"API Key loaded (but not shown): *******")
  else:
      st.write("API Key not loaded! Ensure you have a '.env' file with API_KEY set.")
  st.title('The Agent test')


  agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=HfApiModel())

  agent.run("How can I travel from Nigeria to Mexico transiting in Europe, and give me the cheapest round trip ticket in March?")

if __name__ == '__main__':
    main()
