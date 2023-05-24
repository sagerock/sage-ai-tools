

from langchain.document_loaders import DirectoryLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter

my_loader = DirectoryLoader('contentfolder')
documents = my_loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
texts = text_splitter.split_documents(documents)

from langchain.vectorstores import Chroma, Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone

PINECONE_API_KEY = 'insert-your-pinecone-api-key-here' # put your pinecone api key in here.
PINECONE_API_ENV = 'us-west4-gcp' # you might have to change this.
OPENAI_API_KEY = 'sk-put-your-openai-api-key-here' # put your openai api key in here.

embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

# initialize pinecone
pinecone.init(
    api_key=PINECONE_API_KEY,  # find at app.pinecone.io
    environment=PINECONE_API_ENV  # next to api key in console
)
index_name = "sagerock" # put in the name of your pinecone index here

docsearch = Pinecone.from_texts([t.page_content for t in texts], embeddings, index_name=index_name, namespace="happydays")


