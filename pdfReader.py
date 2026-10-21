from langchain_community.document_loaders import PyPDFLoader

path = "docs/capstone/attention_is_all_you_need.pdf"


def readDoc(path=path):
    return PyPDFLoader(path).load()
