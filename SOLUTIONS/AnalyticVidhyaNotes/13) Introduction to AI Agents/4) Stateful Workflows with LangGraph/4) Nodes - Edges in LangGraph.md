Nodes - Edges in LangGraph:
===========================

  - introduced langGraph which allows you to have semi-deterministic control flows that leverage agentic workflow
  - and it implement some state, which is a datastructure that evolves over time as it passes through these nodes
    which implement python function,and they are routed through the edges that lead from one node to other node.
    based on the decision that is implemented by the logic of the function for the conditional edge.
  - thats all great, but we have to understand little more about nodes and edge , if we really want to have
    an overview and good idea of how thats actually implemented in practice.
  - thats defintiely going to compound as we go into hands on session and actually put everything in practice.

Nodes:
=======

  - so nodes are the core functions units in langraph

![image](https://github.com/user-attachments/assets/93f151c8-10be-4482-bb75-364500445eac)

Functionality:
=============    
  - what is functionality?
  - as we said before a node is a python function that process current state and output an updated state.

Execution:
==========
  - Nodes can run synchronously or asynchronously  and are added to the graph using add_node method.
  - thats the method to put node in to graph.

Special Nodes:
===============
  - includes START and END nodes to manage the flow execution in the graph.


  - Edges define the routing logic in langGraph:

Types of Edge:
===============
![image](https://github.com/user-attachments/assets/1fa4d1f1-d628-488e-a1b7-000b448b34f2)

  - Normal Edge - Direct Transitions from one node to another.
  - Condition Edge - Determine the next Node(s) to execute based on  a function's output.
  - Entry Points - Specify which node to invoke first based on user input.

Parallel Execution:
====================

  - Multiple outgoing edges from a node can trigger parallel execution of destination nodes.

NOTE:
=====
  - any one who draws a diagram can understand easily.



