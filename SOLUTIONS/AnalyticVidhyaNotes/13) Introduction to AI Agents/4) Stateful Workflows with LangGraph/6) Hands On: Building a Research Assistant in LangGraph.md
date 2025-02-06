Hands On: Building a Research Assistant in LangGraph:
======================================================


Task:
=====

   - we saw absolute basics
   - we know how to build statefull applications.
   - we say how node works, we know how graph works.
   - we know compiled graph.
   - lets do something with functionality.
   - lets build simple research assistant.


   Step 1:
   =======
![image](https://github.com/user-attachments/assets/e5469dbc-b209-4ea1-af94-7fabc9927542)

     - imports all the needed
     - set the temperature to 0 for chatOpenAPI

  Step 2:
  =======

      - define 2 function.
      - define should_continue() which takes state messageState 
      - it stores the list of messages that will be stored in exchange to route the execution of flow.
      - we get the last message. if last message is tool_call return 'tools' which are the id for the node response buffer
        which we will do later.
      - else end of the execution of graph.

![image](https://github.com/user-attachments/assets/6809ce82-c909-46f8-a647-f21008f8b74c)

      - the logic is search or return to the user.

      - Another logic for calling model we say call_model which also take state -> messageState
      - it is going to take up messages and then it going to invoke llm that we set up on those messages.
      - that means we have list of messages that we have exchange after that point.
      - so this llm have all the context from those messages when it is producing an output.

![image](https://github.com/user-attachments/assets/b6343db6-7eea-43af-81ce-f42ffca481df)


      - then this is going to return dict with those messages which is going to be essentially 
        updated state of the graph.

Step 3:set up the state :
=========================

  
  graph = StateGraph(messageState)

  -  now , we are going to set up the state.
  - then add the agent node 'agent' and associate with the call_modell
  - also going to create a search_tool by giving the TavilySearchResults(max_results=5)
  - then setting up tool list , give tools=[search_tool]
  - we put under toolnode . i.e we put tools under tool_node
  - then add to the graph.add_node('ootls',tool_node)
  - set up the start node to start the execution.
![image](https://github.com/user-attachments/assets/05ee842a-5f22-4910-a3b0-32b064afa464)

Step 3:set up the state and compile:
=====================================

![image](https://github.com/user-attachments/assets/798d62ef-c3f9-4001-aa4c-23d14dfb182d)

  - we going to set the start of execution flow to the agent with 'agent' node by setting_entry_point as 'agent'
  - which is going to process the input some how.
  - we have conditional_edge between 'agent' and should_continue() function which implement conditional logic
  - in conditional function we are saying either continue search or return result.
  - it will be search , search ,search then result.
![image](https://github.com/user-attachments/assets/999d96b0-8787-4411-a8a2-b0582f1c5736)


  - then we have direct edge between tool and agent.
  - i.e that after tool executes whatever search it did , it will return to the agent.
  - the agent will be able to compile the response for the user instead of just being send.
  - now consider graph.compile()
  - once compiled, again we can visualize with Image(graph_compile.get_graph().draw_mermaid_png())
  - now you can test

Step 4:test the graph:
=========================  

    output = graph_compile.invoke({'messages':[('user','write a simpler report on how to use AI for productivity')]}}

![image](https://github.com/user-attachments/assets/e5cd296a-9af8-470b-9e48-7bd918bf97f7)


![image](https://github.com/user-attachments/assets/284d64d8-45a7-4373-849f-b68da8b17100)


- we get a wonderful research report from research agent.
