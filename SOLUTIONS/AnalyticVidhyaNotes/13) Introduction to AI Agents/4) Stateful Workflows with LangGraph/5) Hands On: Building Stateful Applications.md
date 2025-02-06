Hands On: Building Stateful Applications:
===========================================


![image](https://github.com/user-attachments/assets/dfccb657-db54-4a3d-821f-9c2fbb059c7f)


- hands on LangGraph
- start with simple graph to get started to understand inner working to understanding Agentic workflows.
  

Step 1: define State:
=======================

  - use typing to define state
  - you can use type dict as parameter
  - question behind building a state in langGraph is:
    1) what are the attributes that are worth keeping throughout the execution of workflow?
    2) what do we want to keep track of.
    3) what intermediatory artifact are useful for debugging the applications.

![image](https://github.com/user-attachments/assets/4c535ca4-947d-46b3-92ab-17114ae570ef)

  - we are going to say attribute1 to a string , attribute to a string.
  - what we do now is build logic to transform the state.
  - so what are we going to do? we are going to define a function.
  - define function, so it is going to take objects of some state and we are going to update the state when going
    through this function.
  - now we have function, which takes in some state class which inherit from typeDict . and it changes
    one of its attributes and return that updated state.now we have a graph of some sort.
  - we can actually play with it.


Step 2: create a graph:
=========================

  - create a graph equal to state graph and with someState

![image](https://github.com/user-attachments/assets/9ffa24b3-a2d3-4e5c-b32a-098bc9b0917f)

  - create a node
  - create a edge for that , we need another node in order to create a edge.
  - but how about if other node is the one that terminates the execution of the graph.
  - it is simple lang graph
  - from langGraph we import special node END to end the execution of the graph.
  - now , we can add the edge between node1 and node END we just imported or created.
  - we can actually set , how do we start the graph.
  - how do we set the flow of execution.
  - whats the flow of execution?

![image](https://github.com/user-attachments/assets/0dce5bb9-8e17-49bd-9463-aee1664c931b)

  - we can say graph.set_entry_point('node1')
  - we are setting entrypoint to node1 and execution of graph starts from node1
  - now, lets compile the graph.

![image](https://github.com/user-attachments/assets/30e36402-14db-403d-b442-8b43dddcaf96)


Step 3:compile and visualize graph:
===================================
  - compiled_graph = graph.compile() now you have compiled graph.


![image](https://github.com/user-attachments/assets/a17e0227-9b88-479d-a2bc-a5a115f137ed)

  - visualize the graph.
  - now , you can clearly see the flow as above.

Note:
=====
![image](https://github.com/user-attachments/assets/4d25e4e4-a5e9-47f0-9318-9b3b9d83222c)
![image](https://github.com/user-attachments/assets/45da9290-a26a-4704-be1b-46b64cc50cda)

  - compiled graph is nothing more , if we go to the compiled_graph type , we get the compiled state graph.
  - if we see type , we see it is inherit from the runnable protocol.
![image](https://github.com/user-attachments/assets/40b35171-246e-441e-8b73-490af5993897)
![image](https://github.com/user-attachments/assets/7c4bf5dd-51c5-4b62-8187-df4cc256af20)

  - compiled_graph.invoke( ) pass the attributes
  - we did not need to have input just attributes, so initialize the attributes
  - we can see the attribute1 was changed throughout the execution of graph and attribute2 remain same.

Summary:
=========

    - we know understand adding node, edge
    - putting functionlities together.
