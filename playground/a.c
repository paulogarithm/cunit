// Tests unipol

#include <stdio.h>

int my_isnum(char *str);

int main(void) {
	printf("%d\n", my_isnum("3"));
	printf("%d\n", my_isnum("0"));
	printf("%d\n", my_isnum("-1"));
	printf("%d\n", my_isnum("29830"));
	printf("%d\n", my_isnum("hello"));
	printf("%d\n", my_isnum("-1a"));
}
