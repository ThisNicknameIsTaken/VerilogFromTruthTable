# VerilogFromTruthTable
Converts .txt truth table into verilog module 

## Quick start
1) To create verilog module from truth table you should input at least two required arguments:

    * --pi - path to source truth table file;
    * --pi - path to save output verilog module;
    
    ![image](https://user-images.githubusercontent.com/32493975/97477721-a6221500-1958-11eb-804d-1a8676cab986.png)
    
    Using only this two arguments will create verilog module based on sum of products method.
    
 2) If you want to create verilog module based on products of sum method simply add --mode POS argument. This argument is optional, if leave this argument empty mode will me sum of products by default.
    * --mode POS - creates verilog module based on products of sum method (KNF);
    * --mode SOP - creates verilog module based on sum of products method (DNF);
    
    ![image](https://user-images.githubusercontent.com/32493975/97478543-c4d4db80-1959-11eb-8041-bcb39ba3f10e.png)
  
 3) Type into --help to get quick help for usage of arguments.
    * --help - quick help;
    
    ![image](https://user-images.githubusercontent.com/32493975/97479061-7a079380-195a-11eb-99d2-77c8013a2b9d.png)
  
 4) Examples:
    * Creating POS verilog module:
    
    ![image](https://user-images.githubusercontent.com/32493975/97479791-4d07b080-195b-11eb-9877-60f331fb9c54.png)
    
    * Creating SOP verilog module:
    
    ![image](https://user-images.githubusercontent.com/32493975/97480041-92c47900-195b-11eb-8cf1-52e42fe227f4.png)
    
    This will generate two files in specified path.
    
    ![image](https://user-images.githubusercontent.com/32493975/97480335-ee8f0200-195b-11eb-9841-af2e9297c2ae.png)
    
 
## Testing
  
To check if this script work correctly you can use testbench or .do file which I created to check modules created in previous example. Or you can create you own truth table for testing using TableGenerator.py script. It could be useful to generate big truth table, which could be coplicated to write with bare hands.
  
### Table Generator tutorial

   * Type into --help to get quick help
   ![image](https://user-images.githubusercontent.com/32493975/97485995-847a5b00-1963-11eb-8232-66f89c94b896.png)
   
   * --po - path where to save your output truth table;
   * --i  - input amount of input signals you want to have;
   * --o  - input amount of output signals you want to have;
   * --mode - (optional, little endian is by default), choose how to display input signals. True for little endian, False for big endian mode;
   
   Examples:
   
   * Little endian
   ![image](https://user-images.githubusercontent.com/32493975/97485431-cc4cb280-1962-11eb-9644-b8b84ec5afac.png)
   ![image](https://user-images.githubusercontent.com/32493975/97484947-18e3be00-1962-11eb-97c3-72e74794d4ef.png)
   
   * Big endian
   ![image](https://user-images.githubusercontent.com/32493975/97485555-f605d980-1962-11eb-97f7-21f430d43e34.png)
   ![image](https://user-images.githubusercontent.com/32493975/97482355-bb9a3d80-195e-11eb-86a9-e75dd8724897.png)
   
   ### ModelSim Testing
   In this section I will simulate testbench file for previously generated modules DDNF_8_5.v and DKNF_8_5.v. You can add slight modifictions to this file to test different amount of input and output signals. If DDNF and DKNF outputs are different the error flag will be 1.
   
   ![image](https://user-images.githubusercontent.com/32493975/97494426-f7d59a00-196e-11eb-927b-f70436f067ce.png)
   
   ![image](https://user-images.githubusercontent.com/32493975/97494490-0cb22d80-196f-11eb-97cb-ed7493612e32.png)
