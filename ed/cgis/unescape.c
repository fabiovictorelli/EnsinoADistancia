#include <stdio.h>
#include <string.h>

char hex2char (char* s)
{
  char c = (isalpha (*s) ? toupper (*s) - 'A' + 10 : *s - '0') * 16;

  return c + (isalpha (*(s + 1)) ? toupper (*(s + 1)) - 'A' + 10 : *(s + 1) - '0');
}

int htmlRetireEscapes (char* ln, int tam)
{
  char* s = memchr (ln, '+', tam);

  while (s != NULL)
    {
      *s = ' ';
      s = memchr (s + 1, '+', tam - (int) (s - ln) - 1);
    }

  s = memchr (ln, '%', tam);

  while (s != NULL)
    {
      if (*(s + 1) == '\0' ||
          *(s + 2) == '\0')
        break;
    {
      int t = (tam -= 2) - (int) (s - ln) - 1;

      *s = hex2char (s + 1);
      memcpy (s + 1, s + 3, t);

      s = memchr (s + 1, '%', t);
    }
    }

  return tam;
}

void main (void)
{
  char linha[BUFSIZ];
  int  tamEntrada=0;

  while (fgets (linha, sizeof (linha), stdin) != NULL) {
  	tamEntrada=htmlRetireEscapes (linha, strlen (linha));
        linha [tamEntrada] = '\0';
  	fputs (linha, stdout);
  }
}
