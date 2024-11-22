MultiLabel Binary:
===================


   from sklearn.preprocess import MultilabelBinarizer
   mlb = MultiLabelBinariser()
   y = mlb.fit_transform(y)
   y.shape()

   mlb.classes
   ==========

       array[['classification','distirbution'...]



  Train:
  =====
  
      from sklearn.model.selectoin import train_test_split
      x_tr,x_val,y_tr,y_val=train_test_split(x,y,test-size=0.2,random-state=0,shuffle=True)

  Tokenizer:
  ==========

    from keras.preprocessing.text import Tokenizer
    from keras.preprocessing.sequence import pd_sequences
        x_tokenizer = Tokenizer()
        x_tokenizer.fit.on-texts(x_tr)
        x_tokenizer.fit.on-tests(x_tr)

x_tokenizer.words.index
==========================

  ('the': 1 
   '1' : 2
   'to' : 3
   'this' : 14)

 less frequency occuring tokens:
 ===============================

       thresh = 3;  //occurs 3 times in token.
       cnt =0;
       for key,value in x_tokenizer.word_counts.items():
           if value >= thresh:
              cnt = cnt+1;
      print(cnt);
    
    
      //over 12,000 tokens appear 3 times or more in training.
    
      x_tomenizer = tokenizer(num_words=cnt,oob_token='wnk')
      x_tokenizer.fit.on-test(x-tr)

  train & validations are in text:
  ================================

 - Now  we can feed to deep learning models directly so convert to integer.
 - To make all input sequences of same length, since **model only accept same length sequence** only.
   using technique called  **padding**  by set max_len=100


      max_len = 100
      x_tr_seq = x_tokenizer.text_to_sequences(x_tr)
      x_val_seq = x_tokenizer.text_to_sequences(x_val)
      x_tr_seq = pad_sequences(x_tr_seq, padding='port', maxlen=max_len)
      x_val_seq= pad_sequences(x_val_seq, padding='port', maxlen=max_len)

      //no. of unique words
      x_vec_size = x_tokenizer.num_words+1

   E.g:
   ===

        max_len=7
        s1=[43,96,2,78,43]
        s1p=[43,96,2,78,43,0,0]
        s3=[11,51,9,52,6,1,75,29]
        s29=[11,51,9,52,6,1,75]


   Model Building ( Multi Label Prediction)
   =========================================

         model = sequential
         model.add(embeddings(x_voc_size=50, input_shape=max_len),mask_zero=True)
      
         #rnn layer
         model.ad(simpleRNN(128,activation='relu')
         #dense layer
         model.add(Dense(120,activaation='relu')
      
         #output layer
         model.add(Dense(10,activation='sigmoid')
         model.summary()

   output:
   ========

   Total params : 669,644
      
         model.compiile(optimizer='adam',loss='binary_cross_entrophy')
         mc=ModelCheckPoint('weights.best.hd5', monitor='val-loss',verbose='',save_best_only=True,
                                            mode='min')

Train Model
============

        model.fit(x_tr_seq, y-tr, batch_size=128,epoch=10,verbose=1,vaildation_date(x_val_seq,y_val),callback=[mc])


o/p:
====
    model. stop learn epoch 0.5(6)


model prediction on best model:
==============================

  model.load-weights('weights.best.hd5') // load best model which we saved earlier
  pred_prob = model.predict(x_val_seq)

output:
=======

      pred_prob[0]

Threshold:
==========

   threshold = np.arrange(0,0.5,0.01)

predict tag based on probability:
==================================

 1) set threshold value 0.5
 2) if Tag with probability score >= threshold:
          value convert to 1
      else
         convert to 0
 3) how to set threshold or set or guess best threshold.

 how to determing correct threshold value:
 =========================================

   1) Now tag correspond to there 1 are final predicted tag for question for input
   2) how to determine correct threshold
   3) Def set of candidates values[0.0 to 0.49] we will check value and find best threshold value


 Steps to find optimal threshold value:
 ======================================

       from sklearn import metrics
       score=[]
       #convert to 1d array
       y_true = np.array(y_val).ravel()
       for thresh in threshold:
           y_pred_seq = classify(pred_prob, thresh)
           y_pred = np.array(y_pred_seq).ravel()
           score.append(metrics.f1_score(y_true,y_pred))
      #optimal threshold
          opt = threshold[score.index(max(score))]

  output:
  ======
      0.29 is optimal threshold

1)Model Evaluation:
===================

    y_pred_seq = classify(pred_prob.opt)
    y_pred = np.array(y_pred_seq).ravel()

  output:
  =======

    metrics.classification_report(y_true,y_pred)


  precision | recall | f1_score| support
  ----------|--------|---------|-------------
    0       |  0.90  | 0.85    | 17520
    1       |  0.49  | 0.67    |   470


      y_pred = mlb.inverse_transform(np.array(y_pred_seq))
      y_true = mlb.inverse_transform(np.array(y_val))
      df = pd.DataFrame(f'comment':x_val,'actual':y_true, 'predictions':y_pred)

  output:
  ======

     df.sample[0]

code:
=====


 def  predict_Tag(comments):
    //preprocess
    text = [cleaner(comments)]
    seq = x.tokenizer.texts_to_sequences(text)
    pad_seq= pad_sequences(seq,padding='post',maxlen=max_len)
    pred_prob = model.predict(pad_seq)
    classes = classify(pred_prob, opt)[0]
    class = np.array()

  output:
  =======

      print (predict_tag(comments))

 
      


  
    


  
   
   
