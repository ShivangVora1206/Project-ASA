import fastapi as fp
import uvicorn

app = fp.FastAPI()

@app.get("/")
def endpoint1():
    return " hello world! "

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)