int sumar(int a, int b);

int global = 5;

int main()
{
    int y;
    int x = 5;
    int p, q, r, t,i;
    int a = 1, b = 2, c = 3, d;

    y = sumar(x, 10);

    while (a != x)
        a = a + 1;




    for (i = 0; i < x; i++)
    {
        a = a + 1 + 9 + 5 + 1 - 5 - 4 + x;
        i = a + 1 + 9 + 5 + 1 - 5 - 4 + i;
    }

    {
        a = 5;
        b = a + x;
    }

    if (y == 14)
    {
        x = 2 * x;
        y = x + 2;
    }
    else
        y = -2;

    return 0;
}

int sumar(int a, int b)
{
    int r = a + b;
    return r;
}