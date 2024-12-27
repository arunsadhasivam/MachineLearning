Hit Rate:
=========

![image](https://github.com/user-attachments/assets/b7950eba-fcc6-4856-af32-429e7177efb3)


- Having the high performance Retriever is key to the RAG systems.
  ![image](https://github.com/user-attachments/assets/cd5c1ee6-285e-4974-8aef-c31537d3a461)


Definition:
===========

Def: fraction of the queries where the correct context is found within the top-k retrieved contexts.

![image](https://github.com/user-attachments/assets/4032228a-ea6b-4d55-b468-4e14beabd9b6)


- Above Query Q1 , Retrieved Nodes (N1,N2,N3) where N1 is Actual answer
- 2nd N3 is actual node in the retrieved Node (N3,N5,N1)
- 3nd no node is retrieved in the result. where expected in result node is N3 but
  returned N1,N2,N4

  Challenges:
  ===========

  As you can see in screen shot Q1 retrieved by Retriever1, Retriever2 where Retriever1 retrieves the expected
  Actual Node N1 in the last positional index. where Retriever Node2 retrieves in the first position.
  

 Mean reciprocal Rank (MRR)
 ============================

![image](https://github.com/user-attachments/assets/90cca297-b88a-4b3a-a1a4-6fabfd7607f7)

![image](https://github.com/user-attachments/assets/a42b3a76-9c5e-4f30-bc36-70d868263c74)


since positional index of Actual Node (N1) expected in search results is 3 so 1/3.


![image](https://github.com/user-attachments/assets/06a2173c-781f-484d-86b0-47236df5370c)




here above  positional index of Actual Node (N3) expected in search results is 1 so 1/1.
![image](https://github.com/user-attachments/assets/067fa43b-559b-44db-bad0-0260f3bde258)

![image](https://github.com/user-attachments/assets/c949cde3-21cf-453b-870a-ef3f14cd930e)

 
