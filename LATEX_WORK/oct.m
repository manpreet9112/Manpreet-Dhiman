#include<octave/oct.h>
output "the_file.eps"
gset term postscript eps

theta = linspace(0, 60, 200);

function r = Na(theta, L)
    W = 800*1000;
    w = 20;
    w_one = 200*1000;
    po180 = 3.14159 / 180;

    r = (w_one * 1.5 + (w_one*L).*(L.*cos(theta * po180)) – W*(L-3.3)) / 2.3;
endfunction

xlabel("T")
ylabel("Na")
plot(theta, Na(theta, 2), "-;aaaaaaaaa;", theta, Na(theta, 4), "-;bbbbbbbbb;", theta, Na(theta, 5),
"-;cccccccccc;")h
