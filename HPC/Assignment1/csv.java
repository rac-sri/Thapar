import opencsv.CSVWriter;
import java.util.*;
import java.io.*;

class csv {
    public static void  writeFileLineByLine(String filePath, int add,int subtract,int divide, int multiply){
        File file = new File(filePath);
        try{
            FileWriter output = new FileWriter(file);
            CSVWriter writer = new CSVWriter(output);
            
            String[] header = {"Add" , "Subtract", "Divide" , "Multiply"};
            writer.writeNext(header);

            String[] data = {String.valueOf(add),String.valueOf(subtract),String.valueOf(divide),String.valueOf(multiply)};
            writer.writeNext(data);
        }
        catch(Exception e){
            e.printStackTrace();
        }
    }

    public static void generateRandomNumber(){
        try{
            int max = 100;
            int min = 0;
            Random random = new Random();
            int number = (int)Math.random() * (max - min + 1) + min;
            int number2 = (int)Math.random() * (max - min + 1) + min;

            int add = number + number2;
            int subtract = number - number2;
            int divide = number / number2;
            int multiply = number * number2;

            writeFileLineByLine("./",add,subtract,divide,multiply);
        }
        catch(Exception e){   }
    }
    public static void main(String[] args){
        generateRandomNumber();
    }
}