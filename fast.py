# backend.py
from fastapi import FastAPI
from dotenv import load_dotenv
from together import Together
from pydantic import BaseModel
from typing import List, Dict

load_dotenv()

app = FastAPI()
client = Together()


class Message(BaseModel):
    role: str  
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]  
    user_id: str  

class ChatResponse(BaseModel):
    answer: str
    usage: Dict[str, int] 

@app.post("/api/chat")
async def chat_with_llm(request: ChatRequest):


        response = client.chat.completions.create(
            model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
            messages=[{"role": msg.role, "content": msg.content} for msg in request.messages]
        )
        

        model_response = response.choices[0].message.content
        
  
        return ChatResponse(
            answer=model_response,
            usage={
                "prompt_tokens": response.usage.prompt_tokens,
                "completion_tokens": response.usage.completion_tokens,
                "total_tokens": response.usage.total_tokens
            }
        )
    
        return {"error": str(e)}

