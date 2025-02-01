Hands-On: LangChain Basics:
============================

![image](https://github.com/user-attachments/assets/efea126c-2988-4c92-8b96-ea2634559497)

Step 1: install dependencies:
==============================

![image](https://github.com/user-attachments/assets/cb0dcd0d-cff6-40fb-9ba5-07da8b335be1)


Step 2: openAi Key:
====================

![image](https://github.com/user-attachments/assets/c31f98eb-b7b1-458e-a93b-a09ad099dc40)




Step 3: load Model:
====================

![image](https://github.com/user-attachments/assets/b91b8892-264e-4e75-8697-81edabdd4c44)
![image](https://github.com/user-attachments/assets/b7e09930-f46c-42db-bf47-7b903cc3e89b)


Step 4: prompt template Model:
================================

![image](https://github.com/user-attachments/assets/59395a00-277a-4930-8e49-afd868c5e8cb)
![image](https://github.com/user-attachments/assets/06573f41-9fb0-4031-b6b6-3697c0437a7a)


step 5: dynamic variable:
=========================

![image](https://github.com/user-attachments/assets/10462b54-8e45-4a79-83bb-abc6c1ee9c1e)

Assign value to dynamic variable

  prompt.format("things_to_give_example_of","basics components in langchain")

![image](https://github.com/user-attachments/assets/90b5743b-79f5-4eb9-b3f3-f7da1643ac00)


step 6: set chain and invoke:
=================================

![image](https://github.com/user-attachments/assets/4e75e2a3-3f6e-4eed-870c-9ba12efa0df6)

  - building block combination of prompt and llm
  - it is composed of something called LCEL(Langchain expression language) denoted by pipe.
  - invoke over the chain.

      basic_chain.invoke("thig_to_give_examples_of":"basics components in langchain");
![image](https://github.com/user-attachments/assets/48ad07f6-bffd-42a6-977a-854d7de075ac)


As you can see repsone is in AIMessage() to get as text use output parser.

step 7: outputParser:
=====================


![image](https://github.com/user-attachments/assets/5f9d3868-b7b5-42d4-b417-31015ba0c8bf)

complete chain : 
================

          prompt + llm+ output parser

  from langchain_openai import ChatOpenAI
  llm = ChatOpenAI(model='gpt-40-mini')
  llm.invoke("teaching about langchain") //simple


  //prompt
  from langchain_core.prompts import ChatPromptTemplate
  prompt= chatPromptTemplate.from_template("give me 5 examples of :{thing_to_give_examples_of}")
  prompt.format(things_to_give_examples_of="basics components in langchain")

 //chain
 basic_chain = prompt|llm|
 basic_chain.invoke({"thing_to_give_examples_of":"basic components in langchain"})
 //output will be like AIMessage("langchain is a framework...") like this

  //output parser for formatting the above AIMessage output
  //complete chain - prompt + llm + output_parser
  from langchain_core.output_parsers import StrOutputParser
  output_parser = StrOutputParser()
  complete_chain = prompt|llm|output_parser
  complete_chain.invoke({'thing_to_give_examples_of':'basics components in langchain'})
  

 

