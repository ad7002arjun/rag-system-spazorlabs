from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from app.rag.vector_store import load_vector_store

def get_qa_chain():
    db = load_vector_store()
    retriever = db.as_retriever()

    llm = ChatOllama(
        model="llama3",
        temperature=0
    )

    prompt = PromptTemplate.from_template(
        """Use the following context to answer the question.

        Context:
        {context}

        Question:
        {question}
        """
    )

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
    )

    return chain