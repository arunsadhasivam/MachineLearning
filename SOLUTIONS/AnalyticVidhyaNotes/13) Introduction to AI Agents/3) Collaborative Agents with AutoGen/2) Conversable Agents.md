
![image](https://github.com/user-attachments/assets/695a2033-9815-4471-9a69-ff064057967b)


Conversable Agents:
====================

  - very useful framework for implementing conversable agent.
  - what are conversable agents.
  - conversation agent are essentially entity that has specific role that can pass message
    between the chat so that can send and receive information to and from other conversible agents.
  - e.g to start or continue conversation.

cutomizable:
=============

  - they can configure based on application specific needs.
    to display complex behaviour with them multi-agent conversation.
  - researcher agent , planner agent, scientist agent, engineer agent and so that
    so you can have mix of basic backend types.


Conversable Agents:
======================


![image](https://github.com/user-attachments/assets/4c22cac2-9202-4122-a519-394d958c7ce2)
![image](https://github.com/user-attachments/assets/b41899ba-6109-4605-afad-0570de31aead)

  - one e.g of very basic implementation of this autogen is autogen.assistant agent which is the basic
    very generic agent you can have. that carry the name to identify the agent and some configuration for the llm
    behind the agent functionality.
  - conversible agents are fascinating you have the class and origin conversable agents.
  - in this e.g we set up conversable agent as a chat bot , we give it a configuration with dictionary with list
    containing modules with in the agent along with the api key with the specific model provider.
  - we set code **code_execution_config=false**  meaning we wont have the agent to execute code for us.
    which is one of the functionality autogen put forward.
  - we set the **human_input_mode=never**, meaning we dont want human in loop with in the scope of execution of the agent.
    and then we generate the reply based on some input and this case "just tell me a joke".
  - and then we implement another type of agent. so we create an another character in this context.so we create kathy
    with a specific system message that defines the certain behaviour.
      1)so your name is kathy, part of  duo of comedians,and
      2) then we have joe another comedian .
      3) and then we initiate a conversation between joe and kathy
  - so the idea with this example is just to demonstrate both the idea of conversable agent, something that's just
    a combination of model with some profile behaviour and organization of configuration for the capabilities of that
    specific agent.

   - And we show the idea of conversational programming by showing here on the bottom the initiate chat ald also the
     generic reply here at the top, where we show the different implementations of exchaning of messages between the
     agents and how they can come about. we can generate some output.right?
   - or you can initiate a conversation, which would be loop between two agents or more, etc.
   

Conversable Agents - Execution Flow:
=====================================

  - there is a certain execution flow in conversable agents which involves:
     1) importing some modules,
     2) creating a simple agent  , in this case for e.g i was showing , generate a reply
     3) then we create a some comedians as example of customizable conversable agents.
     4) they initiated a chat between those 2.
  - next we keep keep diving in to autogen and its conversational paradigm- conversational programming paradigm.
    
    
