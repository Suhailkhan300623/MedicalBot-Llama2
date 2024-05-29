from src.helper import pdf_loder, chunks, hf_embedding
import pinecone
from dotenv import load_dotenv
import os

extracted_data=pdf_loder('data/')
text_chunk=chunks(extracted_data)
embedding=hf_embedding()



load_dotenv()
api_key=os.getenv('api_key')
index_name=os.getenv('index_name')

from pinecone import Pinecone

pc=Pinecone(api_key=api_key, region='us-east-1')
index=pc.Index(index_name=index_name, region='us-east-1', host='https://medical-bot-tnswrkd.svc.aped-4627-b74a.pinecone.io')


# for i, chunk in enumerate(text_chunk):
#     embedding = hf_embedding().embed_query(chunk.page_content)
#     index.upsert(vectors=[{'id': f'doc_chunk_{i}',
#         'values': embedding,
#         'metadata': {'text': chunk.page_content}
#     }],namespace='doc1')

