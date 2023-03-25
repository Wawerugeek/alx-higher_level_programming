#include "main.h"
/**
 *_isalpha - checks for a lower case character
 *@c: the charcter
 *Return: 1 or zero
 */
int _isalpha(int c)
{
	if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'))
		return (1);
	else
		return (0);
}
