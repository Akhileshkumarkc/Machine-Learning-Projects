
public class KmeanCalculation {
	
	public int length;
	public int clusterk;
	public int iterations;
	public int maxno;
	
	public int[] items;
	public int[] clusterKmeanList;
	public int[] itemclassList; 
	
	public  KmeanCalculation(){
	
	}
	

	public static void main(String[] args) {
		//Kmeans
		KmeanCalculation kmc = new KmeanCalculation();
		
		kmc.length = 100;
		kmc.clusterk=100;
		kmc.iterations = 100;
		kmc.maxno=255;

		kmc.sampleItems();
		//clusterMeann
		kmc.ClusterMeanInitalize();
		
		// ClusterKMean
		kmc.ClusterKMean();

	}


	private  void sampleItems() {
		items = new int [length];
		for(int i = 0, val = 2; i < items.length; i++){
			items[i] = val + i * 2;
			items[i] = (int) (Math.random()*maxno);
	    }
	}


	public  void ClusterKMean() {
		for(int i = 0;i < iterations; i++){
			
			itemclassList = findArgMin(items,clusterKmeanList,itemclassList,maxno);
			clusterKmeanList = findMeanCluster(items,itemclassList,clusterKmeanList,clusterk);
//			System.out.println("\n*****************************************");
//			System.out.println("\nIteration : " + i + "\n Item Class \n");
//			displayArray(itemclassList);
//			System.out.println("\n Cluster Mean\n");
//			displayArray(clusterKmeanList);
//			System.out.println("\n*****************************************\n");
			
		}
		displayEnd();
	}

	private static int[] findMeanCluster(int []items, int[] itemclassList, int[] clusterKmeanList,int clusterk){
		int[] sumClusterList = new int[clusterk];
		int[] noofItemsClusterList = new int[clusterk];
		
		for(int i = 0;i < clusterk; i++){
			sumClusterList[i] = 0;
			noofItemsClusterList[i] = 0;
			
		}
		
		for(int itemno = 0 ; itemno < itemclassList.length ; itemno++){
			int itemclass = itemclassList[itemno];
			sumClusterList[itemclass] += items[itemno];
			noofItemsClusterList[itemclass]++;
		}
		for(int clusterIndex = 0; clusterIndex < clusterKmeanList.length ; clusterIndex++){
			
			if(noofItemsClusterList[clusterIndex]!=0){
				clusterKmeanList[clusterIndex] = sumClusterList[clusterIndex] / noofItemsClusterList[clusterIndex];
			}
			
		}
		return clusterKmeanList;
	}

	private static int[] findArgMin(int []items, int [] clusterKmean, int[] itemclass,int maxno) {
		
		for(int i = 0 ;i < items.length ; i++){
			int argmin = maxno*maxno, diff, diffsq, argMinClass = 0;
			
			for(int j = 0;j < clusterKmean.length;j++){
				diff = items[i] - clusterKmean[j];
				diffsq = diff * diff;
				if(argmin > diffsq){
					argmin = diffsq;
					argMinClass = j;
				}
			}//Cluster
			itemclass[i] = argMinClass;
		}//items.
//		System.out.println(" \n Cluster K Mean \n ");
//		displayArray(clusterKmean);
		
//		System.out.println(" \n item Class \n ");
//		displayArray(itemclass);
		
		return itemclass;
		
	}
	
	public  void ClusterMeanInitalize() {
		clusterKmeanList = new int [clusterk];
		itemclassList = new int [length];
		for(int i = 0,val = 10; i < clusterKmeanList.length; i++){
			clusterKmeanList[i] = val + i * 10;
		}
	}
	
	private  void displayEnd(){
		//System.out.println("\nitems\n");	
		displayArray(items);
		//DebugFile.write("\nCluster K-Mean List\n");
		displayArray(clusterKmeanList);
		//DebugFile.write("\nitem class List\n");
		displayArray(itemclassList);
	}
	private static void displayArray(int array[]){
		
		for(int i = 0; i < array.length; i++){
			DebugFile.write(array[i]+"  ");	
		}
	}

}
