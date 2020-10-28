restart -force;

force i_x0 0 0ns, 1 {10ns} -repeat 20ns;
force i_x1 0 0ns, 1 {20ns} -repeat 40ns;
force i_x2 0 0ns, 1 {40ns} -repeat 80ns;
force i_x3 0 0ns, 1 {80ns} -repeat 160ns;
force i_x4 0 0ns, 1 {160ns} -repeat 320ns;
force i_x5 0 0ns, 1 {320ns} -repeat 640ns;
force i_x6 0 0ns, 1 {640ns} -repeat 1280ns;
force i_x7 0 0ns, 1 {1280ns} -repeat 2560ns;

run @ 2560ns;