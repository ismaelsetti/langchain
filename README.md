# langchain

## Requirements
- Install Ollama: https://ollama.com/download
- Command to pull the open source LLM models you need:
```
ollama pull <model_name>
```

## Execution
- Run OpenAI chatbot:
```
streamlit run chatbot/app.py
```
- Run Llama2 chatbot:
```
streamlit run chatbot/locallama.py
```
- Run API server (FastAPI):
```
python api/app.py
```
- Run API client:
```
streamlit run api/client.py
```