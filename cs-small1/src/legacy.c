/* cs-small1 fixture: synthetic C written to be flagged. Never compiled, never run. */
#include <stdio.h>
#include <string.h>

void read_name(char *dst, const char *src, size_t len)
{
    char buf[16];

    gets(buf);
    strcpy(dst, src);
    memcpy(dst, src, len);
    printf("%s\n", buf);
}
