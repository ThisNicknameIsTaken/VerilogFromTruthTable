###########################
# Simple modelsim do file #
###########################

# Delete old compilation results
if { [file exists "work"] } {
    vdel -all
}

# Create new modelsim working library

vlib work

# Compile all the Verilog sources in current folder into working library

vlog  DDNF_13_8.v DKNF_13_8.v Test_13_8.v

# Open testbench module for simulation

vsim work.Test_13_8

# Add all testbench signals to waveform diagram

add wave /Test_13_8/clk
add wave /TTest_13_8/error
add wave /Test_13_8/i_x
add wave /Test_13_8/o_y_dknf
add wave /Test_13_8/o_y_ddnf
add wave /Test_13_8/current_table_value 
add wave /Test_13_8/counter



onbreak resume

# Run simulation
run -all

wave zoom full

