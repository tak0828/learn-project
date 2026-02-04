from fastapi import FastAPI
import redis
import os

app = FastAPI()

redis_host = os.getenv("REDIS_HOST", "redis")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.get("/")
def read_root():
    count = r.incr("counter")
    return {"message": f"Hello! You are visitor #{count}"}
