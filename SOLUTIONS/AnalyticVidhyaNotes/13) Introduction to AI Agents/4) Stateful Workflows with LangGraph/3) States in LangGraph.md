States in LangGraph:
=====================


  - previous video talked about how langGraph model things as graph.
  - and we just mentioned about foundational components nodes and edges, as we talked about  **node
    as python function that going to transform a state of the graph**.
  - but we do not introduce what the state was, which is was we are going to do now.



![image](https://github.com/user-attachments/assets/c3bc8e6d-d172-45ee-a512-921b0b303d3f)

States:
=========

  - States in langGraph are essentially **shared data structure** that evolve over time as these workflow 
    are executed and they pass messages along these edges.


Message Passing:
================

  - Besides that graph in langGraph is driven by message passing, which is the passing of information
    when we more like directly , when we talked about autogen.
  - we talked about how autogen implements some control flows and some customizability for controlling
    how agents interact with each other and exchange message between each other.
  - langChain is also going to have control over the message passing.
  - however , here it is going to be about nodes sending messages to activate other nodes which facilitates
    the execution of workflows in discreate iterations of super steps.
  - the idea that we want to keep in mind is :
      1) you going to have state which is a datastructure evolve over time   as nodes gets executed
      2) and you have passing of information between nodes.

