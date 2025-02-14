Introduction to Langfuse:
==========================
![image](https://github.com/user-attachments/assets/4fe85653-c634-4d41-8e52-47aa25b3803e)

    - it is full fledged llm engineering platform , which is also opensource present in github.
    - currently it has 2.4k stars and it is popular
    - available as paid cloud solution or self hosted.
    - as it is opensource, it can be hosted in our server internally.
    - it has integrations with other third party apis llama index.
    - it makes langfuse really easy.
    - REST Api's are also available.

Why LangFuse:
==============

![image](https://github.com/user-attachments/assets/721f7afe-1814-4b34-a92b-fbf25dc43a76)

    - we go through the same app,
    - we have a query which goes through the langchain promptTemplate 
    - we have a retriever which fetches the document from the vector store.
    - we have also have document loaders , which scrap the website using all of this along with the query
      we generate the final prompt.
    - send it to the llm component of langchain
    - this has the llm config and using all this , llm model is called.
    - the llm model now , gives the output , which is first introduced by the output_parser and then handles the
      output in the given format. and then this generates the final output.


    - for a single llm application in production, we need to debug issues in production , as we go through
      the all the steps, if we go through the issue or an error , we dont know where it actually happen.
      1) did it happen in prompt template stage
      2) was the query wrong.
      3) may be retriever did not retrieve the document properly
      4) or the web site scrapping not working properly
      5) or the output_parser actually failed, we dont know.

   - unless we iterate on multiple solution,
   - one solution
       1) is what if we change the llm and if stops works
       2) and we analyze the exact portion which stops working.
       3) and we monitor the performance in production, in which once it is deployed we also want to know
          how time full end to end for the user.
       4) how much time did the model took.
       5) how much time web scrapping tool took.
       6) what was the end to end latency.
       7) what was the cost of the llm model , these are things that we want to monitor in production.
       8) also want to continuously run test and create releases.


![image](https://github.com/user-attachments/assets/a701b3c2-79fa-4f59-934e-46393176236f)

  - let say we have dataset of input, and output. we want to know then what is output of new model, based on it
    we will run it on test set.
  - the test set also generates another output , and then we can compare the new llm output from the previous output.
  - and then know when if we want to release it  a new release.
  - so , these kind of testing can also be implemented using langfuse.
  - now , this is something discussed about one single project.
  - this is something, that we discussed about one single project. multiple teams needs to research
    and collborate on multiple project . so all this issue would be there in multiple project
  - multiple llm application needs to be released and maintained at the same time.
  - so we are not just **to monitor one applications in an organization, but multiple applications** for their
    metric at the same time.
  - thats where langfuse comes in to picture.

LangFuse ecosystem:
====================
![image](https://github.com/user-attachments/assets/7e79b82a-82b8-4903-a31f-2fc3a22fb443)


  - currently the ecosystem in divided in to 3 parts.

    1) developed
    2) Monitor
    3) Testing

1.development:
=================

  - track llm calls and other application logic
  - we can track what all happens at each and every step in our llm chain.
  - support api , sdk and third party libraries
  - we can integrate it using direct api to the cloud solutions or internally deployed langfuse solutions.
  - we can also use their pyton and typescript sdk, as we discuss third party libraries like llama index
    and langchain integration is very easy to do.
  - we have an langfuse ui , where we can inspect and debug calls.
  - so , **once an llm chain branch , we can directly go to our ui** and see how it performs.
  - we also have prompt engineering playground , where we can try different prompt and see the output, without any code.
  - we also have prompt management , rather than **hard coding our prompts in our code base** , we can also manage and
    version these prompts really well.

2.Monitor:
================  

  - it deals with metrics and dashboard.
  - so, langfuse has an analytics dashboard, in which we can see the cost , latency and  quality of the model
  - we can also run evaluations, these days we use llm to get to know the llm output
  - so this is the llm evaluating another llm.
  - we also run these evaluations, of some of the output that are application generated using llm also known as evaluations.
  - we can also integrate user feedback with score and comment.
  - this is something the end user can see in ui and feedback and score given can be integrating directly to which
    particular api call was made.
  - there is a deep integration with   final user feedback and scores.

3.testing:
==========
  - langfuse offers something called as datasets.
  - in which we can create samples of input and output
  - and once the dataset is prepared , we can run test on it and then benchmark or baseline performance.
  - we can then use this test as basic benchmark to which future changes can be checked  as to if
    that increases or decreases the score. based on this , we can see if you want to deploy this application
    in production or not.
  - in this way we track versions and different releases and langfuse also supports knowing which version
    of the application or releases  which it is showing output.
   - High level langfuse demo
