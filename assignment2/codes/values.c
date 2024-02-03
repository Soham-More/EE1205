#include <stdio.h>
#include <math.h>

#define SIZE 100

int main()
{
    FILE* values = fopen("./values.txt", "w");

    float min = -2.9f;
    float max = 12.0f;

    float s[SIZE];

    // n values
    for(int i = 0; i < SIZE; i++)
    {
        s[i] = min + ((max - min) * i) / SIZE;
        fprintf(values, "%f%c", s[i], i != SIZE - 1 ? ' ' : '\n');
    }

    for(int i = 0; i < SIZE; i++)
    {
        float X_s = exp(-5.0f * (s[i] + 3.0f)) / (s[i] + 3.0);
        fprintf(values, "%f%c", X_s, i != SIZE - 1 ? ' ' : '\n');
    }

    fclose(values);

    return 0;
}
