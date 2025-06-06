from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate

from src.core.chains.embedder.embedder import Embedder


class Search:
    def __init__(self):
        self.embedder = Embedder()

        # self.llm = ChatOllama(
        #     model="qwen2.5:7b",
        #     base_url="http://localhost:11434"
        # )
        self.llm = ChatOllama(
            model="tinyllama:latest",
            base_url="http://localhost:11434"
        )

        self.prompt_template = PromptTemplate(
            template="""Based on the following legal information, answer the question clearly:
            Legal Information:
            {context}
            
            Question: {question}
            
            Answer:""",
            input_variables=["context", "question"]
        )

    async def answer(self, query: str) -> str:
        search_results = await self.embedder.search(query, limit=5)
        context = "\n\n".join([
            f"• {result['text']} (유사도: {result['score']:.2f})"
            for result in search_results
        ])

        prompt = self.prompt_template.format(context=context, question=query)
        response = await self.llm.ainvoke(prompt)

        return response.content