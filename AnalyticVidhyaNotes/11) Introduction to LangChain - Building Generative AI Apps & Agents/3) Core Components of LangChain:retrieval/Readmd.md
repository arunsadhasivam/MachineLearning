
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
