#include <stdio.h>
#include <math.h>   

#define SIZE 100

int main()
{
    FILE* values = fopen("./values.txt", "w");

    float min =  0.0f;
    float max = 12.0f;

    float t[SIZE];

    // t values
    for(int i = 0; i < SIZE; i++)
    {
        t[i] = min + ((max - min) * i) / SIZE;
        fprintf(values, "%f%c", t[i], i != SIZE - 1 ? ' ' : '\n');
    }

    for(int i = 0; i < SIZE; i++)
    {
        float unitStep = 1.0;
        if(t[i] < 5.0) unitStep = 0.0;

        float x_t = exp(-3.0f * t[i]) * unitStep;
        fprintf(values, "%.12f%c", x_t, i != SIZE - 1 ? ' ' : '\n');
    }

    fclose(values);

    return 0;
}