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
