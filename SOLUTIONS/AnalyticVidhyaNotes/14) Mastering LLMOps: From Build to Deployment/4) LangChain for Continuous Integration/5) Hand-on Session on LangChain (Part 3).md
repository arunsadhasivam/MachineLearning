Hand-on Session on LangChain (Part 3):
==========================================


 - in chain all the processes that we just saw before.
 - in chains, what we can do is all these processes that we found ,
     1) modularizing the prompt using prompt templates,
     2) creating these llms as objects using different third party integrations.
     3) then after the final response is generated,
     4) we have an parser class
     5) if you want to combine all of them together we can simply do using (|) pipe operator.
        
 - previoulsy, we used to combine 2 things, but in the same way you can generate it to create chains with multiple steps.
 - these chains can also run in parallel, there are lot of features that this supports.
 - so over here we have chat prompt template from message, we create prompt template, then we create the llm class
   and we have the parser, then we combine into one chain, and then we can simply run this chain.
 - this standardized our code really well.
 - and we can just do chain.invoke() and then we can simply run this chain()
 - so this standaridized our code really well.
 - we can use chain().invoke() and we click on it , the name we would provide at runtime , and
   the user input is also something that we will provide at runtime.
 - and then this chain will run.
![image](https://github.com/user-attachments/assets/4753fbb2-8e7c-4f2c-b009-b3ddd715bfbd)

 - we pass the hyperparameters, string parser will parse the string and we have final response generated.
 - one of the advantages of doing this once all of this is standardized really well, you can use other features of chain.
 - the thing that we can implement is called streaming, but to implement streaming ourselves , we have to then make
   sure all the streaming output and parsing and all the logic is written by us. this can be cubersome but in chain
   we can get it by default.

Chains:
=======

![image](https://github.com/user-attachments/assets/8ff6d49f-2df5-4f0c-b757-a961b5faebe4)

- we can do chain().stream() and then we get a stream() object back.
- we can subscribe to this and then we can get the output in token by token format rather than
  waiting for the whole answer we will just the response back in token by token fashion.
- we saw the generated response "my name is bob, how can i assist to you today" as token.
- also see the chain  fails, then there is also one of parameter in which we can do automatic retry in chain.
- this is also one of the advantages or feature of chain that it already support.


Saving and loading chains:
============================

  - so that we discussed in presentation slides, a feature that chain already supports.
  - and so we have saving and loading chain.
  - the chain that we created can be saved as a json file and then we can save it into a persistent storage
    and then we can load it at runtime and then use it. this has modularized the code really well.
  - chain are still in beta and are not fully reliable ,but we can still see how chains can be stored and
    loaded at runtime.
  - so we have the chains before , just create a JSON .dump using JSON string chain, which is nothing
    but uses the load module and then calls dumpd.
  - and then this just save it into a file called chain.json . so if we go to langchain, in the same folder
    we have chain.json . we click on it , we see the chain .
  - now , this is sagemaker way of showing json. this is a json file but then sagemaker really helps in
    standardizing this properly and showing it in a modularized fashion.
![image](https://github.com/user-attachments/assets/21d597f9-8c85-48ed-9ba2-d57baf636d9d)


![image](https://github.com/user-attachments/assets/4bda0e9a-ad95-4b18-822a-27e5321a02bc)

  - we have the root chain as we can see all the
    1) information store  ,
    2)  we have first , middle and last
    3) which is one the way the chain object is created,
    4) in which you can see that these are the 2 variables  input that we have,
![image](https://github.com/user-attachments/assets/e15f051e-1ce0-44d8-abbd-82ed84c6b225)
    
    5)  what are the messages that we are provided,
    6)  your helpful AI Assistant
    7)  your name is this.
    8)  what are the variable that are present in the middle
    9)  open AI chat and all the hyperparameters are saved inside here.
    10)  we simply saved in json format.
![image](https://github.com/user-attachments/assets/2f7fd203-e017-4f9e-931a-5654a9a9391c)



![image](https://github.com/user-attachments/assets/d47b1c60-a1c4-4639-914f-c6a747ec7ed2)


  - chain.middle[0].lc_secrets is the dictionary of all the secrets used in chains
  - Now, the chain was smart enough to know that openAI key was one of the secrets , which should not be
    saved in the json format. so it just create a placeholder for this.
  - now, we can do is , we can load the chain again,using the load function from langchain,and then over
    here is secrets map in which you can provide again the openAPI_KEY and it will automatically load the
    chain with the secrets that were present
  - And as i said, the function load() is still in beta and there might be certain changes in the library
    go through.
  - and then we can do chain.invoke() and as you can see , we loaded the chain from json and it has
    all the things that we mentioned before,
      1) the same chat template
      2) the same hyperparameter in llm call
      3) the output is also passed in a proper string.

  - this is the introduction of langchain.
  - Now, we can implement RAG.


Rag:
======

  - 2nd notebook LangChain_RAG.ipynb.
  - we load env again.
  - one of the advantages as we discussed, that they have lot of loaders and lot of integrations provided by
    langchain by default.
  - so , we can go to the langchain community package and in document loader
  - wikipedia loader can be given any query and also can tell how many documents that we want to load and
    maximum characters we want to load in each document.
  - we can load at the same time and can do lazy loading , which will run when finally invoke().
![image](https://github.com/user-attachments/assets/de815c77-4a6a-4192-8ac1-80f36b5b047f)



  ![image](https://github.com/user-attachments/assets/873eb2d2-7dc0-4cb0-8f6b-49f99949a389)
![image](https://github.com/user-attachments/assets/2e67d5ab-7116-462f-a115-77e460e2fbdd)
![image](https://github.com/user-attachments/assets/9325dd88-6054-45fc-9d64-85ab304f0ce8)
![image](https://github.com/user-attachments/assets/a6f32635-1813-41d5-8703-6ad718d0f984)

  - so, it went to wikipedia for the topic of AI and then it created these 2 documents
  - now, then in RAG applications, 
      1) we have to take this document,
      2)  then we have to split it
      3)  we have to embeddings on it.
      4)  we have to store it in vector store.
      5)  all of this is also something langchain give support out of box.

  - in langchain , something we have called text_splitter, in which they are lot of different ways
    of splitting the text, we just simply take the recursive character text splitter.
   - in the recursive character text splitter, we can mention , 
        1) these are documents.
        2) what are the chunk size that i am looking for
        3) then the chunk should overlap for how many characters or text.
  - then , previously  as we can see we loaded everything in docs , which also created a class of document
    to structure properly and then just do text splitter.split() document provided the docs.
  - As you can see it took the documents and splitted it into managable chunks.

![image](https://github.com/user-attachments/assets/04208588-c314-4b25-ae10-d18bea539c99)
![image](https://github.com/user-attachments/assets/fb5d6de6-9905-4c09-8249-5f07469c5561)
![image](https://github.com/user-attachments/assets/c5d504e7-2082-40e0-a40f-6a31318164b5)
![image](https://github.com/user-attachments/assets/619ec36d-d268-4f4d-b233-d861ad84217e)
![image](https://github.com/user-attachments/assets/d6ff49cc-6bad-474b-bf88-95035ea1fcf4)

  - Now, that the chunks are created, now put them in a vector store by putting embeddings of it.
  - so for that, we have langchain chroma which we installed , which is a vector database integration provided
  - we can also use embedding model.
  - we use the embedding model, we use one  from openAI.
  - and for that we import langchain openAI and import openAI embedding model.
  - we simply create an object of embedding, and in chroma vector store, we can just mentioned the documents
    that we have created and it finally created a vector store.
  - so,to create a vector store was this simple.

![image](https://github.com/user-attachments/assets/9d2208e3-5c53-4836-a72a-99046a87503c)

  - you can also do batch operations.
