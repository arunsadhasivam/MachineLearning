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

  1)Understand dataset:
  ====================

  build a model to suggest Tag


      question_df = pd.read_csv("question.csv", encoding='lation-1')

  SNO | owneruserid  | creationdata | score | title | body
  ----|--------------|--------------|-------|-------|-------------


  code:
  ======

        def cleaner(text):
              text = beautifulsoup(text).get_text()
              text = re.sub('^[a-zk-z]"," ",text)
              text = text.lower()
              tokens = text.split()
              return "".join(token)

       question_df['cleaned-text']= question_df["body"].apply(clener)
       question_df["body"][1]
       question_df["cleaned_text"][1]


  Tag Dataset:
  ============
  
       tags_df['tag'].unique()
       tags_df['tag']= tags_df['tag'].apply(lamda.x:re.sub("."," ",x)

       tags_df = tags_df.groupby('id')
                        .apply(lambda->x:x['tag'].values)
                        .reset_index(name='tags')

  mergeto question with tag df:
  ===============================

       df = pd.merge(question_df,tags_df,how='inner' on ='id')
        


  2)Dataset Preparation:
  =======================


  Get freq of each tag:
  =======================

        freq={}
        for i in df['tags']:
          for j in freq.keys:
             freq[j]= freq[i]+1
          else
             freq[j]=1;
    
      freq  = dict(sorted(freq.items(),key=lambda.x:x[1],reverse=true)

      //since sequence sorting is important.

  Top 10 tags:
  ============

     comment_tags = list(freq.keys())[:10]


we only then assign questions to only questions that map to top 10 tags:
=========================================================================


       x=[]
       y=[]
       for i in range( len(df['tags'])):
          temp=[]
       for j in df['tags'][i]:
          if j in common_tags:
             temp.append(j)
          if len(temp>1):
             x.append(df['cleaned_text'][i]
             x.append(temp)


       
  
