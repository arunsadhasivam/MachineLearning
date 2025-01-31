Output Parsers:
=================

  - components of langchain
  - 1) like model calling llm provider api
  - 2) prompt - allow you create dynamic variables make it modular pieces of llm workflow.
  - 3) output parser - the output parser is an abstraction for parsing the output that come out of llm.


![image](https://github.com/user-attachments/assets/33e6c913-7755-4cff-a562-a6e2dacf14b3)

  - idea here is essentially that you want to translate some output that comes from the model to a workable format.
  - this idea you can think about the transforming the list to string or string to list or dictionary to string or
    string to dictionary
  - the example here is custom implementation of output parser that parses the string and uses the comma to create
    list.
  - the relevance of the output parser is that one put together with the modal components and prompt component.
  - it gives you the foundational building block that we are going to cover next called chain.
  - it allows you to treat workflows with the llm as a composition of these building block.
  - the output parser allows you to control for what comes out of the building blocks.



  

