import pickle

from langchain.vectorstores import FAISS

from data_schema.agents import setup


class SydoniaDatabaseSchema():
    __slot__ = ("query_generator", "vector_db")

    def __init__(self) -> None:
        # We leverage RAG-like behaviour because of the size of incoming Sydonia schema. 
        # The example you have is solely for the sake of demonstration and only contains two tables.
        self.query_generator = setup()
        # This could be done on a remote server but the project aim to be self-contained and the usage of the Azuer is just for the sack of IMF demontration.
        # The embedding is leveraging OSS both for FAISS and the embedding model.
        with open('../tmp/schema_loader/hf_model.pkl', 'rb') as f:
            embedding = pickle.load(f)
        self.vector_db = FAISS.load_local("../tmp/schema_loader/faiss_index.faiss", embeddings=embedding)

    async def retrieve_schema(self, prompt: str) -> str:
        for _ in range(3):
            response = await self.query_generator.create(prompt)
            if response:
                return response.content
        self.vector_db.similarity_search(prompt, k=1)

