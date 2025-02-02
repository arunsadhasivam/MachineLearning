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
      
      
        llm = ChatOpenAI(model='gpt-40-mini')
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


