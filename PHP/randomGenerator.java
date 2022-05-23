import java.io.BufferedReader;
import java.io.Console;
import java.io.FileReader;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;
import java.util.concurrent.CountDownLatch;
public class randomGenerator {
    public static void main(String args[]){
        randomGenerator g = new randomGenerator();
        g.start();        
    }
    List<String[]> randomList = new ArrayList<>();
    List<String[]> dataList = new ArrayList<>();

    public void start() {
        getData();
        while(randomList.size() < 500) {
            if(randomList.size() < 300)
            {
                String[] x = dataList.get(getRandomNumber(12289, dataList.size() + 1));
                if(randomList.contains(x) == false)
                {
                    randomList.add(x);
                }
            }
            else if(randomList.size() < 450) {
                String[] x = dataList.get(getRandomNumber(1160, dataList.size() + 1));
                if(randomList.contains(x) == false)
                {
                    randomList.add(x);
                }
            }
            else {
                String[] x = dataList.get(getRandomNumber(0, dataList.size() + 1));
                if(randomList.contains(x) == false)
                {
                    randomList.add(x);
                }
            }
        }
        for (String[] strings : randomList) {
            System.out.println(strings[0]+","+strings[1]+","+strings[2]+","+strings[3]);
        }
    }

    public void getData() {
        String file = "sorted.csv";
        try(BufferedReader br = new BufferedReader(new FileReader(file))) {
            String line = "";
            while ((line = br.readLine()) != null) {
                // System.out.println(line);
                String[] x = line.split(",");
                // System.out.println(x[0]);
                dataList.add(x);
            }
        } catch (Exception e) {
          //Some error logging
          System.out.println("Error" + e);
        }
        return;
    }

    public int getRandomNumber(int min, int max) {
        return (int) ((Math.random() * (max - min)) + min);
      }
}