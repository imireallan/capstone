from connect import llmconnect
from pdfReader import loader
from docxReader import loader as docLoader
from csvReader import loader as csvLoader


def main():
    # response = llmconnect().invoke(
    #     "What are the frameworks popular in creating llm applications in python?"
    # )
    # documents = loader.load()
    documents = csvLoader.load()
    print(len(documents))

    for doc in documents[:5]:
        print(doc)
        print('_'*100)


if __name__ == "__main__":
    main()
