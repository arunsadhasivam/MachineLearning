Hands-On: Simple Chains:
========================


Chain in langchain:
====================

    - how to build chain and how it work
    - interesting things we can do in chain.


CODE:
====


      from langchain_openai import ChatOpenAI
      from langchain_core.prompts import ChatPromptTemplate
      from langchain_core.output_parsers import StrOutputParser
      from IPython.display import Markdown


      llm = ChatOpenAI(model='gpt-40-mini')
      prompt = ChatPromptTemplate.from_message([('system','you are a research assistant'),
                                                ('user','{input}')])
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


  
  ![image](https://github.com/user-attachments/assets/bda295b1-1c13-42a6-8f86-02026ee1ff68)

![image](https://github.com/user-attachments/assets/e64757ae-80af-4d29-a01d-c9bdc0644e3f)

  - temperature - how random the message from the llm ( 1 more random, if 0 stable result)
  - when set to high, less likely tokens will be more likely
  - when set to low , you dont do anything to output probability distribution of next token
  - so it is as precise as possible
    ![image](https://github.com/user-attachments/assets/293e92c7-e5e9-490a-b8b1-cfee0469c075)

      llm = chatOpenAI(model='gpt-40-mini',temperature=0)
      output_parser = StrOutputParser()
      writer_chain = prompt|llm|output_parser
      output = writer_chain.invoke({'topic':'how do transformers work for non AI researchers?'}) //line 10
      Markdown(output)


    ![image](https://github.com/user-attachments/assets/5e4306a0-bbdc-45d3-a170-5b037c134000)
![image](https://github.com/user-attachments/assets/9800e5f8-eb3e-4d40-806f-11a64de280c2)


  above output is good, reviewer chain 

    REVIEWER_SYS_MSG ="""you are a reviewer  for research reports"""
    prompt_reviewer =ChatPromptTemplate.from_messages([('system',REVIEWER_MSG),
                                                      ('human','provide feedback on this research paper{report}\n.as concise as 5 concise bullet points')])

   llm_reviewer =ChatOpenAI(model = 'gpt-40-mini',temperature=0.2) //since reviewer we want interesting feedback.
   review_chain = prompt_reviewer|llm_reviewer|output_parsers
   feedback_output = review_chain.invoke({'report':output) //from previoius output line 10
   Markdown(feedback_output)
    ![image](https://github.com/user-attachments/assets/a276f925-5ba0-4a71-9984-135c8adf6f1f)

![image](https://github.com/user-attachments/assets/56415847-4387-4b35-935d-ad1ecc97f3fc)


- now we way chain to write a report and chain to review the report
- write report we use temparature 0 to avoid unnecessary predictions or unlikely words to be predicted in probability density function.
- in review report we have temperature 0.2 to allow some interesting feedback review.
- write all together write a final draft with incorporating the write report and feedback from the review feedback output
  and provide final draft.


    FINAL_WRITER_MSG="""Final draft with incorporating the write report and feedback report by reviewer"""
    prompt_final_writer = ChatPromptTemplate.from_message([('system',FINAL_WRITER_MSG),
                                                           ('human','Write  a reviewed and improved version of 
                                                             research report'{report}, based on feedback{feedback})
                                                          ])
   llm_final_writer = chatOpenAI(model='gpt-40-mini',temperature=0.2)
   chain_final_writer = prompt_final_writer | llm_final_writer| output_parser
    output_final_report = chain_final_writer.invoke({'report':output,'feedback':feedback_output})
   

![image](https://github.com/user-attachments/assets/5622e954-d770-4c57-b54a-fcf61ede8cb2)

 ![image](https://github.com/user-attachments/assets/5f001668-5649-4424-8340-ac651fb8b013)
                                                          
![image](https://github.com/user-attachments/assets/9888b1dc-7b3f-44b3-bc9c-bbb8d0a9b62a)

![image](https://github.com/user-attachments/assets/43549590-6d3e-48b5-8e61-d232b93acaa2)
            

- above is well organized, reviewed full report
