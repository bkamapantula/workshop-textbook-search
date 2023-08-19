# Creating a textbook search app

This workshop
- is an introduction to the Python ecosystem of embeddings, vector databases.
- demonstrates how to build a search app
- is designed to be delivered in-person.
- not a deep dive in to all the technologies involved.

## Prerequisites

I recommend to keep the workshop contained in a conda environment, if you can.

A machine or an environment (Google Colab or Kaggle etc.) that supports:
- Python
- [LangChain](https://python.langchain.com/docs/get_started/installation)
  - We will use [Chroma](https://docs.trychroma.com/getting-started), an open-source and lightweight embedding database.
- Pandas, for data transformations
- [SQLite]([url](https://www.sqlite.org/index.html)https://www.sqlite.org/index.html), [SQLite browser](https://sqlitebrowser.org/) to view the records.
- [FastAPI](https://fastapi.tiangolo.com/#installation), uvicorn

## Outline

1. What are embeddings?
2. What are vector databases?
3. What is Retrieval Augmented Generation (RAG)?
4. Building a search engine
    - Select textbook (will be preselected)
    - Create chunks from the book pages using LangChain text splitter utilities
    - Embed chunks in Chroma
    - Build a query service
    - RAG to summarize the user question
    - Host with FastAPI, if time permits
5. Troubleshooting
6. Q&A, Discussion
7. Appendix
    - Tooling
    - Python Ecosystem

Skeleton utilities for all these will be provided for the workshop.

## Feedback

TBD

## Contact

Email me with any questions: bhanu@collab.place
