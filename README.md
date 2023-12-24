![Running app](https://github.com/Aravind-Sridhar/Blog-Generation-using-Llama-2/blob/e639c6091dc06e2d5d5ccb11ea58c8a8ea80cb71/Blog%20Generation%20using%20Llama-2.jpeg)

# Blog Generation using Llama2

This is a Streamlit web application that generates blog content using the Llama2 language model. Users can input a topic, specify the number of words, and choose a blog style to generate a blog post dynamically.

## Getting Started

### Prerequisites

- Python 3.9
- [Streamlit](https://streamlit.io/)
- [langchain](https://github.com/LanguageResearchInc/langchain) library
- Llama2 model file (`llama-2-7b.ggmlv3.q8_0.bin`) - You can obtain this from the official Llama2 repository or other sources https://huggingface.co/TheBloke/Llama-2-7B-GGML/tree/main).

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Aravind-Sridhar/Blog-Generation-using-Llama-2.git
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to the provided local URL (usually http://localhost:8501).

3. Input the blog topic, number of words, and select a blog style.

4. Click the "Generate Blog" button.

5. View the generated blog post.

## File Structure

- `app.py`: Main Streamlit application script.
- `langchain`: Module containing the langchain library for working with language models.
- `llama-2-7b.ggmlv3.q8_0.bin`: Llama2 language model file.

## Configuration

- The Llama2 model file path is specified in the `app.py` file. Modify it if your file is located elsewhere.

