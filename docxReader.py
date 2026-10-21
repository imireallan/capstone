from langchain_community.document_loaders import Docx2txtLoader

path = "docs/Allan-Imire-Resume-Tailored.docx"

loader = Docx2txtLoader(path)
