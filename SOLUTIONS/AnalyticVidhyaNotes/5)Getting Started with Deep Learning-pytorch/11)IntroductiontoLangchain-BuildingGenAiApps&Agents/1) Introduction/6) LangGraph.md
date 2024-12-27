
LangGraph:
=========



- Langraph build on top of langchain,facilitates the cyclical graph structure.
- Main features:
  
   - **Nodes** - functions or langchain Runnable objects such as tools
  
   - **Edges** - specify directional paths between nodes
  
   - **Stateful Graphs**: Manage and update state objects  while processing data through nodes.
 

Flow:
=====
        LLM -----> run agent <------ run tools
                        \              /
                          \           /
                            \        /
                             Tool_calls
                                 |
                                 V
                                 End  
           


Cycles:
=======


      Task ---> Tools ----->
        |     /       <-----  Environment
        |   /
        V  V ---| Reasoning loop
        LLM-----| 

- Let says question " who won world cup" llm reason checks knowledge base whether it has information.
- let says chatgpt only have info till 2022, so this reasoning cycle helps to reason whether " i have
  info on worldcup 2022. so it reason, if it does not have it searches google and build knowledge base.
 - cycle is first thought, decision, action- this is cycle loop to model agent as graph

 
