from app.models.llm import LLMModel

llm = LLMModel()

response = llm.generate_response(
    "What are symptoms of flu?"
)

print(response)