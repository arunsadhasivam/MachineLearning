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
 - so we have the model name , temperature , max_no_of_tokens we looking far and then we call invoke()
 - based on temperature, if 2 more creative as hyperparameter.
     
![image](https://github.com/user-attachments/assets/9442e443-6e1c-4f32-953f-c17cae982ec7)


 - if we want to parse the output, we just care about the final output , we can use output_parsers.
 - you can mention we are looking for csv or json.
 - we pass the output of stringOutputParsers
 - one of the things the llm provides is (|) pipe operator it can added at the front to create a chain.
 - after it run it can simply pass to the next set of input.

![image](https://github.com/user-attachments/assets/2717962f-2b1d-41d5-be73-ef969c845e6f)


 - you can the output_parser does not care about the full fledged response, but only the final response that is generated.
 - if it is a json parser , it makes sure json output is created.
