`timescale 1ns / 1ps
module Test_8_5;


reg clk;
reg error;
reg [7:0] i_x;
wire [0:4] o_y_dknf;
wire  [0:4] o_y_ddnf;
reg [0:4] o_dknf;
reg [0:4] o_ddnf;

reg [0:4] current_table_value;
reg [0:4] table_out[255:0];
integer counter = 0;

initial begin
$readmemb("Table_8_5_testbench_table.txt",table_out);
$display("COUNTER		INPUT		DKNF		DDNF		TABLE		ERROR");
error = 0;
clk = 0;
i_x = 0;
o_dknf = 0;
o_ddnf = 0;
end


DDNF_8_5 ddnf(i_x[0],i_x[1],i_x[2],i_x[3],i_x[4],i_x[5],i_x[6],i_x[7],o_y_ddnf[0],o_y_ddnf[1],o_y_ddnf[2],o_y_ddnf[3],o_y_ddnf[4]);
DKNF_8_5 dknf(i_x[0],i_x[1],i_x[2],i_x[3],i_x[4],i_x[5],i_x[6],i_x[7],o_y_dknf[0],o_y_dknf[1],o_y_dknf[2],o_y_dknf[3],o_y_dknf[4]);


always @(o_y_ddnf,o_dknf) begin
o_dknf <= o_y_dknf;
o_ddnf <= o_y_ddnf;
end

always @(counter) begin
current_table_value <= table_out[counter];
end

always begin
#10 clk = ~clk;
end

always @(posedge clk) begin

 
if(o_dknf != current_table_value )begin
	error = 1;
	//$display("ERROR! DKNF");
	//$finish;
 end else if(o_ddnf != current_table_value )begin 
	error = 1;
	//$display("ERROR! DDNF");
	//$finish;
 end else begin
	error = 0;
end

$display("%d		%b		%b		%b		%b		%b",counter,i_x,o_dknf,o_ddnf,current_table_value,error);

if (i_x == 8'b1111_1111) begin
	$finish;
end

i_x = i_x + 1;
counter = counter + 1;
end


endmodule

