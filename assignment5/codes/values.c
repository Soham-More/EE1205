#include <stdio.h>
#include <math.h>   

#define SAMPLE_POINTS_PER_RAD 10
#define SAMPLE_TOAL (200 * SAMPLE_POINTS_PER_RAD)

// |X(jw)| without the spectral point
float X(double jw)
{
    if(fabs(jw) > 50.0) return 0.0;

    return (1 - fabs(jw)/50.0);
}

int main()
{
    FILE* values = fopen("./values.txt", "w");

    float min =  0.0f;
    float max = 200.0f;

    unsigned int samplePointsPerRad = 10;

    float t[SAMPLE_TOAL];

    // t values
    for(int i = 0; i < SAMPLE_TOAL; i++)
    {
        t[i] = min + ((max - min) * i) / SAMPLE_TOAL;
        fprintf(values, "%f%c", t[i], i != SAMPLE_TOAL - 1 ? ' ' : '\n');
    }

    for(int i = 0; i < SAMPLE_TOAL; i++)
    {
        int k = (i % (100 * SAMPLE_POINTS_PER_RAD));

        float jw = k / 10.0;

        fprintf(values, "%.12f%c", X(jw) + X(100.0 - jw), i != SAMPLE_TOAL - 1 ? ' ' : '\n');
    }

    fclose(values);

    return 0;
}