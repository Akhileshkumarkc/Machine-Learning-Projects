/*** Author :Akhilesh Kumar
The University of Texas at Dallas
Modified Vibhav Gogate code
*****/


import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;
 

public class KMeans {
	
	public static int Transparent_index = 0;
	public static int Red_Value_index = 1;
	public static int Green_value_index = 2;
	public static int Blue_value_index = 3;
	
	// k <-  0 = value, 1 = clusterno 
	public static int original_value_index = 0;
	public static int clusterno_index = 1;
	//Trans, Red, Green, Blue.
	public static int ColorSize = 4;
	
    public static void main(String [] args){
	if (args.length < 3){
	    System.out.println("Usage: Kmeans <input-image> <k> <output-image>");
	    return;
	}
	try{
	    BufferedImage originalImage = ImageIO.read(new File(args[0]));
	    int k=Integer.parseInt(args[1]);
	    BufferedImage kmeansJpg = kmeans_helper(originalImage,k);
	    ImageIO.write(kmeansJpg, "jpg", new File(args[2])); 
	    System.out.println("Clustered File has been written to "+ args[2]);
	}catch(IOException e){
	    System.out.println(e.getMessage());
	}	
    }
    
    private static BufferedImage kmeans_helper(BufferedImage originalImage, int k){
	int w=originalImage.getWidth();
	int h=originalImage.getHeight();
	BufferedImage kmeansImage = new BufferedImage(w,h,originalImage.getType());
	Graphics2D g = kmeansImage.createGraphics();
	g.drawImage(originalImage, 0, 0, w,h , null);
	// Read rgb values from the image
	int[] rgb=new int[w*h];
	int[] rgbm=new int[w*h];

	int count=0;
	for(int i=0;i<w;i++){
	    for(int j=0;j<h;j++){
		rgb[count++]=kmeansImage.getRGB(i,j);
	    }
	}
	// Call kmeans algorithm: update the rgb values
	
	rgbm = kmeans(rgb,k);
	
	//Call error.
	float val,diffsq=0;
	for(int i = 0; i < w * h;i++){
		val = rgbm[i] - rgb[i];
		diffsq += ( val * val );
	}
	float error = diffsq / (float)( w * h);
	//System.out.println(error);
	
	// Write the new rgb values to the image
	count=0;
	for(int i=0;i<w;i++){
	    for(int j=0;j<h;j++){
		kmeansImage.setRGB(i,j,rgbm[count++]);
	    }
	}
	return kmeansImage;
    }

    // Your k-means code goes here
    // Update the array rgb by assigning each entry in the rgb array to its cluster center
    private static int[] kmeans(int[] rgb, int k){
    	int Totallength = rgb.length;
    	//Initialize Debug File.
    	initializeDebug();
    	
    	// pixel <- pixel
    	// color <- trans, red, green, val
    	// k <-  0 = value, 1 = clusterno
    	// Data Structure to choose the pixel values.
    	int [][][] values = new int[Totallength][ColorSize][2];
    	
    	// color <- T, R, G, B 
    	// clusterno <- 0.. K-1 clusters  
    	int [][]    clusterMeanInfo = new int[ColorSize][k];
    	
    	
    	for(int pixel=0; pixel< Totallength;pixel++ ){
    		
    		PixelObject pixelObj = new PixelObject(rgb[pixel]);
    		int trgb = pixelObj.getConCatRGBValues();
    		//if(rgb[i] == trgb) System.out.println("yes");
    		int [] pixelArray = pixelObj.getRGBvalues();
    		//System.out.println(pixelArray[0]+" "+pixelArray[1]+" "+pixelArray[2]+" "+pixelArray[3]);
    		values[pixel][Transparent_index][original_value_index] = pixelArray[Transparent_index];
    		values[pixel][Red_Value_index][original_value_index] = pixelArray[Red_Value_index];
    		values[pixel][Green_value_index][original_value_index] = pixelArray[Green_value_index];
    		values[pixel][Blue_value_index][original_value_index] = pixelArray[Blue_value_index];
    		    	
    	}
    	
    
    	 for(int color = 1; color < ColorSize;color++) {
    	
    	  int[] itemvalue = new int[Totallength];
	    	 for(int pixel = 0; pixel < Totallength; pixel++){
	    		 itemvalue[pixel] = values [pixel] [color][original_value_index];
	    	 }
	    	 
	    	 KmeanCalculation kmc= new KmeanCalculation();
	    	 kmc.length = Totallength;
	    	 kmc.clusterk = k;
	    	 kmc.iterations = 100;
	    	 kmc.maxno = 255;
	    	 kmc.items = itemvalue;
	    	 kmc.ClusterMeanInitalize();
	    	 kmc.ClusterKMean();
	    	 
	    	 //meanlist
	    	 int [] itemMeanList = kmc.clusterKmeanList;
	    	 clusterMeanInfo[color] = itemMeanList;
	    	 
	    	 //itemlist
	    	 int [] itemclassList = kmc.itemclassList;
	    	 for(int pixel = 0; pixel < rgb.length; pixel++){
	    		 values[pixel][color][clusterno_index] = itemclassList[pixel];
	    	 }
	    	 
	    }
    	 
    	//put back the values into RGB 
    	int rgbmodified[] = new int[Totallength];
    	
    	for(int pixel=0; pixel<Totallength; pixel++){
    		int[] pixelArray = new int[ColorSize];
    		pixelArray[Transparent_index] = values[pixel][Transparent_index][original_value_index];
    		
    		for(int color = 1;color < ColorSize;color++){
    			int cluster_index = values[pixel][color][clusterno_index];
    			pixelArray[color] = clusterMeanInfo[color][cluster_index];
    		}
    			
    		PixelObject pixelObj = new PixelObject(pixelArray);
    		rgbmodified[pixel] = pixelObj.getConCatRGBValues();
    	}
    	return rgbmodified;
    	
    	
    }

	

	private static void initializeDebug() {
		DebugFile.init();
    	DebugFile.write("sample");
	}
	

}