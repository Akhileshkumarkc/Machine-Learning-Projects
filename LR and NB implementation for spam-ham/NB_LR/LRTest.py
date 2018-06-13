import pickle
import LogisiticRegression as LR
import time
start_time = time.time()
ms = pickle.load(open("trainingms300.dat","rb"))
print("classification starts")
LR.LRclassify(ms,LR.TestFilepath,False)
