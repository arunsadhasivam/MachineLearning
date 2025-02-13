Hand-on Session on LangChain (Part 5):
======================================

![image](https://github.com/user-attachments/assets/609b55f6-8185-45d8-800d-ef8e925352a8)
![image](https://github.com/user-attachments/assets/44e182fb-b237-474a-9ce4-4a1f50bd22c2)
![image](https://github.com/user-attachments/assets/a6e0af48-deef-4fd0-ac82-f9a07c45bf40)
![Uploading image.png…]()


- now we have documents ready and now build a chain.
- so we will import the llm and then create a llm object and then we would have our prompt template
- so this is how it is , answer the **questions using provided context only**
- we would ask it a question, for that we provide it the context.
- and now as we can see, the chatprompttemplate is created, the output_parser is ready
- but we want the context to be coming from something called as retriever, that we just created.
- and this question that would be given by the user at runtime. and so for those things,we just have
  simple object called RunnablePassThrough which simply provides the key at runtime.
   
- And so this is something that we can just import from langchain.
- so , this chain is created and it simply says that the context is something provided by retriever
  and then the other variable i.e question will be provided at runtime.
- so we have parser as well at the end, we can create a chain out of it and then we can do chain.invoke()
- as you can see there are 2 variables, in which one is already provided by the retriever for the
  second one , there is only one variable that needs to be provided you dont need to mention.
  otherwise for multiple ones we need to create a dictionary just like {"context":retriever ,"question":RunnablePassThrough()}
  here mentioning the key and value.so then i simply do chain.invoke()
- chain.invoke()
   1)what the retriever takes it,
   2) find the documents,
   3) put it in to context variable
   4) then the question is this, what is AI through the RunnablePassthrough() that is also input in to messageprompt.
   5) the prompt is finally created
   6) llm is finally called
   7) the output  finaly generated.
   8) output is passed as string output
   9) we have final set of output.

 - we dont have any idea what actually happened inside, there are places where we see a lot of errors hapening
   and we want to modify and see where the error is .
   1) either it is in the document retriever.
   2) or may be prompt may be prompt not good
   3) hyper parameter
   4) or it is some other complex parser which did not parse properly.


- to do this we have something in global module some variables called set_verbose() and set_debug()
- these are 2 methods that we can simply set as true and then if we do that whole langchain eco-systems print
  lot of more logs .
- then we do chain.invoke() again ,
    1) now we can see how the chain started
    2) the chain was having this is the input
    3) then what are the runnableSequence happened
    4) what document retriever
    5) what were the final prompt that actually went in
    6) what was the final generated actually created by llm.
    7) different arguments
    8) and then we post the output of the parser.
    9) and so , in this way , we know in more depth what is actually happening behing the scenes.
    10) and this can simply be done by just invoking one of the functions.



    Summary:
   ==========

     - we know how we langchain to standardize the whole code base.
     - this not only gives us the flexibility to be able  to use different integrations to develop these
       applications quickly.
     - because everything is super modularized, we can just plug and play with multiple solutions and see
       what fits best for your use case.
   
