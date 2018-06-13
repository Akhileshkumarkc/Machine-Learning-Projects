
public class PixelObject {
	
	int trans;
	int red;
	int green;
	int blue;
	int int32bit;
	
	public PixelObject(int int32bit){
		this.int32bit = int32bit;
		convertToRgb();
	}
	
	public PixelObject(int[] pixels){
		trans = pixels[0];
		red = pixels[1];
		green = pixels[2];
		blue = pixels[3];
		convertToInt();
		
	}

	private void convertToRgb() {
		trans = int32bit >> 24 & 0xFF;
    	red = 	int32bit >> 16 & 0xFF;
	    green = int32bit >> 8 & 0xFF;
	    blue =  int32bit & 0xFF;
		
	}
	
	private  void convertToInt() {
	    int32bit= ( ((trans & 0xFF) << 24) | ((red & 0xFF) << 16) | ((green & 0xFF) << 8) | (blue & 0xFF) );
	    
	}
	
	public int[] getRGBvalues(){
		int [] pixelArray = new int[4];
		pixelArray[0] = trans;
	    pixelArray[1] = red;
	    pixelArray[2] = green;
	    pixelArray[3] = blue;
	    
	    return pixelArray;
	}
	public int getConCatRGBValues(){
		return int32bit;
	}
	
	
}
