import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers


def get_llama_response(input_text, num_words, blog_style):

    llam2 = CTransformers(model=r"D:\Blog-Generation-using-Llama2\llama-2-7b.ggmlv3.q8_0.bin",
                          model_type='llama',
                          config={'max_new_tokens': 256,
                                  'temperature': 0.1})

    template = """
    Generate blog post content for the following topic: {input_text} within {num_words} words in {blog_style} style.
    """

    prompt = PromptTemplate(
        input_variables=["input_text", "num_words", "blog_style"], template=template
    )

    response= llam2(prompt.format(input_text=input_text, num_words=num_words, blog_style=blog_style))

    print(response)

    return response

st.set_page_config(page_title="Blog Generation using Llama2", page_icon=":robot:", layout="centered", initial_sidebar_state="collapsed")

st.header("Blog Generation using Llama2")

input_text = st.text_input("Enter topic for blog generation")

word_count, blog_style = st.columns([5, 5])

with word_count:
    num_words = st.text_input("Enter number of words")

with blog_style:
    blog_style = st.selectbox("Select Blog Style", ("Technical", "Non-Technical", "Personal"), index=0)

submit = st.button("Generate Blog")

if submit:
    st.write(get_llama_response(input_text, num_words, blog_style))