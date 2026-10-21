from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
The agent should be able to search for the latest iPhone information, retrieve the relevant price, and use its math tool to perform a conversion if it obtains a USD-to-GBP rate.
Important: The exchange rate and product price should come from current search results rather than the model's memory.
If you still encounter an error, please share the cell where you initialize groq_llm and the output of pip show langchain langchain-core langchain-groq groq. That will help identify whether the remaining issue is model behavior or package compatibility.

"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=3000,
    chunk_overlap=600,
    separators=["\n\n", "\n", ".", " ", ""]
)

# chunks = splitter.split_text(text)