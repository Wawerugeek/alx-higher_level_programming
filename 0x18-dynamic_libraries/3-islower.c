#include "main.h"
/**
 *_islower - checks for llowwr cses
 *@c: character totest
 *Return: nothing
 */
int _islower(int c)
{
	if (c >= 'a' && c <= 'z')
		return (1);
	else
		return (0);
}
