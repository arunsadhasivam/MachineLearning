
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
        LLM
