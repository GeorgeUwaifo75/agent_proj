import os
import streamlit as st

from dotenv import load_dotenv
from transformers import tool
from transformers import CodeAgent, HfApiEngine

@tool
def model_download_tool(task: str) -> str:
    """
    This is a tool that returns the most downloaded model of a given task on the Hugging Face Hub.
    It returns the name of the checkpoint.

    Args:
        task: The task for which
    """
    model = next(iter(list_models(filter="text-classification", sort="downloads", direction=-1)))
    return model.id


def main():
  load_dotenv()
  api_key = os.getenv('HF_TOKEN')
  if api_key:
      st.write(f"API Key loaded (but not shown): *******")
  else:
      st.write("API Key not loaded! Ensure you have a '.env' file with API_KEY set.")
  st.title('The Agent test')


  

llm_engine = HfApiEngine(model="https://huggingface.co/inference-endpoints")
agent = CodeAgent(tools=[], llm_engine=llm_engine, add_base_tools=True)

#agent = CodeAgent(tools=[model_download_tool], llm_engine=llm_engine)
agent.run(
"Can you give me the name of the model that has the most downloads in the 'text-to-video' task on the Hugging Face Hub?"
)

if __name__ == '__main__':
    main()
