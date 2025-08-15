from together import Together
from dotenv import load_dotenv
import os
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    prompt: str

class ChatResponse(BaseModel):
    answer: str    


load_dotenv()
api_key = os.getenv("TOGETHER_API_KEY")
client = Together(api_key=api_key)
LLM_Model = "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free"


@app.post("/chat", response_model=ChatResponse)
async def chat_with_llama(request: ChatRequest):

    response = client.chat.completions.create(
        model = LLM_Model,
        messages=[
            {
                "role": "user",
                "content": request.prompt
                
            }
        ]
    )
    # print(response)
    model_answer = response.choices[0].message.content
    return ChatResponse(answer= model_answer)



