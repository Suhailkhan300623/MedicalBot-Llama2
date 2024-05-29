from flask import Flask, render_template, request
from src.helper import hf_embedding
from langchain.vectorstores import Pinecone
import pinecone
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain.chains import LLMChain
from dotenv import load_dotenv
from src.prompt import *
import os
from pinecone import Pinecone


load_dotenv()
api_key = os.getenv('api_key')
index_name = os.getenv('index_name')

app=Flask(__name__)

pc = Pinecone(api_key=api_key, region='us-east-1')
index = pc.Index(index_name, region='us-east-1', host='https://medical-bot-tnswrkd.svc.aped-4627-b74a.pinecone.io')

prompt=PromptTemplate(template=prompt_temp, input_variables=['context', 'question'])
chain_type_kwargs={'prompt':prompt}

embedding=hf_embedding()

llm=CTransformers(model='model\llama-2-7b-chat.ggmlv3.q4_0.bin',
              model_type='llama',
              config={'max_new_tokens':512,
                      'temperature':0.8})



def query(query):
    query_embedding = embedding.embed_query(query)
    response = index.query(namespace="doc1", vector=query_embedding, top_k=2, include_values=True, include_metadata=True)
    
    # Extract context from query results
    contexts = [match['metadata']['text'] for match in response['matches']]
    context_text = " ".join(contexts)


    prompt = PromptTemplate(template=prompt_temp, input_variables=['context', 'question'])

    chain = LLMChain(llm=llm, prompt=prompt)

    answer = chain.run(context=context_text, question=query)

    return answer


@app.route('/')
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input_text = msg
    print(input_text)
    result = query(input_text)
    print("Response: ", result)
    return str(result)


if __name__=='__main__':
    app.run(debug=True)