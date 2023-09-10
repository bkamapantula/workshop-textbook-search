from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)
collection_name = ""
client = ""
collection = ""
n_results = 5

try:
    client = chromadb.PersistentClient(path='/db')
    # Get a collection object from an existing collection, by name. If it doesn't exist, create it.
    collection = client.get_or_create_collection(name=collection_name)
except Exception as e:
    print('Error connecting to the collection:', e)


# Don't use it
def delete_chromadb_collection(collection_name=''):
    try:
        client = chromadb.PersistentClient(path='/db')
        client.delete_collection(name=collection_name)
    except Exception as e:
        print('Could not delete the collection', e)


class TextBook(BaseModel):
    search_input: str
    selected_class: str
    selected_subject: str


class SearchResponse(BaseModel):
    result: Optional[str] = None


@app.post('/search')
async def query_textbook(search_input: TextBook, response=JSONResponse):
    query = search_input.search_input
    results = collection.query(
        query_texts=[query],
        n_results=n_results,
        where={
            "$and": [
                {
                    "class": {
                        "$eq": int(search_input.selected_class)
                    }
                },
                {
                    "subject": {
                        "$eq": search_input.selected_subject
                    }
                }
            ]
        },
    )
    return results

if __name__ == "__main__":
    port = 8989
    uvicorn.run("app:app", host="0.0.0.0", port=port)
