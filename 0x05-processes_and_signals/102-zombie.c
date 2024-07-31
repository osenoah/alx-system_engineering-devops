#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>


int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}


int main(void)
{
	int i;

	for (i = 0; i < 5; i++)
	{
		if (fork() == 0)
		{
			dprintf(1, "Zombie process created, PID: %d\n", getpid());
			return (0);
		}
	}
	infinite_while();
	return (0);
}
