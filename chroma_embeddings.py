# import os

# from dotenv import load_dotenv
from langchain_community.embeddings import FastEmbedEmbeddings
from langchain_community.vectorstores import Chroma

# from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# load_dotenv()

# os.environ["HF_API_KEY"] = os.getenv("HF_API_KEY")


text = """
# Historical Events and World Developments

In **1453**, the Ottoman Empire conquered Constantinople, bringing the Byzantine Empire to an end. The city's capture changed trade routes and influenced the movement of scholars and classical knowledge into Western Europe.

In **1492**, Christopher Columbus reached the Americas during a voyage sponsored by the Spanish Crown. The expedition initiated sustained contact between Europe and the Americas, leading to profound changes in global trade, migration, and indigenous societies.

In **1776**, representatives of thirteen British colonies in North America adopted the Declaration of Independence on July 4. The document proclaimed that the colonies considered themselves independent states and laid out principles concerning liberty and government.

In **1789**, the French Revolution began, challenging the monarchy and the traditional social order in France. The storming of the Bastille on July 14 became a powerful symbol of resistance against royal authority. Later that year, the Declaration of the Rights of Man and of the Citizen articulated principles of individual liberty and equality before the law.

In **1804**, Napoleon Bonaparte crowned himself Emperor of the French. His rise followed years of political upheaval in France, and his government introduced reforms that influenced legal systems across Europe, including the Napoleonic Code.

In **1865**, the American Civil War ended following the surrender of major Confederate forces. The Thirteenth Amendment to the United States Constitution abolished slavery, marking a significant turning point in American history.

In **1884**, the Berlin Conference formalized rules for European colonization and trade in Africa. European powers negotiated territorial claims without meaningful representation from African societies, accelerating the partition of the continent.

In **1914**, the assassination of Archduke Franz Ferdinand of Austria-Hungary triggered a diplomatic crisis that contributed to the outbreak of the First World War. The conflict eventually involved major powers across Europe and beyond.

In **1945**, the Second World War ended after Germany surrendered in May and Japan surrendered in August. The United Nations was established that year, with the aim of promoting international cooperation and preventing future global conflicts.

In **1963**, Martin Luther King Jr. delivered his famous “I Have a Dream” speech during the March on Washington for Jobs and Freedom. The speech became an important moment in the American civil rights movement.

In **1969**, Apollo 11 landed on the Moon, and astronauts Neil Armstrong and Buzz Aldrin walked on its surface. This achievement represented a major milestone in space exploration and the technological competition of the Cold War.

In **1989**, the Berlin Wall fell, symbolizing the weakening of Cold War divisions in Europe. The event accelerated political changes across Eastern Europe and contributed to the reunification of Germany in 1990.

In **1994**, South Africa held its first democratic elections under universal adult suffrage. Nelson Mandela became president, marking the end of the apartheid political system and the beginning of a new democratic era.

In **2001**, terrorist attacks in the United States destroyed the World Trade Center towers in New York and damaged the Pentagon. The attacks transformed international security policy and influenced military and diplomatic developments around the world.

In **2010**, social and political protests began in Tunisia and spread to several countries in the Middle East and North Africa. These uprisings, commonly known as the Arab Spring, challenged established governments and led to different political outcomes across the region.

In **2020**, the COVID-19 pandemic disrupted international travel, education, healthcare, and economic activity. Governments introduced public health measures, while scientists developed vaccines at an unprecedented pace.

"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100, chunk_overlap=20, separators=["\n\n", "\n", ".", " ", ""]
)

chunks = splitter.split_text(text)

# for i, chunk in enumerate(chunks):
#     print(f'Chunk {i} \n')
#     print(chunk)

embeddings = FastEmbedEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vector_store = Chroma.from_texts(chunks, embeddings)

query1 = "What happened when Constantinople was captured?"
query2 = "Which year did America declare independence?"
query3 = "What historical event happened in 1789?"

result1 = vector_store.similarity_search(query1, k=4)
result2 = vector_store.similarity_search(query2)
result3 = vector_store.similarity_search(query3)

for doc in result1:
    print(doc.page_content)

# print(result1[0].page_content)
# print(result2[0].page_content)
# print(result3[0].page_content)
