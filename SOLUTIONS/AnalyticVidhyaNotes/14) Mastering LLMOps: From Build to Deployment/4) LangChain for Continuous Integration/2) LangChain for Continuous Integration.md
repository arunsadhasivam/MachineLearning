LangChain for Continuous Integration:
======================================

    - langchain has lot of components, which is divided in to multiple sections, we have
       1) main lang chain  - which is chains, agents, retrieval strategies - core of the langchain ecosystem.
       2) 


1.main lang chain:
===================

    - it has chains, agents, retrieval strategies.
    - core of the langchain ecosystems.
    - it has also have open source library support langchain as a library is opensourced which has 2 major components
          1) core:langchain core - LCEL and base abstractions. 
          2) also we have lot of community support for e.g @langchain/openai -> code to make it easy to work it openai,
           same way for anthropic, and other providers as well.

2.LangGraph:
=============
    - langGraph - which helps us to buiild agent very quickly using graph database
    - we also have langSmith , which is a developer platform that lets you to debug, test, evaluate and monitor llm applications.
    - once you have llm applications ready , you also measure a lot of different parameters, test and evaluate things as they 
      go along , even during testing or even during deployment and thats what langsmith takes care of and has very high
      integration with langchain.


3.langGraph Cloud:
==================

    - which is the deployment part of langGraph in which you can take our langGraph application and deploy it on 
      langGraph Cloud.

4.LangServe:
============

  - chain as rest APIs
  - it makes it really easy to take these langchain chains and represent as **webserver base REST api's**
  - so from a project to actual web server, can be made really easy using langServer.
  - we have 2 main aspects of this langchain ecosystem.
    1) one is open source software
    2) then we have commerical part of these things.
  - so in the diagram we can see that commerical is mentioned with this box and **OSS is something open source**
  - And so we have langchain is the architecture and this is the underlying library
  - in the same way , the langGraph is also open sourced 
  - ALL the integrations, that we can do with the langChain and LangGraph is also opensourced.
  - then to deploy our langGraph applications to the cloud,
