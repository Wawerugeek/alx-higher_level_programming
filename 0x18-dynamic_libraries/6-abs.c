#include "main.h"
/**
 *_abs - determines the absolute value of the number from zero
 *@i: the interger subject to conversion
 *Return: absolute value
 */
int _abs(int i)
{
	if (i < 0)
		i = i * -1;
	return (i);
}
