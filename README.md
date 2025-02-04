# GroqTranslator
This code translates your sentences to language you want.
## Dependencies
Needed dependencies are FastAPI, Unicorn, Pydantic and Groq.
```
pip install fastapi uvicorn pydantic groq
```
## Instructions to run
Clone the repositorio.
```
git clone https://github.com/ranurm/GroqTranslator.git
cd GroqTranslator
```
Set GROQ_API_KEY environment variable.
```
export GROQ_API_KEY="your_groq_api_key"
```
You can run the FastAPI server with Uvicorn.
```
uvicorn groqAPItask:app --reload
```
With PowerCell can be tested with command:
```
Invoke-WebRequest -Uri "http://127.0.0.1:8000/translate/" -Method POST -Headers @{ "Content-Type" = "application/json" } -Body '{"text": "Hello, world!", "target_language": "fi"}'
```
Also curl for other devices:
```
curl -X POST -H "Content-Type: application/json" -d '{"text": "Hello, world!", "target_language": "fi"}' http://127.0.0.1:8000/translate
```
