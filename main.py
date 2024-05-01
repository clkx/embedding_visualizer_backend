from fastapi import FastAPI
import os
from dotenv import load_dotenv
import pymongo
from bson import json_util
import json
from sklearn.decomposition import PCA
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

load_dotenv()
app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MONGO_URL = os.getenv("MONGO_URL")
myclient = pymongo.MongoClient(MONGO_URL)
mydb = myclient["mydatabase"]
mycol = mydb["embedded_music"]

@app.get("/all")
def find_all():
    cursor = mycol.find({}, {"_id": 0, "name": 1, "genre": 1, "prompt": 1, "embedded_prompt": 1})
    results = list(cursor)
    
    # Extract embedded prompts from results
    embedded_prompts = [item['embedded_prompt'] for item in results if 'embedded_prompt' in item]

    # Dimensionality reduction to 3D
    if embedded_prompts:
        pca = PCA(n_components=3)
        embedding_3d = pca.fit_transform(embedded_prompts)

        # Add reduced dimensions to results and remove the original embedding
        for item, coords in zip(results, embedding_3d):
            item['umap_3d'] = coords.tolist()
            del item['embedded_prompt']  # Remove the original embedding

    return json.loads(json_util.dumps(results))

@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, log_level="info")

