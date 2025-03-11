from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

if __name__ == "__main__":
    print('Hellow LangChain')

    summary_template = """
        given the information {information} about a person, I want you to create:
        1. A short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )

    llm = ChatOpenAI(temperature=0.9, model_name="gpt-3.5-turbo")

    chain = summary_prompt_template | llm

    output = chain.invoke(input={"information": "I am a human"})
    print(output)