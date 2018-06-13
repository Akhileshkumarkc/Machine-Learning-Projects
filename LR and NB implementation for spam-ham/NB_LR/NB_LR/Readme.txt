Running the NaiveBayes file
========================================================================
format:
python NaiveBayes.py "traingset" "testset"
ex:
python "NaiveBayes.py" "./hw2_train/train/" "./hw2_test/test/"

===========================================================================
Output:
Training path./hw2_train/train/
Testing path./hw2_test/test/

The Naive Bayes Classifier with Stopwords
(hamCount:spamcount=totalcount),filelistlen = (340:8=348),348
 Accuracy of the ham  97.70114942528735
(hamCount:spamcount=totalcount),filelistlen = (20:110=130),130
 Accuracy of the spam  84.61538461538461
No Stopwords removed from ham 117
No Stopwords removed from spam 113

 The Naive Bayes Classifier without Stopwords
(hamCount:spamcount=totalcount),filelistlen = (338:10=348),348
 Accuracy of the ham  97.1264367816092
(hamCount:spamcount=totalcount),filelistlen = (19:111=130),130
 Accuracy of the spam  85.38461538461539

============================================================================

Runnning the Logistic Regression:

==============================================================
python LogisiticRegression.py "./hw2_train/train/" "./hw2_test/test/"
=====================================================================
Takes Around 80 minutes to run!!!(4851.835983037949 seconds )
Output:
Training path./hw2_train/train/
Testing path./hw2_test/test/

The Logistic Regression Classifier including Stop words
init Matrix is built
---Time Taken: 5.652035474777222 seconds ---
---Time Taken: 5.653039932250977 seconds ---
classification starts
Accuracy of ham file:0.9482758620689655
Accuracy of spam file:0.8076923076923077
---Time Taken: 2711.1571829319 seconds ---
The Logistic Regression Classifier removing Stop words
init Matrix is built
---Time Taken: 2719.0055632591248 seconds ---
---Time Taken: 2719.0065672397614 seconds ---
classification starts
Accuracy of ham file: 0.9454022988505747
Accuracy of spam file: 0. 82307692307692
---Time Taken: 4851.835983037949 seconds --- 

