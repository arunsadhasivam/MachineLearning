Hands-On: Understanding Runnables LCEL:
========================================

![image](https://github.com/user-attachments/assets/b8ceb89f-aec1-421b-add2-d55aab3c2553)


- idea of writer , reviewer chain and another chain to combine to get refined research report
- in this how can we put in 1 in an organized fashion.
- understand core concepts in langchain.
- question of what is chain under hood and finally look at runnable in langchain and LCEL and so on.


![image](https://github.com/user-attachments/assets/58dc4b04-4820-474b-949b-01c800ce3a74)


Runnables:
===========


- copy the writer and reviewer chain of previous section
- also copy final writer

Writer :
========



       from langchain_openai import ChatOpenAI
        from langchain_core.prompts import ChatPromptTemplate
        from langchain_core.output_parsers import StrOutputParser
        from IPython.display import Markdown
      
      
        llm = ChatOpenAI(model='gpt-40-mini',temperature=0)
        prompt =  ChatPromptTemplate.from_message([ ( 'system', 'you are a research assistant'),('user','{input}')])
       output_parser = StrOutputParser()
       basic_chain = prompt| llm|output_parser
      
       output=basic_chain.invoke({'input','write a 3 bullet point summary of how transformer worker'})
       Markdown(output)
      
 ![image](https://github.com/user-attachments/assets/e1c66fbf-eb65-4a86-bf30-9ab36aad2360)
      
      //draft of research report using chains in langchain
      //first setup writer_msg
      WRITER_SYS_MSG ="""you are research assistant and scientific writer. you can take in requests about topics and
      write organized research reports"""
      prompt =ChatPromptTemplate.from_messages([('system',WRITER_SYS_MSG),
                                                ('human','write an organized research report{input}')
                                              ])


Reviewer :
=================



          REVIEWER_SYS_MSG ="""you are a reviewer  for research reports"""
           prompt_reviewer =ChatPromptTemplate.from_messages([('system',REVIEWER_MSG),
                                                             ('human','provide feedback on this research paper{report}\n.
                                                             as concise as 5 concise bullet points')])
       
          llm_reviewer =ChatOpenAI(model = 'gpt-40-mini',temperature=0.2) //since reviewer we want interesting feedback.
          review_chain = prompt_reviewer|llm_reviewer|output_parsers
          feedback_output = review_chain.invoke({'report':output) //from previoius output line 10
          Markdown(feedback_output)


Final Writer :
===============

      FINAL_WRITER_MSG="""Final draft with incorporating the write report and feedback report by reviewer"""
      prompt_final_writer = ChatPromptTemplate.from_message([('system',FINAL_WRITER_MSG),
                                                             ('human','Write  a reviewed and improved version of 
                                                               research report'{report}, based on feedback{feedback})
                                                            ])
     llm_final_writer = chatOpenAI(model='gpt-40-mini',temperature=0.2)
     chain_final_writer = prompt_final_writer | llm_final_writer| output_parser
      output_final_report = chain_final_writer.invoke({'report':output,'feedback':feedback_output})



Optimizing using Runnable the above 3 chains:
================================================

![image](https://github.com/user-attachments/assets/f8fa27a2-9a27-4112-8625-5b5ef02a2e20)



- all these chains above are of same type of object RunnableSequence.
- they are build in very simpler way
- what is a runnable sequence.
- so langchain implements Runnable interface just this interface that allows for the chaining of building blocks that
  we see when we combine things like model,prompt,output_praser and putting things together and so on.
- this runnable protocol or runnable interface allows to combine this object in a interesting way.
- understand this chaining and composition methods work in more deeply
- we can actually inspect how they work from scratch.
![image](https://github.com/user-attachments/assets/70ea6368-9d91-4aee-b102-cf6550562e6a)
- we can import RunnableSequence and RunnableLamba
- define couple of function , what is runnable sequence , answer is a sequence of runnables
- Runnable is something you can run
- Runnable is essentially a object with standard methods like invoke(), batch() and other methods.
- idea is you can compose these objects together to create a pipeline of operations
  

       def sumitself(val :int) -> int:
         return val+val;
       
       def multiplyitself(val:int) ->int:
         return val*val;

 - so now we can actually define runnable

       runnable1= RunnableLambda(sumitself);

 - now we can actually define runnable1 which is runnableLambda and give the operation to runnableLambda
 - now instead of being just a function , now we have composable operation called runnable1
 
         runnable2= RunnableLambda(multiplyitself);

 - now do same for multiple
 - now define runnable sequence.
        runnablesequence = RunnableSequence(first= runnable1, last= runnable2)
 - now we can say runnablesequence.invoke(2)
        runnablesequence.invoke(2)  #16

![image](https://github.com/user-attachments/assets/d48b5c92-8937-4fa8-8ae1-10549bd850e8)

   
 - first goes to sumitself(2)-> 2+2 =4 and then go to multiplyitself(4*4)= 16.
 - so we just chain together these 2 operations , in langchain it is what happenning.
 - when we chain these operations, we can chain these operations on the top of text, we can chain together.
 - we now use this runnable logic and we try to put these chain together.
 - we can chain these operations that essentially operate on top of the text. 
 - think about what we put together?
 - we want to put together 3 chain(writer,reviewer,final_chain)
 - to put this logic together , we need to route, what are the things we need to route
 - create a 3 chain and input chain for each of the chain.
 - create a input for writer chain(topic)
 - create a input for review chain(report)
 - create a input for the final chain which takes both the report and feedback
 - now consider what comes out of the writer chain, the writer chain otutput the report
 - so writer chain output the report
![image](https://github.com/user-attachments/assets/cf71b1ac-c2f5-4e79-98db-ccc3845a3180)

 - we need a way to setup this idea to route
 - what comes out of writer chain , it goes as input to review chain.
![image](https://github.com/user-attachments/assets/05226217-610c-4ab2-83c7-e4b2286b0f48)

 - so this routing procedure that we need to implement , go to draw in green.
 - what comes of writer is a report , that goes to review chain.
 - we also need to have a way to say, what comes out of review chain is feedback.
 - so finall we need to say output of writer report and output of review route to final writer chain.

![image](https://github.com/user-attachments/assets/0058501f-9808-4748-aa0f-6676bb02ebe2)
 
 - route review and feeback to finalwriter chain.

 
Runnable Pass Through:
=======================

![image](https://github.com/user-attachments/assets/e1ba16d3-edb4-4129-90eb-c6b20dda85de)

 - to do output feedback or route to input of another i.e output of report route to review route and output of review
   and report route to finalwriter we need runnable Pass through.
![image](https://github.com/user-attachments/assets/2c9e15f1-1b8b-4e2e-bc88-98a1fd27bed8)


 - above what we are doing is create a composedChain and assign writer_chain output to report

       RunnablePassthrough.assign(feedback=review_chain)
![image](https://github.com/user-attachments/assets/b467c524-10a1-4218-91ab-e5a1216ad917)

 - now use runnable passthrough to pass the feedback of whatever comes out of review_chain.

       composed_chain = {'report': writer_chain} | RunnablePassthrough().assign(feedback=review_chain)

 - once we assigned report( 'report':writer_chain} to some thing , it is **indischain for ever** .
 - so all the upcoming chain (feeback=review_chain) got to know about it.
 - so now we assign this , now we gave information about the important feedback( RunnablePasstrhough().assign(feedback=review_chain) 
       
