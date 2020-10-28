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
import re       # To split string of raw data by tabs

#---------------------------------------------------------------------------------------INPUT ARGUMENTS
parser = argparse.ArgumentParser(description="Verilog truth table code generator")

parser.add_argument("--mode", default="SOP",help = "(Optional, SOP is default value)This argument stands for generation mode: SOP for DNF and POS for KNF")
parser.add_argument("--po",required=True,help="Path to save output file")
parser.add_argument("--pi",required=True,help="Path to source truth table")

console_arguments = parser.parse_args()

mode = console_arguments.mode
full_output_path = console_arguments.po
full_input_path = console_arguments.pi

if(mode != "POS" and mode != "SOP"):
    raise Exception("Illegal mode value! It could be only SOP or POS or empty")


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


if(module_format != "v"):
    raise Exception("Illegal output file extension. It should be verilog (.v)")
#----------------------------------------------------------------------------------------





#------------------------------------------------------------------------------------------------READING INPUT FILE
raw_text_lines = []                         # all data of input file without formatting
is_exist = os.path.isfile(full_input_path)
if is_exist:
    with open(full_input_path) as file:
        if file.readable:
            raw_text_lines = file.readlines()
        else:
            raise Exception("Couldn`t read file!")
else:
    raise Exception("No such file!")
#------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------SIMPLE DATA PROCESSING
# checking if input data is correct
# check if there are more 1 lines in file
# check if there are the same amount of elements in each line
raw_text_lines_length = len(raw_text_lines)
if(raw_text_lines_length <= 1):
    raise Exception("You should have more than one line in file!")

# creating array for splitting data by tabs   
raw_data = []

# Splitting data by tabs
for line in raw_text_lines:
    line = line.strip()     # remove \n from strings
    raw_data.append(re.split(r'\t+',line))

# searching indexes of input (i_) and output (o_) signals in first line of file, if found at least one not (i_) or (o_) signal, exception will occure
input_indexes = []
output_indexes = []

first_line = raw_data[0]
counter = 0
for signal_element in first_line:
    in_index = signal_element.find("i_")
    out_index = signal_element.find("o_")
    
    if(in_index == 0):
        input_indexes.append(counter)
    elif(out_index == 0):
        output_indexes.append(counter)
    else:
        raise Exception("Wrong name of input or output signals! Input signals should start with i_, output should start with o_")
    counter += 1

if(len(input_indexes) < 1):
    raise Exception("Must be more input signals!")


if(len(output_indexes) < 1):
    raise Exception("Must be more output signals!")
#------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------------------GENERATING OUTPUT
output_assign_string = ""

if(mode == "SOP"):
    #searching 1 in outputs
    for o_index in output_indexes:
        
        prev_found = 0
        counter = 0
    
        for line in raw_data:
            if(counter == 0):
                output_assign_string += ("assign " + line[o_index] + " = ")
                counter += 1
                continue

            str = ""
            if(line[o_index] == '1'):
                if(prev_found == 1):
                    output_assign_string += " | "
                str += "("

                count_index = 0
                for index in input_indexes:
                    num = line[index]
                    if(num == '1'):
                        str += raw_data[0][index]
                    elif(num == '0'): 
                        str += ("~" + raw_data[0][index])
                    else:
                        raise Exception("Signal should be only 0 or 1!"); 

                    if(count_index == len(input_indexes) - 1):
                        str += ")"
                    else:
                        str += " & "  

                    count_index += 1

                output_assign_string += str
                prev_found = 1

            if(counter == len(raw_data) - 1):
                output_assign_string += ";\n"
            counter += 1
else:
    for o_index in output_indexes:
        
        prev_found = 0
        counter = 0
    
        for line in raw_data:
            if(counter == 0):
                output_assign_string += ("assign " + line[o_index] + " = ")
                counter += 1
                continue

            str = ""
            if(line[o_index] == '0'):
                if(prev_found == 1):
                    output_assign_string += " & "
                str += "("
                count_index = 0
                for index in input_indexes:
                    num = line[index]
                    if(num == '0'):
                        str += raw_data[0][index]
                    elif(num == '1'): 
                        str += ("~" + raw_data[0][index])
                    else:
                        raise Exception("Signal should be only 0 or 1!");    
                    
                    if(count_index == len(input_indexes) - 1):
                        str += ")"
                    else:
                        str += " | "  

                    count_index += 1

                output_assign_string += str
                prev_found = 1

            if(counter == len(raw_data) - 1):
                output_assign_string += ";\n"
            counter += 1

#print(output_assign_string)
#------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------------------WRITING OUTPUT
module_begin_string = ("module " + module_name +"(")
counter = 0
for element in raw_data[0]:
    if(counter != len(raw_data[0])):
        module_begin_string += (element)
        if(counter < (len(raw_data[0]) - 1)):
            module_begin_string += ", "
        counter += 1    
module_begin_string +=");\n"


input_string = "\tinput "
counter = 0
for i_index in input_indexes:
    input_string += raw_data[0][i_index]

    if(counter == len(input_indexes) - 1):
        input_string += ";\n"
    else:
        input_string += ", "
    counter += 1

output_string = "\toutput "
counter = 0
for o_index in output_indexes:
    output_string += raw_data[0][o_index]

    if(counter == len(output_indexes) - 1):
        output_string += ";\n"
    else:
        output_string += ", "
    counter += 1   

endmodule_string = "endmodule\n"

with  open(full_output_path,'w',encoding= 'utf-8') as module_file:
    module_file.write(module_begin_string)
    module_file.write(input_string)
    module_file.write(output_string)
    module_file.write(output_assign_string)
    module_file.write(endmodule_string)


