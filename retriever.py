from langchain_community.vectorstores import FAISS


def faiss_retriever(store: FAISS, k):
    return store.as_retriever(search_kwargs={"k": k})
