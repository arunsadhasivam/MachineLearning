Introduction to LangChain:
===========================
![image](https://github.com/user-attachments/assets/92187b50-bd74-49b4-b701-32b0dfdcc542)

    - Framework for developing applications powered by LLM.
    - primarily in python and also in javascript.
    - integrations with many third party APIs like Ollama, OpenAI
    - opensource with 80k+ stars on Github.


why do we need LangChain:
===========================

![image](https://github.com/user-attachments/assets/d2e40dd1-7dba-4610-8dd2-e2d966e47d99)


  - this is a typical llm app setting which we have a query run it through the LLM model and get the output.
  - lot of time, we want to give llm more capabilities, for that in the prompt we add more context.
  - that context might be that we have an integration of the website scrapping and then when the user makes a query ,
    we search from the web , get some data and also add that in our prompt.
  - there might be cases where we have internal data, that we store in our vector store, and we also retrieve certain documents
    and add it to our prompt.
  - using this and the query , with them call the llm model and the llm model gets us a output.
  - with this setting, we might get in to certain problems, one is the query changes a lot with prompt engineering over time
    and things we are using now, might not be the exact prompt that we are using in the coming month.
  - Vector Store Retrieval (RAG) is also there which vector store was used , what where the type of documents and different
    settings that we use for vector store might also change.
  - Tools for website scrapping that we use in real time when the user makes a query is also something that might changes over time.
  - Also when we make the call to llm model, there are multiple parameters that we change which also is something that we keep
    track of .


LLM Ecosystem:
===============

  - as you can see , this project itself changes a lot over time, and we have to keep track of all the configuration that you are using.
  - so with langchain , it has support for multiple prompt types but different types of llm models , it also have support for
    multiple different type of vector store and it also has multiple tools , we discuss web scrapping as one of the tools.
  - but they are lot of other tools, that we want to use , to get more features in our applications, which we can then integrate with the LLM.
  - we also have multiple models,the model that we would be using now might get outdated quickly and then we have change the model and we
    changes lot of othere parameters as well.then we have also multiple output parsers also available.
  - the output that we see over here would be in plain text, a streaming byte that would be written by llm model, they are multiple
    output parsers,which can parse this output and can give us a really good standardized output in our own format.
  - then we have things like agents , which is really popular these days where we give the llm the capability to make decisions.
  - in that case , implementing the agents is also cumbersome because of all the changes and configuration parameters and features
    that has to be given to llm models.
  - and to work or create agents it is very easy to do that in langchain.



