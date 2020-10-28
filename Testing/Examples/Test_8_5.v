`timescale 1ns / 1ps
module Test_8_5;
	
reg clk;
reg error;
reg [7:0] i_x;
wire [4:0] o_y_dknf;
wire  [4:0] o_y_ddnf;
reg [4:0] o_dknf;
reg [4:0] o_ddnf;

initial begin
$display("INPUT		DKNF		DDNF		ERROR");
error = 0;
clk = 0;
i_x = 0;
end


DDNF_8_5 ddnf(i_x[0],i_x[1],i_x[2],i_x[3],i_x[4],i_x[5],i_x[6],i_x[7],o_y_ddnf[0],o_y_ddnf[1],o_y_ddnf[2],o_y_ddnf[3],o_y_ddnf[4]);
DKNF_8_5 dknf(i_x[0],i_x[1],i_x[2],i_x[3],i_x[4],i_x[5],i_x[6],i_x[7],o_y_dknf[0],o_y_dknf[1],o_y_dknf[2],o_y_dknf[3],o_y_dknf[4]);



always @(o_y_dknf,o_y_ddnf) begin
o_dknf <= o_y_dknf;
o_ddnf <= o_y_ddnf;
end

always begin
#10 clk = ~clk;
end

always @(posedge clk) begin
i_x = i_x + 1;

if(o_dknf != o_ddnf) begin
	error = 1;
	$display("ERROR!");
	$finish;
 end else begin
	error = 0;
end

$display("%b		%b		%b		%b",i_x,o_y_dknf,o_y_ddnf,error);

if (i_x == 8'b11111111) begin
	$finish;
end

end

endmodule
