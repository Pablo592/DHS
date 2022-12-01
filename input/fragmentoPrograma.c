int sumar(int a, int b);
int restar(int p, int q, int t);
int sinParametros();

int global = 5;

int main()
{
    int y;
    int x = 5;
    int p, q, r, t, i, j;
    int a = 1, b = 2, c = 3, d;

    y = sumar(x, p);
    p = restar(a, b, c);
    d = sinParametros();

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
        int estoyFor;
        a = 5;
        for (j = 0; j < x; j += 7)
        {
            a = a + x;
            int variable = 5;
            j = a + j;
            a = 5;
        }
    }

    b = a + x;

    if (i < 5)
    {
        b = 3;
        p = restar(a, x, c);
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

int restar(int ar, int br, int cr)
{
    int mo = ar - br - cr;
    return mo;
}

int sinParametros()
{
    int p;
    p = 5 + 6;
    return p;
}