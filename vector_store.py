from langchain_community.vectorstores import FAISS


def faiss_vectore_store(docs, embeddings) -> FAISS:
    return FAISS.from_documents(docs, embeddings)
