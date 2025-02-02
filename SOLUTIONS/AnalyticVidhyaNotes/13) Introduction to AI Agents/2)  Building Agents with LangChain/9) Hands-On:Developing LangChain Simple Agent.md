Hands-On:Developing LangChain Simple Agent:
============================================

    - we go to do now is build a natural agent.
    - we use all the knowledge that we learned.


Step 1:
=======

 import warnings
 warnings.filterwarnings("ignore")


 from langchain import hub
 hub.run()


 - langchain is a database of useful prompts
 - not only prompts , bunch of runnables, chain and useful things.
 - but this only we use prompt , a useful prompt to work with agents.

![image](https://github.com/user-attachments/assets/e2b51137-90ac-41b4-9387-91179e3533a9)

    from lanchain import hub
    prompt_agent = hub.pull('hwchase17/openai-tools-agent');
![image](https://github.com/user-attachments/assets/f75963b2-0ed4-44ee-b29c-f093ab6bc750)
![image](https://github.com/user-attachments/assets/3663538b-b6c0-4047-b82f-1d2762e5ace0)

 - we inspect what prompt_agent looks like
 - it has provide out of box agent_scratchpad , input, message_history

![image](https://github.com/user-attachments/assets/db5c2870-f706-4bc4-8bf4-e8057aca4eec)

 - Agent is a combination of llm + tools
 - in langchain framework facilitates the creation of tools out of any python function by just leveraging the @tool decorator
 - lets set up along with subprocess package.
 - subprocess to write a tool to perform shell command from terminal.

@tool:
=======


![image](https://github.com/user-attachments/assets/74d7215a-cd9d-461c-8bdd-f59247d7c1b4)

     import langchain_core.tools import tool
     @tool
     def list_files():
       return subprocess.run(["ls"], stdout=subprocess.PIPE).stdout.decode('utf-8'))

      list_files.invoke({"input":""}) //it does not need any input.

BindingTo() method:
===================


  llm_with_tool = llm.bind_tools([list_files])
  llm_with_tool


  ![image](https://github.com/user-attachments/assets/83ca7203-06c6-4e31-a61c-4ac1bc6afae0)


 - we can bind to llm_tool
 - llm_with_tool is a RunnableBinding.
 - we can use model and tools to list files
 - we can test this now by checking whether this model works.

![image](https://github.com/user-attachments/assets/bcb2bba7-2cf7-4bdf-8d55-269c98064e30)
![image](https://github.com/user-attachments/assets/599dd9f5-fa80-4f37-b8d3-685321a2cb39)

 - we can see now the inspect with no content .
 - we see tool_calls, it show model detected tools should be called , and in return some structured
   information to inform whatever downstream processing should to occur that a truce call should be made.
 - we now implement the infrastructure , to actually calling tools from our computer.
 - we do now some pretty simple stuff, dictionary_with_tool_names

    dictionary_with_tool_names={ "list_files":list_files}
    output= llm_with_tool.invoke("list files in the directory", dictionary_with_tool_names)

   if output.tool_calls:
      for tool_call in output.tool_calls:
        tool_name = tool_call["name"]
        tool_args = tool_call["args"]  //also specified by model.
        tool_func = dictionary_with_tool_names[tool_name]
        tool_func.invoke(tool_args);


  - name of function tool_call["name"]
  - args of function will be under tool_call["args"] also specififed by model
  - tools actual function will be given by dictionary defined.

     
![image](https://github.com/user-attachments/assets/45854812-4ef6-4476-a2b6-3a0a3fece8c3)
   ![image](https://github.com/user-attachments/assets/b25ec608-f69f-439f-83b0-4ccb0ecf7c8b)

![image](https://github.com/user-attachments/assets/de4b0169-ad4b-4a98-b54a-583e5e55521d)
![image](https://github.com/user-attachments/assets/5f0c1516-6a11-4b39-a510-3c607a981e5b)

 
  - we want an agent , we dont just ability to just call a specific tool
![image](https://github.com/user-attachments/assets/9cac64bf-8500-4867-b43d-1de952456778)

  - we dont want to implementing lot of tool_calling above , looks like boiler plate should be handled by framework
  - langchain does lot more for us under langchain.agents.

       from langchain.agents  import create_tool_calling_agent
       
  - create_tool_calling_agent which helps to combine model with the tools
  - it going to handle the execution of tools and lot of other cool stuffs.
  - create_tool_calling_agent combines model with the tools and handle the execution of tools and other cool
    stuffs

    

    tools=[list_files]
    agent = create_tool_calling_agent(llm,tools,prompt_agent)
    agent_executor = AgentExecutor(agent=agent,tools=tool,verbose=True) #loop dynamics will executed under AgentExecutor.
    agent_executor.invoke({'input':"List files in current directory"})


![image](https://github.com/user-attachments/assets/e68bd836-980a-4e9e-959e-04cb54eda6ad)
![image](https://github.com/user-attachments/assets/04be0b05-b596-4ed1-9688-a7e4d365ce33)
![image](https://github.com/user-attachments/assets/4f6011f3-fc9e-4d47-957e-060fa60251be)
![image](https://github.com/user-attachments/assets/4638bc0d-b5c3-4cbc-a682-5ddd2c2a0607)
![image](https://github.com/user-attachments/assets/8d38630b-3f3c-4454-a541-83dfe145ab92)

  - tools as list_files  
  - Agent we call create_tool_calling_agent with parameters llm,tools,prompt_agent which we get from langchain hub.
  - AgentExecutor is runtime for agent.
  - verbose =true to visualize the agent how it performs steps that perform.
  - it implements the loop dynamics
  - so that is go to done on agent executor
  - agent executor also helps to specify the verbose to visualize the agent performing the steps
    to execute the tasks whatever we give it.

  - now not only list files but also doing something with output
  - as in output - > the model list files
  - the model organizes the response that we have jupyter notebook.
  - model essentially perform some sort of autonomous decision making on top of the calling the tools and doing something with that up.
  - that is what we expect from agent.
  - however listing the files not a fun, we want to do something more.

Search the web Tool:
=====================


  - usually involves search in the web and doing something with that information.

     from langchain_community.tools import TavilySearchResults.
      
![image](https://github.com/user-attachments/assets/01a8a788-8e18-4d3f-aa54-9774ca728c7c)

  - set the api_key for TavilyAPI KEY
  - search tools 

      search_tool = TavilySearchResults(max_results=5,search_depth="advanced" , include_answer=True)  
      search_tool.invoke('what is the capital of france')

![image](https://github.com/user-attachments/assets/0b1585ed-a303-470f-9c33-9e3a68666fc7)

  
Tools to search a file in current directory:
===============================================

![image](https://github.com/user-attachments/assets/4b547b9f-4fc9-406f-a58d-88ebda432ccf)

    @tool
    def create_file(file_path:str, content: str):
      with open(file_path,'w') as f:
        f.write(content)
      return f"File created at{file_path} with content:{content}"
    
    tools=[crete_file,search_tool]
    simple_research_agent = create_tool_calling_agent(llm,tools,prompt_agent)
    simple_research_agent_executor = AgentExecutor(agent=simple_research_agent,tools=tools,verbose=True)
    output_report = simple_research_agent_executor.invoke({'input':'write a summarize report of main highlights of paris olympics- save locally as report-olympics-2024.md'})
    
![image](https://github.com/user-attachments/assets/7b4314cc-2998-48bd-b9b2-1b76fa9c6513)
![image](https://github.com/user-attachments/assets/6eebcbca-0a53-4bdf-907c-165a1d2b9f2c)


- now ready to build a useful agent.
- as you can see the simple_research_agent_executor has template,binding,output_parser.
- now produce the output_report with this .

![image](https://github.com/user-attachments/assets/53558f4d-a365-4120-9418-6d359d17ce51)

- above create a report of olympics.

![image](https://github.com/user-attachments/assets/d642c6a0-efe8-4579-b685-413e474d050f)
![image](https://github.com/user-attachments/assets/ae58eca0-e2d9-4313-9e57-fa331e730348)

![image](https://github.com/user-attachments/assets/646b9388-b824-43f0-b5c7-51222d13ab97)

print the report


![image](https://github.com/user-attachments/assets/de9e7b0a-ec53-4a0d-9aa8-2f2c7a2054fd)

![image](https://github.com/user-attachments/assets/4b0edb70-48a5-4a5d-8b1d-1ae27c13bf4d)
   
Summary:
========

  - create a useful agent in langchain
  - could search and write to report store in local
