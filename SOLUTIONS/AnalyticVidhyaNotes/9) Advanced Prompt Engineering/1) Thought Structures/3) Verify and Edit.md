Verify and Edit:
================

![image](https://github.com/user-attachments/assets/c206dd91-19b9-4e16-b41f-fb0ba66536f8)


  - enhances the output by validating with wikipedia or google.

how does it work:
==================


![image](https://github.com/user-attachments/assets/7f0f90e0-5417-4876-a963-0efb72d75867)


  - after we ask questions , the language model assists us its response for 
    certainty before seeking external information using self-consistency prompting.
  - if the initial certainty is lacking, then the language  queries for more information
    from an external resources like wikipedia or google and then it utilizes the new data
    to correct and improve its initial answer.

Verify and edit example:
=========================

![image](https://github.com/user-attachments/assets/d5576dfa-ea1e-48e4-baf4-696334903ce0)

  - so here is the example of verify and edit prompting.
  - we also compare this prompting technique with standard input & ouput prompting
  - also compare the output with the chain of thought prompting.
  - for e.g question **"all of team john playing which team is nyskohus played"**
    1) it generates the answer new castle it is not correct
    2) it also uses chain of thought prompting think in a linear way , it gives the rational and
       based on the rational and generate the answer as old grenland which is also incorrect.
    3) we use the self consistency , where we use the sampling techniques to ask same questions  multiple different ways
    4) then we use external knowledge , we use wikipedia and then we extract information from wikipedia and based
       on the additional knowledge . we edit the ration .
    5) after edit the **rational , we get the answer as "Adelaide footbal club"**

Advantages:
===================

![image](https://github.com/user-attachments/assets/5c4c2428-d5f9-4c91-9e49-1f7efeb7a762)

- this technique increases the language model accuracy by fact checking.
- it calrifies the language model thought process for greater transparency.
- uses real world data, enhancing trust and applicability.
- also outperforms other model methods in complex problem solving.

Cons:
=====
![image](https://github.com/user-attachments/assets/530c81ae-f8ce-4c6f-8bc3-5afa4a8fe757)

- most effective for complex questions and less impactfull for commense queries.
- this techniques also relies on the reliable verification system to improve answer quality.
- also risks introducing error or irrevalent data during **edit** process

