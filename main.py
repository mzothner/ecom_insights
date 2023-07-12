import streamlit as st
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv

from tempfile import NamedTemporaryFile

def main():

    load_dotenv()

    st.set_page_config(page_title="Ecom Insights")
    st.header("Ecom Insights")
    
    user_csv = st.file_uploader("Upload your CSV file: ", type="csv")

    if user_csv is not None:
        with NamedTemporaryFile() as f: # Create temporary file
            f.write(user_csv.getvalue()) # Save uploaded contents to file
        
            user_question = st.text_input("Ask a question about your data: ")

            llm = OpenAI(temperature=0)
            agent = create_csv_agent(llm, f.name, verbose=True)

            if user_question is not None and user_question != "":
                response = agent.run(user_question)
                st.write(f"{response}")


if __name__ == "__main__":
    main()
