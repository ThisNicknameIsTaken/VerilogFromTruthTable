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

vlog  DDNF_8_5.v DKNF_8_5.v Test_8_5.v

# Open testbench module for simulation

vsim work.Test_8_5

# Add all testbench signals to waveform diagram

add wave /Test_8_5/clk
add wave /Test_8_5/error
add wave /Test_8_5/i_x
add wave /Test_8_5/o_y_dknf
add wave /Test_8_5/o_y_ddnf
add wave /Test_8_5/current_table_value 
add wave /Test_8_5/counter



onbreak resume

# Run simulation
run -all

wave zoom full

