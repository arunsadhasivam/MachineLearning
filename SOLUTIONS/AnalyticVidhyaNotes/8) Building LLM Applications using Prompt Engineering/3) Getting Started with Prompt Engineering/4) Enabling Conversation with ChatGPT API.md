Enabling Conversation with ChatGPT API:
========================================

  - first prompt to write a article in datascience
  - output get from the chatput like seo
  - 2nd prompt include 10 faq
  - it gives 10 unrelated response it forgets the 1st prompt.
  - first prompt where i asked chatgpt to write the article "decision trees"
  - i got the output
  - second prompt which have given was to include 10 faq for above blog.
  - what it id is it gives 10 faq of very unrelated context. not in decision trees
  - in order to do this enable conversation.
  - for this we create a list of messages

![image](https://github.com/user-attachments/assets/6f8f6de9-5d4c-435e-a422-2bab3c838f71)

![image](https://github.com/user-attachments/assets/f00f170d-5016-4cb7-a784-472bf377113e)

- here the first role was **user** which is prompt given by user.
- second one was the output which was created - hence role of **assistant**
- again second prompt with the role of **user**
- all history gets passed on in form of messages.
- let run to see output
![image](https://github.com/user-attachments/assets/c9482fbb-b943-48ba-874e-5a99b3dbeae0)

- above you can see the context is carried  by using the list we cread message[] array


Define chat function:
========================

  - let say working on an applications, where there are 100s of these prompt getting generated
    you cannot keep adding in this manual way.
  - actually a automated way, in that all these prompts and their output are adding in the history.
  - what we do is we create a emtpy list history[] and then all the user input prompt are added with the
    role **user** in to history.
  - we append every time when there is new input message we append to history and then pass it on to chat gpt.
  - finally whatever **output** comes we add to history but this time with the role of **assistant**
  - short input -> user role
          output -> assistant role to make converstation carries the context.

![image](https://github.com/user-attachments/assets/cb84549a-23b3-4d91-8910-7b9eb4cddfcd)
![image](https://github.com/user-attachments/assets/09a58b5c-e7ce-407b-a446-5fa900d0faae)
Another prompt to check whether the context is carried forward
![image](https://github.com/user-attachments/assets/d03cf401-6242-4118-8e38-5a13a569aa38)


print the history:
===================

![image](https://github.com/user-attachments/assets/799a29d7-8e90-4cdb-8275-bb4c6266c03e)


- like you can see the all the user, system ,assistant messages passed in history
- assistant is the output.

![image](https://github.com/user-attachments/assets/f2497806-7dbc-45d6-91e1-8ace9496eea0)

- start a new task with new message , as you can see does not carry over the context
![image](https://github.com/user-attachments/assets/71a06f44-f597-47fa-91d8-0a2d0f728be5)

- as you can history has   1 input and 1 output.
