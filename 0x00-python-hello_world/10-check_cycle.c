#include "lists.h"
/**
 *check_cycle - function that checks if a list has a cycle
 *@head: list given by the user
 *Return: 0 if theres no cycle, 1 if there is
 **/
int check_cycle(listint_t *head)
{
	listint_t *aux1 = head;
	listint_t *aux2 = head;

	if (!head)
		return (0);
	while (1)
	{
		if (aux2->next != NULL && aux2->next->next != NULL)
		{
			aux1 = aux1->next;
			aux2 = aux2->next->next;
			if (aux2 == aux1)
				return (1);
		}
		else
			return (0);
	}
}
