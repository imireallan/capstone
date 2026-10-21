from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough,
)

from connect import llmconnect
from embeddings import fastembed_embeddings
from pdfReader import readDoc
from prompt_template import template
from recursive_text_splitter import splitter
from retriever import faiss_retriever
from schema import Transformer
from vector_store import faiss_vectore_store

# print(llmconnect().invoke("Hi"))

documents = readDoc()
chunks = splitter.split_documents(documents)

vector_store = faiss_vectore_store(chunks, fastembed_embeddings)

query = "What are transformers?"

retriever = faiss_retriever(vector_store, 2)

result = retriever.invoke(query)


def join(doc):
    return {"context": "\n\n".join(d.page_content for d in doc)}


q_chain = RunnableParallel(
    {"question": RunnablePassthrough(), "context": retriever | RunnableLambda(join)}
)

result = q_chain.invoke(query)
parser = PydanticOutputParser(pydantic_object=Transformer)

prompt = PromptTemplate(
    template=template,
    input_variables=["question", "context"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = q_chain | prompt | llmconnect() | parser

query = input('Please enter your query.\n')
response = chain.invoke(query)

for ans in response.answers:
    print('Text \n', ans['text'])
    print('Context \n', ans['context'])
