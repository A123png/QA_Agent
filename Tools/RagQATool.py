from langchain.chains import RetrievalQA
from Models.Factory import llm
from Tools.VecStore import VecStore

vec = VecStore()
db = vec.load_chroma()
def rag_qa(query):
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=db.as_retriever()
    )
    response = qa.run(query)
    return response