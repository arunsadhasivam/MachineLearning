Stack Exchange - Auto Tagging system:
====================================

- stack exchange
- how tag a question based on questions like question releated to regression are
  tagged to regression tag, similary classification related topics are tag to classification tag
- exper answer to question.
- automatic question tag based on question.

E.g:
====

" The rising environmental pollution screams out for a need for reduce fossil fuel"

Two Tags are possible.

1) environmental pollution.
2) Fossil fuel.


- input : Text from question
- Target variable : Multiple Tags
- Diff rom binary and multiclass classification (when target class has > 1 label i.e atleast 2 labels)


  SNO   |  X(input)      |     Y (Target outcome)
  ------|----------------|------------------------
   1    | X1             |  [t2,t5]  tag :python
   2    | X2             |  [t1,t3,t2] tag: regression
   3    | X3             | [t4] tag: numpy

  Understand dataset:
  ====================

  build a model to suggest Tag


      question_df = pd.read_csv("question.csv", encoding='lation-1')

  SNO | owneruserid  | creationdata | score | title | body
  ----|--------------|--------------|-------|-------|-------------


  
