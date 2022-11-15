int sumar(int a, int b);

int global = 5;

int main()
{
    int y;
    int x = 5;
    int p, q, r, t, i;
    int a = 1, b = 2, c = 3, d;

    y = sumar(x, p);

    while (a != x)
    {
        a *= 3 + 1 - 5 * 8 + 5 - 7 / 4;
        a = a + 1;
        a /= 2;
        a %= 2;
        a += 2;
        b *= 2;
        a -= 2;
        a %= 3 + 1 - 5 * 8 + 5 - 7 / 4;
        a %= 3 + 3 - 5 * (8 + 5 - 7 / 4);
        a -= 3 + 3 - 5 - (8 + 5 - 7 / 4);
        a /= (8 + 5 - 7 / 4);
    }

    for (i = 0; i < x; i += 7)
    {
        a = a + x;
        i = a + i;
        a = 5;
    }

    b = a + x;

    if (i < 5)
    {
        b = 3;
        b = a + x;
    }
    else
    {
        b = 7;
    }

    return 0;
}

int sumar(int a, int b)
{
    int r = a + b + 8;
    return r;
}