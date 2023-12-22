#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * main - This program creates 5 zombie precesses
 * Return: 0 if success or 1 otherwise
 */

int main(void)
{
	pid_t zombie;
	int i;

	for (i = 0; i < 5; i++)
	{
		zombie = fork();
		if (zombie == -1 || zombie == 0)
			exit(1);
		else
			printf("Zombie process created, PID: %d\n", zombie);
	}
	while (1)
		sleep(1);

	return (0);
}
