LCEL and Runnables:
==================


  - defined agent is
  - idea of connecting model to tools
  - agent loop
  - idea of autonomously decide when to call the loop and when to give output to user.
  - how useful agents can implement routing procedure
  - langchain is a python framework that also has a javascript implementation by the way
  - that allows you for implementing context-aware reasoning applications that essentially allow you to
    put forward these routing procedures.
  - langchain is a fast native framework with components and after chain shelves which are essentially building
    blocks.
  - talked about the 3 basic components
     1) model
     2) prompt
     3) output_parser
  - langchain has many other components which are also essential.
  - now one another foundation components of langchain is LCEL (lang chain expression language)
  - Runnable interface behind the expression languages essentially the LCEL expression language.
  - LCEL which allows the composition of chains, which is another building block we introduce now.
  - Lang Chain expression language is an interface which leverage the | pipe symbol to compose Langchain components.
![image](https://github.com/user-attachments/assets/5cfb043f-39de-402a-8d58-130b5a24da4f)
  - there are all other components like retriever, tools etc.
  - what are all these things that are composed with | symbols these are chains.
![image](https://github.com/user-attachments/assets/c3623149-8f89-4774-8186-8276a60f067d)

  - langchain is the combination of components (prompt | model| output parser)
  - output parser which converts the chain block to a string.
  - Now we see why we need the output_parser to parse in to a string.
  - should it be a string when comes out of chain .
  - but it is no that usually output from chain is a object , we need to parse out to a string.
  - when we combine, prompt, outut_parse,model we get chain.
  - it is building block we can re-use.
  - it  is something whcih can be applied many places so on.
  - we are able to build chains out of these components.
  - we are putting together these components with in the scope of this language
  - now we can invoke the chain meaning calling the chain with a dictionary containing key that
    is reference in the template string .
  - it is called concept chain.invoke({'concept':'probability distribution'})
  
