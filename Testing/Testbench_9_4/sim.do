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

vlog  DDNF_9_4.v DKNF_9_4.v Test_9_4.v

# Open testbench module for simulation

vsim work.Test_9_4

# Add all testbench signals to waveform diagram

add wave /Test_9_4/clk
add wave /Test_9_4/error
add wave /Test_9_4/i_x
add wave /Test_9_4/o_y_dknf
add wave /Test_9_4/o_y_ddnf
add wave /Test_9_4/current_table_value 
add wave /Test_9_4/counter



onbreak resume

# Run simulation
run -all

wave zoom full

