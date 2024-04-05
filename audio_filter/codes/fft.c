#include <stdio.h>
#include <stdint.h>
#include <complex.h>
#include <stdlib.h>

complex float* fft_radix2_algo(float* x, size_t len, size_t start, size_t pad)
{
    float pi = 3.14159265359;

    complex float* out = (complex float*)malloc(len * sizeof(complex float));

    if(len == 1)
    {
        out[0] = x[start] + 0 * I;
        return out;
    }

    complex float* E = fft_radix2_algo(x, len / 2, start +   0, pad * 2);
    complex float* O = fft_radix2_algo(x, len / 2, start + pad, pad * 2);

    for(size_t i = 0; i < (len / 2); i++)
    {
        out[i] = E[i] + cexp(-2 * pi * I * (float)i / (float)len) * O[i];
    }
    for(size_t i = 0; i < (len / 2); i++)
    {
        out[i + (len / 2)] = E[i] - cexp(-2 * pi * I * (float)i / (float)len) * O[i];
    }

    // free memory
    free(E);
    free(O);
    return out;
}

// wrapper for python
void fft_radix2(float* x, float* y_real, float* y_imag, size_t len)
{
    complex float* out = fft_radix2_algo(x, len, 0, 1);

    for(size_t i = 0; i < len; i++)
    {
        //printf("out[%lu] = %f + %fi\n", i, creal(out[i]), cimag(out[i]));

        y_real[i] = creal(out[i]);
        y_imag[i] = cimag(out[i]);
    }
}
