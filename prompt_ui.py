from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from pydantic import SecretStr
import os
from langchain_core.prompts import PromptTemplate


load_dotenv()

st.header('Research Tool')

paper_input = st.selectbox("Select Research Paper Name", ["Select..", "Attention is all you need", "bert: Pre-traning of deep bidirectional transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GAN's on Image Synthesis"])

style_input = st.selectbox("Select Explanation Style",["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])

lenght_input = st.selectbox("Select Explanation Length", ["Short (1-2 paragraph)", "Medium(3-5 paragraph)", "Long(detailed explanaiton)"])

model = ChatOpenAI(model="default", api_key=SecretStr(os.environ["LLM7_API_KEY"]), base_url="https://api.llm7.io/v1")

# template
template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:
explanation style: {style_input}
explanation length: {lenght_input}
""",
input_variables=['paper_input', 'style_input', 'lenght_input']
)


# fill the placeholders
user_input = template.invoke(
    {
        'paper_input': paper_input,
        'style_input': style_input,
        'lenght_input': lenght_input
    }
)

if st.button('summarize'):
    result = model.invoke(user_input)
    st.write(result.content)