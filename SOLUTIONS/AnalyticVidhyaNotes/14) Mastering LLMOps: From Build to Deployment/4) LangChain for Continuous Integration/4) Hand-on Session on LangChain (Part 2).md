Hand-on Session on LangChain (Part 2):
=======================================

   - langchain for major providers have packages automatically present.
   - so we have langchain_openai package available.

![image](https://github.com/user-attachments/assets/514013ed-684e-4ac5-a650-1a29085fd241)

   - the authentication was then used using key that was provided before.
   - this output has
     1) the prompt tokens,
     2)  completitions_tokens were created by,
     3)  response,
     4)  model_name,
     5)  fingerprint which is representation , a hash value of the whole request.
     6)  finish_reason
     7)  logProbs
     8)  id

 - Response also one of the Object called as AIMessage.
 - this helps us to modularize the code really well.
 - this helps to plug in and play with multiple other modeules which works seamlessly as well.
 - llm.invoke() see the AIMessage was generated.
 - to change the model, just need to change the model-name from "gpt-4o-mini" to  "gpt-40" and this
   simply changes the model.
 - so this also be given in the docs that you open up  for specifically open langchain openai docs for this package
   inside that you can just go to chat-openai and see what all input parameters are supported.
 - As you can see , rather than having to hardcode this into our code, these are parameters which can be saved at other
   places and then injected at runtime.
 - so we have the model name , 
     
