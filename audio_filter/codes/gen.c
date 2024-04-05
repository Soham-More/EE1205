#include <stdio.h>

#define _len_(x,ty) sizeof(x)/sizeof(ty)
#define N 20

float x[] = {1, 2, 3, 4, 2, 1};

float x_n(int n)
{
    if (n < 0) return 0.0f;
    if (n >= _len_(x, float)) return 0.0f;

    return x[n];
}

float delta(int n)
{
    if (n != 0) return 0.0f;
    return 1.0f;
}

int main()
{
    FILE* file = fopen("values.dat", "w");

//    // write x(n) values
//    for(int i = 0; i < _len_(x, float) - 1; i++)
//    {
//        fprintf(file, "%f ", x[i]);
//    }
//    fprintf(file, "%f\n", x[_len_(x, float) - 1]);

    // Response to x(n)
    float y_prev = 0.0f;
    for(int i = 0; i < N - 1; i++)
    {
        float y_n = x_n(i) + x_n(i - 2) - 0.5f * y_prev;

        fprintf(file, "%f ", y_n);

        y_prev = y_n;
    }
    fprintf(file, "%f\n", x_n(N - 1) + x_n(N - 3) - 0.5f * y_prev);

    // Response to impulse
    y_prev = 0.0f;
    for(int i = 0; i < N - 1; i++)
    {
        float y_n = delta(i) + delta(i - 2) - 0.5f * y_prev;

        fprintf(file, "%f ", y_n);

        y_prev = y_n;
    }
    fprintf(file, "%f", delta(N - 1) + delta(N - 3) - 0.5f * y_prev);

    return 0;
}

