Levels of Agents Complexity:
==============================

  - what agents are?
  - it is a combination of ability to think given by llm , ability to perform action in realword given by tools
    like different python functions
  - different python functions do different actions like weather, search.
  - some common implementation of agents.
  - Agent practical implementation is agent complex.
    

Agent in 3 levels of Agent complexity:
============================================

![image](https://github.com/user-attachments/assets/548bb9a4-a0e7-403d-9800-60080486b48b)


- first level is understanding how you can connect llm through a python function that you have in some script.
- inorder to allow the model to understand when you should call specific function to solve the problem,the model
  understand it cannot solve by itself.
- level 1 inspired by toolformer.
![image](https://github.com/user-attachments/assets/7861edba-65ea-4483-a63d-90378f1bec45)
- above is basic implementation of agent at level1.
- it takes a promt a input question, model type (gpt-3.5-turbo)
- it calls the open api with the system_level api like "you are a helpful researcher"
- then you send a prompt to the model
- then you retrieve response as string.
- here function takes input and output text.

- set of 3 function
  1) create_directory().
  2) create_file()
  3) list_files()

- output should be python function nothing else.
- idea is model can identify what the task involve, in this case create folder, create file , list files
- when we call a model with particular prompt, where outline what is the task and also list the function available.
- the model identitifies that it should use function create_directory() to create.
- Also each function has task description, this shows that the model can understand the context of the tasks and use tools to solve the
  task.
- that is level llm+functions inside of prompt. (LEVEL 1)
- in order to call from model to become a natural action in the real world.
- i mean with in my computer, we need to find a way to execute a function.
- we could use python built in exec method for that.

![image](https://github.com/user-attachments/assets/9ae04ef7-8237-4e94-ae83-723579732b40)

- exec string output like exec("model."+output) function of model connected to class of model via "model."
- idea is that you can exec function call that was identified and properly written by llm and then in this
  example below demonstrated folder created.

- the main idea is that you can explain to the model , which functions has been available to the  model
  and then model can identify which function to call given proper argument.

Limitations:
================

![image](https://github.com/user-attachments/assets/49df58b8-040a-43bb-801b-eada0c6035d1)

- probabilistic output make function calls unreliable.
- Need a structure way to prepare the input for function calls.
- putting entire function inside text prompt is clunky and non-scalable.


  Solutions:
  ==========

  - we could use openAI function calling(recently released fine tune model).
  - we could use open AI recently recently released fine tuned Models they have ability to call python functions
    as a way to get around the limiations.
  - that is level 2 of agent complexity.

openAI's Function calling API:
==============================


![image](https://github.com/user-attachments/assets/97ec2725-fabb-407d-9854-be25d1e99a27)

- standard way to connect model outside tools.


Steps:
======

![image](https://github.com/user-attachments/assets/c26fa11e-f9ff-44be-9b74-81c1cc61cfa4)

1) call the model with user query and set of functions defined in function's parameters
2) The model can choose to call one or more functions , if so the content will be stringified JSON object
   adhering to your custom schema.
3) parse the String in JSON in your code, and call your function with provided arguments if they exist.
4) call the model again by appending the function response as a new message.

- when we have a function calling in this way
- then the model has initial query,
- then the model if the model identifies it needs to call a function, it will call a function.
- it will go through the process of preparing the proper input for the function.
- output as a JSON object, they will be parsing the code.
- then we call the function , with the provided arguments the model will also provide automatically.
- what we can do is we can take the information from the output of this function call + initial query and
  append to the messages parameter in the open AI which is essentially the history of messages called.
- now the model knows what happened, what is the initial query, what is the output of function, model can
   summarize the proper response to the user.
![image](https://github.com/user-attachments/assets/aa19872d-2eae-44d4-98a0-ccdde14faeff)

- one way to implement is to taking the example from create directory function that we did earlier.
- we could have the function that takes the input directory name and then we have dictionary description
  of the function (name of variable to create directory, type is function, function is name to create directory,description)
- it has explanations of the parameters involved, the properties of those parameters and then which parameters are required.
- in this case just 1 parameters (name)
- which is required.
- we put this in list , you know multiple tools , multiple function if that is the case.
![image](https://github.com/user-attachments/assets/331587d7-2b75-49ee-8498-a07c0bcc4a6b)

- we have function that run through the entire loop for us.
- so we start with the messages list containing the prompt from the user.
- so containing the task create a folder called 'lucas-agent-master' etc
- then we have the list with tools and then we call api first in this case 'gpt-3.5-turbo'
- we give the message list, list of tools and we set the choice automatic

- we retrieve the response from the model.
- we would then identify we wouldn't check if any tool calls, meaning calling this specific tool that was made
  available to the model.
- if that was made during the process.
- if the model idenitify have the call of the  tool, then we go to the next step which would be to essentially first
  append the responose that was given by the model to the messages list.
  

![image](https://github.com/user-attachments/assets/d99209c4-9cc9-4a74-bde5-191c8043e7b4)

- then we loop over the tool calls that were made by model , we would retrieve the name of the function,
  which function in our current scope of our script should be called, the arguments, we would call the
  fucntion with those arguments with this line : function to call and then we append the response to the
  messages list again.

![image](https://github.com/user-attachments/assets/1e2c169f-1d08-425b-bb50-f05e176a9e1d)

- finally we would retrieve the second response from the model by sending all that and the message parameters
- that would be our entire loop, which would involve true call to openai api (truecall + execution of function).
- that would be level 2 of complexity that we have ability to connect models to tools in a more structured and more
  organized and deterministic way.
- level 3 in the next video.
