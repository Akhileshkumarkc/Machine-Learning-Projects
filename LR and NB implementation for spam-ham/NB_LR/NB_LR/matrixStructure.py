class matrixStructure:

    def __init__(self):
        self.length = 0
        self.matrix  = [[0 for x in range(12000)] for y in range(1000)]
        self.targetFunc =[]
        self.listofWords=[]
        self.filecount=0
        self.weightVector=[]
        self.sigSum = []

    def initWeightVec(self,len):
        self.weightVector =[0.0 for i in range(len) ]
        self.initSigSum()

    def initSigSum(self):
        self.sigSum =[0 for i in range(1000)]