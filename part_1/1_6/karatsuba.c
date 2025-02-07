#include <stdio.h>
#include <math.h>

#define max(a, b)             \
({                            \
    __typeof__(a) _a = (a);   \
    __typeof__(b) _b = (b);   \
    _a > _b ? _a : _b;        \
})

int karatsuba(int x, int y);

int main(void) {
    int x = 5678;
    int y = 123;

    printf("Karatsuba Result: %d\n", karatsuba(x, y));
    printf("Direct Multiplication Result: %d\n", x * y);
    return 0;
}

int karatsuba(int x, int y) {
    if (x < 10 || y < 10) {
        return x * y;
    }

    int x_length = (int)log10(x) + 1;
    int y_length = (int)log10(y) + 1;


    int n = max(x_length, y_length);
    int half_n = n / 2;

    int a = x / (int)pow(10, half_n);
    int b = x % (int)pow(10, half_n);

    int c = y / (int)pow(10, half_n);
    int d = y % (int)pow(10, half_n);

    int ac = karatsuba(a, c);
    int bd = karatsuba(b, d);
    int ad_bc = karatsuba(a + b, c + d) - ac - bd;

    return pow(10, 2 * half_n) * ac + pow(10, half_n) * ad_bc + bd;
}
