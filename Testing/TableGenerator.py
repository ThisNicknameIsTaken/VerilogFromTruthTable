#*********************************************************************************
#* Copyright (C) 2020 Vitalii Romakh vitalik55575@gmail.com
#* 
#* This file is part of VerilogFromTruthTable.
#* 
#* VerilogFromTruthTable can not be copied and/or distributed without the express
#* permission of Vitalii Romakh
#*********************************************************************************

import argparse # To proccess input arguments
import os       # To check if path of file is real
import math
import random



#---------------------------------------------------------------------------------------INPUT ARGUMENTS
parser = argparse.ArgumentParser(description="Verilog truth table code generator")

parser.add_argument("--mode",required=False,default="LittleEndian", help = "(Optional, LittleEndian by default) Output mode.")
parser.add_argument("--po",required=True,help="Path to generated table")
parser.add_argument("--i",required=True,help="Amount of input signals",type=int)
parser.add_argument("--o",required=True,help="Amount of output signals",type=int)
parser.add_argument("--g",required=False,default=1,help="(Optional, by default is generating) Generate output table for $readmemb. input 1 to generate this table, 0 - stop generation",type=int)

console_arguments = parser.parse_args()

BigEndian = False
mode = console_arguments.mode
if(mode == "BigEndian"):
    BigEndian = True

if(mode != "LittleEndian" and mode != "BigEndian"):
    raise Exception("Wrong input of --mode argument")
    
full_output_path = console_arguments.po

input_amount = console_arguments.i
if(input_amount <= 0):
    raise Exception("--i; Your input should be greater than 0!\n")

output_amount = console_arguments.o
if(output_amount <= 0):
    raise Exception("-- o; Your input should be greater than 0!\n")

allow_generation = console_arguments.g
if(allow_generation != 1 and allow_generation != 0):
    raise Exception("--g; Wrong argument input! Only 1 and 0 are allowed")

#Checking output file parameters
splited_out_path = full_output_path.split("\\")
#Check if output path exists
output_path = ""    #output path without module_name.v
output_path_counter = 0
for element in splited_out_path:
    if(output_path_counter < len(splited_out_path) - 1):
        output_path += splited_out_path[output_path_counter] + "\\"
        output_path_counter += 1

isOutputFolderExist = os.path.isdir(output_path)
if not isOutputFolderExist:
    raise Exception("No such folder for output file!")

module_file_name = splited_out_path[len(splited_out_path) - 1]
module_file_name_splited = module_file_name.split(".")


if(len(module_file_name_splited) < 2):
    raise Exception("Illegal output path. No file")

module_name = module_file_name_splited[0]
module_format = module_file_name_splited[1]

if(module_format != "txt"):
    raise Exception("Illegal output file extension. It should be text file (.txt)")





random.seed()

full_combination_amount = math.pow(2,input_amount)                         #Amount of lines in file to get all combinations


testbench_readmemb = ""

with open(full_output_path,'w') as file:
    first_line_counter = 1
    out_first_line_count = 0

    while first_line_counter <= (input_amount + output_amount):     #fill first line with i_x0  i_x1    ....    o_y0    o_y1    ...
        if(first_line_counter <= input_amount):
            file.write("i_x" + str((first_line_counter - 1)))
            file.write("\t")
        else:
            file.write("o_y" + str(out_first_line_count))
            out_first_line_count += 1
            if(out_first_line_count == output_amount):
                file.write("\n")
            else:
                file.write("\t")
        first_line_counter += 1

   

    line_counter = 0
    while line_counter < full_combination_amount:
      
        
        number = format(line_counter, 'b').zfill(input_amount)
        
        if(BigEndian == True):
            in_number_counter = 0
            while in_number_counter < input_amount:
                file.write(str(number[in_number_counter]) + "\t")
                in_number_counter += 1
        else:
            in_number_counter = input_amount - 1
            while in_number_counter >= 0:
                file.write(str(number[in_number_counter]) + "\t")
                in_number_counter -= 1

        out_counter = 0
        while out_counter < output_amount:
            num = random.randint(0,1)
            testbench_readmemb += str(num)
            file.write(str(num) + "\t")
            out_counter += 1
        
        line_counter += 1
        testbench_readmemb += "\n"
        file.write("\n")

                
 #Generate comfotable table for $readmemb               
if(allow_generation):

    #Create new file with name of original table + _testbench_table
    #Result of this operation is such: usersTableName_testbencj_table.txt
    splited_out_path = full_output_path.split(".")
    splited_out_path[0] += "_testbench_table"
    new_path = splited_out_path[0] + "." + splited_out_path[1]

    with open(new_path,'w') as file:
        file.write(testbench_readmemb)
    
