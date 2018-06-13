import pandas as pd
predictedData = pd.read_csv('predictions.txt',sep=',', header = None,names =["movieid","userid","givenrating","predictedrating"])
#print(predictedData.head())
movieData = pd.read_csv('movie_title.txt',sep='\t', header = None,names =["movieid","movieyear","movieName"])
movieData.head()
Totaldata = predictedData.merge(movieData)
Totaldata.head()
Totaldata =Totaldata.ix[Totaldata.predictedrating > 3.5]
Totaldata.head()
usercounts = Totaldata.groupby('userid').size().sort_values()
highestrated = usercounts[-2:]
# usercounts = Totaldata.groupby('userid')
#print(usercounts)
filtered = Totaldata[Totaldata.userid.isin(highestrated.index)]
#print(filtered)
filtered.movieName= filtered.movieName.str[:25]
filteruserid = filtered.sort_values(by =['userid','predictedrating'], ascending=[False,False]).groupby('userid')
print(filteruserid.head(100))

