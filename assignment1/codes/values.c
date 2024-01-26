#include <stdio.h>
#include <math.h>

int main()
{
    FILE* values = fopen("./values.txt", "w");

    // n values
    for(int i = -4; i < 12; i++)
    {
        fprintf(values, "%f ", (float)i);
    }
    fprintf(values, "%f\n", 12.0);

    for(int i = -4; i < 12; i++)
    {
        float UnitStep = 1.0f;
        if(i < 0) UnitStep = 0.0f;

        fprintf(values, "%f ", 2.0f * powf(2.0, i / 2.0) * UnitStep);
    }
    fprintf(values, "%f\n", 2.0f * powf(2.0, 6.0));
    
    for(int i = -4; i < 12; i++)
    {
        float UnitStep = 1.0f;
        if(i < 0) UnitStep = 0.0f;

        fprintf(values, "%f ", sqrtf(3.0) * powf(3.0, i / 2.0) * UnitStep);
    }
    fprintf(values, "%f\n", sqrtf(3.0) * powf(3.0, 6.0));

    for(int i = -4; i < 12; i++)
    {
        float UnitStep = 1.0f;
        if(i < 0) UnitStep = 0.0f;

        fprintf(values, "%f ", powf(1.0 / 3.0, (double)i) * UnitStep / 3.0f);
    }
    fprintf(values, "%f", powf(1 / 3.0, 12.0) / 3.0f);

    fclose(values);

    return 0;
}
