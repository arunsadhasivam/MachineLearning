LangGraph Components:
=====================

  - LangGraph is a graph based approach to model a agentic workflow and we introduced the core principles behind it.
    like controllability, streaming etc.


LangGraph components:
======================

![image](https://github.com/user-attachments/assets/64ffebef-c8b6-422c-a630-1ebe30116878)

basic components of graph are:

  1) Nodes
  2) Edges
  3) Conditional Edges - edge that has decision to make , so that it can route information to different route
                         depending on some decision that made with in the node involved.


1.Node:
=======

![image](https://github.com/user-attachments/assets/26b279a8-52ca-4711-8287-a3a0d48a2fd0)

   - Node is a python function that implements logic of events.taking the current state input and return updated state.
   - we going to start with a state
   - then the state going to have series of transformations that is defined by the logic of python function implemented with in those
     nodes.

2.Edges:
========

![image](https://github.com/user-attachments/assets/c6c75e9f-12f8-4bd5-855b-7fe88aa29b62)

    - Edges and conditional edges are the basic foundational components in langGraph.
    - these are going to functions that implements Fixed or conditional transitions to determine which node to execute
      next based on current state.

