#include <stdio.h>
#include <math.h>
#include <stdbool.h>
void b1(int, int);
void b2(int, int, int);
bool getuser(void);
int main()
{
    bool check = false;
    while (check != true)

        check = getuser();

    return 0;
}

bool getuser(void)
{
    double a, b, c;
    printf("Nhap a b c: ");
    while (!(scanf("%lf", &a)) || !(scanf("%lf", &b)) || !(scanf("%lf", &c)))
        ;
    return true;
}