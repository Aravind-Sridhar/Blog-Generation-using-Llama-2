# Import necessary libraries
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# Define a function to get the llama response
def get_llama_response(input_text, num_words, blog_style):

    # Create an instance of CTransformers with the Llama2 model
    llam2 = CTransformers(model=r"D:\Blog-Generation-using-Llama2\llama-2-7b.ggmlv3.q8_0.bin",
                          model_type='llama',
                          config={'max_new_tokens': 256,
                                  'temperature': 0.1})

    # Define a template for the prompt
    template = """
    Generate blog post content for the following topic: {input_text} within {num_words} words in {blog_style} style.
    """

    # Create a PromptTemplate using the template
    prompt = PromptTemplate(
        input_variables=["input_text", "num_words", "blog_style"], template=template
    )

    # Generate a response using the llama model and the formatted prompt
    response = llam2(prompt.format(input_text=input_text, num_words=num_words, blog_style=blog_style))

    # Print the response
    print(response)

    # Return the response
    return response

# Set Streamlit page configuration
st.set_page_config(page_title="Blog Generation using Llama2", page_icon=":robot:", layout="centered", initial_sidebar_state="collapsed")

# Display a header
st.header("Blog Generation using Llama2")

# Get user input for the blog topic
input_text = st.text_input("Enter topic for blog generation")

# Create two columns for word count and blog style selection
word_count, blog_style = st.columns([5, 5])

# Get user input for the number of words
with word_count:
    num_words = st.text_input("Enter number of words")

# Get user input for selecting the blog style
with blog_style:
    blog_style = st.selectbox("Select Blog Style", ("Technical", "Non-Technical", "Personal"), index=0)

# Create a button to trigger blog generation
submit = st.button("Generate Blog")

# If the button is clicked, generate and display the blog response
if submit:
    st.write(get_llama_response(input_text, num_words, blog_style))
