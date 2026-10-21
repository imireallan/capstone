from langchain_text_splitters import CharacterTextSplitter

sent = "My name is Allan Imire. I'm learning RAG. AI Engineering is so fun once you understand the basic foundations of LLM"

splitter = CharacterTextSplitter(chunk_size=30, chunk_overlap=10, separator=" ")

chunks = splitter.split_text(sent)

for chunk in chunks:
    print(chunk)
