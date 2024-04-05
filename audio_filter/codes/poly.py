import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

a = [ 1.0, -1.96842779,1.73586071,-0.72447083,0.1203896 ]
b = [0.01020948,0.04083792,0.06125688,0.04083792,0.01020948]

# calculates partial fraction residues, poles and polynomial terms
r, p, k = signal.residuez(b, a)

print(f'r = {r}')
print(f'p = {p}')
print(f'k = {k}')

N = 30

n = np.arange(N)

k = np.copy(k)
k.resize(N)

h = np.array([np.sum(r * np.power(p, k)) for k in n]) + k

plt.stem(n, np.real(h))
plt.xlabel('$n$')
plt.ylabel('$h(n)$')
plt.savefig('../figs/filter_h_n.png')

# generate latex code for table

newline = '\\\\ \\hline\n'

cells = ''

cells += newline.join([f'\t\t${i}$ & ${round(r[i], 3)}$ & ${round(p[i], 3)}$ & ${round(k[i], 3)}$' for i in range(len(p))])

table_code = '''
\\begin{table}[h!]
\t\\centering
\t\\renewcommand\\thetable{1}
\t\\setlength{\\extrarowheight}{9pt}
\t\\resizebox{0.51\\textwidth}{!}{
\t\\begin{tabular}{|c|c|c|c|}
\t\\hline
\t\\textbf{$i$} & \\textbf{$r\\brak{i}$} & \\textbf{$p\\brak{i}$} & \\textbf{$k\\brak{i}$}'''

table_code += newline + cells + newline

table_code += '''
\t\\end{tabular}}
\t\\caption{Values of $ r(i) , p(i) , k(i)$}
\t\\label{tab:values of r(i) , p(i) , k(i)}
\\end{table}
'''

print(table_code)

