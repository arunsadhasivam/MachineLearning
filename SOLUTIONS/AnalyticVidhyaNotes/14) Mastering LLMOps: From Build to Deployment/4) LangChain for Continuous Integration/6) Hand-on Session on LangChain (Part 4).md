Hand-on Session on LangChain (Part 4):
=======================================

   - Application retriever is ready
   - you can call llm module, same way before.
   - we have langchain core prompts,chatpromptTemplate,RunnablePassThrough
   - RunnablePassThrough is that in this RAG application, the prompt looks like this,
     answer this question using provided context only.
   - we would provide the context , but the context comes from vector store or retriever.
   - this is the question, that the user would be asking.
   - now , this context would not be something that would be input while the chain invocation is there.
   - it should be in the chain, it should automatically comes from the vector store.
   - so , we dont have to specify the variable.
   - if there are things, which would be provided in the chain in between by other components, we can create
     something called RunnablePassThrough and that particular component will just inject the value for that
     variable as it comes along.
   - let say how it looks like
   - we created a chatPrompt using this message : {"human",message}
   - we create a chain, the chain looks something like this,
        1) here the context
        2) thats the question and the question is RunnablePassThrough
        3) then we have chain that we input this in to prompt and we have llm as output.

   - if we run this, we can see this chain just have to provide the question and the context is now
     coming from the retriever.
   - then i can simply do langchain.invoke() and as you can see context_variable was automatically provided
     by retriever and we have the question something that we input over here.


![image](https://github.com/user-attachments/assets/8abe82c9-6534-4434-b4e6-ad34ed30e241)
 
   - we have also have something called langchain.globals , which is just global variable and methods that we can use.
   - one of the important method is set_verbose,set_debug
   - Basically , if you want to see during our chain,
       1)what exactly changed,
       2) what was the input given to llm,
       3) what actually happened at the prompt level.
       4) what actually happend at the vector store level.
   - All these things you can check by just importing  these set_verbose() and set_debug()
   - they both offer different levels of output.
![image](https://github.com/user-attachments/assets/bf3d6088-7be3-447b-a82c-2547eced3ba5)

   -  you can set the verbose and debug  values true and just invoke() chain in the similar manner
![image](https://github.com/user-attachments/assets/8207a33f-eac4-4f55-b70b-8fba0c0072ef)

   -  as you can see it shows what was happening at each stage by using the set_verbose() and set_debug() to true.
   -  you can see 
      1) what happen in the prompt template stage,
      2) runnablePassThrough, what was the sent input
      3) what was llm output generated.
  - in this way, we standardized the whole rag generation process, these chain can be really huge and can still be
    modularized in a really good way.
    ![image](https://github.com/user-attachments/assets/414c7b98-9637-4308-9c3d-42521599304c)

  - we can export them as JSON, retrieve back the JSON and these parameters can then be changed by simply by changing
    values in JSON.this can help a lot during research and experimenting with different kinds of retrievers llm
    and different out_parsers as well.
  - this is something about langchain.
  - now we can actually take this output and standardize it into a much better way and monitor at another central location
    using something called langfuse.
![Uploading image.png…]()

   
     
     
    


