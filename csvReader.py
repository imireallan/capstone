from langchain_community.document_loaders import CSVLoader

path = 'docs/jobs_latest_allan_engineering.csv'

loader = CSVLoader(file_path=path)