# VerilogFromTruthTable
Converts .txt truth table into verilog module 
Written in Python 3

## Quick start
1) To create verilog module from truth table you should input at least two required arguments:

    * --pi - path to source truth table file;
    * --po - path where to save output verilog module;
    
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
    
    ![image](https://user-images.githubusercontent.com/32493975/97776550-bfea7480-1b71-11eb-87a1-5b42a1b08db5.png)
    
 
## Testing
  
To check if this script work correctly you can use testbench or .do file which I created to check modules created in previous example. Or you can create you own truth table for testing using TableGenerator.py script. It could be useful to generate big truth table, which could be coplicated to write with bare hands.
  
### Table Generator tutorial

   * Type into --help to get quick help
   ![image](https://user-images.githubusercontent.com/32493975/97776194-c6c3b800-1b6e-11eb-824a-a360ba6be71b.png)
   
   * --po - path where to save your output truth table;
   * --i  - input amount of input signals you want to have;
   * --o  - input amount of output signals you want to have;
   * --g  - (optional, turned on by default), if you want to create testbench file to compare output values of parsed modules with values from truth table this argument can be useful. It creates table only with values of output signals, so you can easily use $readmemb() function in your testbench file to check if all results are correct. Generated file will be named YourTableName_testbench_table.txt. 1 to turn on, 0 to turn off.
   * --mode - (optional, little endian is by default), choose how to display input signals. True for little endian, False for big endian mode;
   
   Examples:
   
   * Little endian table with testbench_table.txt
   ![image](https://user-images.githubusercontent.com/32493975/97485431-cc4cb280-1962-11eb-9644-b8b84ec5afac.png)
   ![tables](https://user-images.githubusercontent.com/32493975/97776314-b5c77680-1b6f-11eb-94df-b2122a929222.jpg)
   
   
   * Big endian table without testbench_table.txt
   ![image](https://user-images.githubusercontent.com/32493975/97776347-f0311380-1b6f-11eb-8fb0-4176b8dd12a0.png)
   ![image](https://user-images.githubusercontent.com/32493975/97776368-0b038800-1b70-11eb-8d24-5e4843e62998.png)
   
   ### ModelSim Testing
   In this section I will simulate testbench file for previously generated modules DDNF_8_5.v and DKNF_8_5.v. You can add slight modifictions to this file to test different amount of input and output signals. If DDNF and DKNF outputs are different from output values from truth table error flag will be rised. And in console you will get output of simulation. You can find this and a few more examples of testbench files in "Testing" folder.
   
   ![image](https://user-images.githubusercontent.com/32493975/97776681-d47b3c80-1b72-11eb-9fe0-1fc8f7afe3ae.png)
   
   ![image](https://user-images.githubusercontent.com/32493975/97776693-f1177480-1b72-11eb-83ab-4d9e0836a24e.png)


### Hardware utilization
   Maximum that I was able to compile in Quartus was project with 14 input pins. Above that value I was getting StackOverlfow error.
   
   Flow Summary
   
   ![image](https://user-images.githubusercontent.com/32493975/97778563-b4527a00-1b80-11eb-809f-f233f0653dbc.png)
   
   Flow Elapsed Time
   ![image](https://user-images.githubusercontent.com/32493975/97778582-cf24ee80-1b80-11eb-9587-b5b5faa5325d.png)
