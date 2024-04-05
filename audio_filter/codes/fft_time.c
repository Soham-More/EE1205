#include <stdio.h>
#include <stdint.h>
#include <complex.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define TEST_COUNT 10000
#define complexf complex float

size_t min(size_t x, size_t y){ return x < y ? x : y; }

complexf* fft_radix2_algo(const complexf* x, size_t len, size_t start, size_t pad)
{
    float pi = 3.14159265359;

    complexf* out = (complexf*)malloc(len * sizeof(complexf));

    if(len == 1)
    {
        out[0] = x[start] + 0 * I;
        return out;
    }

    complexf* E = fft_radix2_algo(x, len / 2, start +   0, pad * 2);
    complexf* O = fft_radix2_algo(x, len / 2, start + pad, pad * 2);

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

complexf* ifft_radix2_algo(const complexf* x, size_t len, size_t start, size_t pad)
{
    float pi = 3.14159265359;

    complexf* out = (complexf*)malloc(len * sizeof(complexf));

    if(len == 1)
    {
        out[0] = x[start] + 0 * I;
        return out;
    }

    complexf* E = ifft_radix2_algo(x, len / 2, start +   0, pad * 2);
    complexf* O = ifft_radix2_algo(x, len / 2, start + pad, pad * 2);

    for(size_t i = 0; i < (len / 2); i++)
    {
        out[i] = E[i] + cexp(2 * pi * I * (float)i / (float)len) * O[i];
    }
    for(size_t i = 0; i < (len / 2); i++)
    {
        out[i + (len / 2)] = E[i] - cexp(2 * pi * I * (float)i / (float)len) * O[i];
    }

    // free memory
    free(E);
    free(O);
    return out;
}

// wrapper for c
complexf* fft_radix2(const complexf* x, size_t len)
{
    return fft_radix2_algo(x, len, 0, 1);
}

// wrapper for c
complexf* ifft_radix2(const complexf* x, size_t len)
{
    return ifft_radix2_algo(x, len, 0, 1);
}

void convolution(const complexf* x, size_t xlen, const complexf* h, size_t hlen, complexf* y)
{
    for (size_t i = 0; i < xlen; i++)
    {
        y[i] = 0;
        for (size_t j = 0; j < min(hlen, i + 1); j++)
        {
            y[i] += x[i - j] * h[j];

            if ((i - j) < 0)
            {
                printf("unexpected error!\n");
            }
        }
    }
}

void mul_array_inplace(complexf* a, const complexf* b, size_t len)
{
    for(size_t i = 0; i < len; i++)
    {
        a[i] *= b[i];
    }
}

complexf* construct_random_array(size_t len)
{
    complexf* out = malloc(len * sizeof(complexf));

    for(size_t i = 0; i < len; i++)
    {
        out[i] = 10.0 * (float)rand()/(float)(RAND_MAX) + 0 * I;
    }

    return out;
}

int main()
{
    // make a transfer function, do multiplication

    srand(time(0));

    time_t begin, end;

    FILE* file = fopen("time.dat", "w");

    for(size_t i = 0; i < 16; i++)
    {
        complexf* x = construct_random_array(1 << i);
        complexf* h = construct_random_array(1 << i);

        complexf* y_conv = construct_random_array(1 << i);

        // test FFT
        begin = clock();
        for(size_t j = 0; j < TEST_COUNT; j++)
        {
            complexf* X = fft_radix2(x, 1 << i);
            mul_array_inplace(X, h, 1 << i);
            complexf* y = ifft_radix2(x, 1 << i);
        }
        double fft_exec_time = (double)(clock() - begin) / CLOCKS_PER_SEC;
        printf("FFT %lu: %fs\n", i, fft_exec_time);

        // test Convolution
        begin = clock();
        for(size_t j = 0; j < TEST_COUNT; j++)
        {
            convolution(x, 1 << i, h, 1 << i, y_conv);
        }
        double conv_exec_time = (double)(clock() - begin) / CLOCKS_PER_SEC;
        printf("Convolution %lu: %fs\n", i, conv_exec_time);

        fprintf(file, "%lu %f %f", i, fft_exec_time, conv_exec_time);

        if(i != 9) fprintf(file, "\n");
    }

    return 0;
}

