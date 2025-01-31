Messages and Prompts:
======================

  - how they introduce components and off shelfs.


  first components - which is just abstraction over many possible llm apis


  other important components:
  ==============================

- prompt template - one of the essential components in langchain and it is essentially an abstraction over the 
  traditional text prompt.
- what a prompt is ? essential a piece of text send to the model.
- every time you interact with the llm and you send a text that is our prompt.
- what langchain does with prompt template is very interesting.
![image](https://github.com/user-attachments/assets/b10c3aa5-668f-43bc-9695-120ec653198a)
- obviously you can just have the string that you send to the model and may be if you want to control
  specific aspects of what you send to the model but you want to keep the rest of the text intact
  you could use something like formatting in python or fstream allow you to change the text that is been
  send to the model.
- however what langchain does it with prompt template is they make it so that prompt can allow you to
  create dynamic variables.
- in this example here, strings are "show me 5 examples of the concept {"concept"}
- so we want example of any concept we can change which concept we use when we are calling the model which allows
  to create some functionality that can change just the concept that we are generating examples for and keeping the
  rest intact. that is one of the usecases for modular implementations of abstractions of prompt template that
  langchain makes it possible.
- in this case, we are saying show me 5 examples of this concept that we are formatting the prompt to animal
- so you want them the concept to be animal it could be animal or exercises for calculus.

  
        

