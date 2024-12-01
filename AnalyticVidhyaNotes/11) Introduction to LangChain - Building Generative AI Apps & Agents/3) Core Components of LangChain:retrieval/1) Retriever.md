
Steps:
======

        Load(internet) - >   transform -> embeddings(llm call) -> store in vector db.
        
        step1-> load data from file upload
        step2-> transform in to managable chunk otherwise no.of tokens exceeded
                exception will occurs.
        step3-> create embeddings for the documents to be make llm calls. since
                llm understand only numbers. usually llm call to get embeeddings.
        step4->   store in vector db to avoid unnecessary llm call. since llm calls are cost.
                 also you llm cache,stream. llm supports asynchronous (astream ) and stream.


Build Retriever on top of vector db:
=====================================

when query it searches the vector db . it transform query to embedding vector and searches
db which already stored with vector of documents. it searches based on 
cosine similarity or other searching strategy.


Document Loader:
=================


popular document loader to load data from source. source can be pdf,ppt to extract text data
and relevant metadata like pageno,authorname . langchain has loader for every posssible data.

unstructured.io -> langchain has binding to unstructured .io to load from pdf and other unstructured data.

pdf loader -> langchain has integration with pdf loaders.pypd,pymupdf(fatest),pdfminer .
used to extract ocr data aswellas
