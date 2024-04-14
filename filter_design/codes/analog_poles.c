#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    unsigned int N = 4;

    double PI = 3.14159265358979323846;
    double omega_lp = 1.0f;
    double epsilon = 0.3f;
    double b_k = asinh(1.0/epsilon) / (double)N;

    FILE* file = fopen("poles.dat", "w");

    for(unsigned int k = 0; k < 2 * N; k++)
    {
        double a_k = (2.0 * k + 1.0) * PI / (2.0 * N);

        double s_k_real = -omega_lp * sin(a_k) * sinh(b_k);
        double s_k_imag = -omega_lp * cos(a_k) * cosh(b_k);

        fprintf(file, "%f %f%c", s_k_real, s_k_imag, k != 2*N ? '\n' : '0');
    }

    fclose(file);

    return 0;
}

