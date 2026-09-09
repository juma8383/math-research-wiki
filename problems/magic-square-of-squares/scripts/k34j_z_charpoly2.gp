\\ hyperellcharpoly expects the polynomial in x with y^2=... implicit; maybe
\\ it needs the 'hyperell' form [f] with x being the variable AND the input
\\ must be squarefree of even degree. f has degree 8, ok. The type error: f is
\\ t_POL — maybe it wants the polynomial in variable x with y^2 - f form?
\\ docs: hyperellcharpoly(f) with f the polynomial such that curve is y^2 = f(x),
\\ f must have ODD degree? or any even degree? Try y^2+f vs f vs degree 9 form.
f = 8*x^8 + 1016*x^4 + 9;
print(hyperellcharpoly(x^9 + 2));
quit