import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

public class DebugFile {
	
	public static FileWriter fw;
	public static BufferedWriter bw;

	
	public static void init(){
		try {
			fw = new FileWriter("debug.txt");
			bw = new BufferedWriter(fw);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	
	}
	public static void write(String s){
		try {
			bw.write(s);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
	public static void done(){
		try {
			bw.close();
			fw.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
}
