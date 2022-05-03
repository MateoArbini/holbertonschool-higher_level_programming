#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
/**
 *is_palindrome - function that checks if a singly liked list is a palindrome
 *@head: head of the list
 *Return: 0 if it is not a palindrome, 1 otherwise
 **/
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	listint_t *temp2 = *head;
	int array[5000], i = 0, len = 0;

	if (!head)
		return (0);
	if (!*head || (*head)->next == NULL)
		return (1);

	for (len = 0; temp2->next != NULL; len++)
	{
		temp2 = temp2->next;
	}

	for (i = 0; i <= len; i++)
	{
		array[i] = temp->n;
		temp = temp->next;
	}

	for (i = 0; i < len; i++, len--)
	{
		if (array[len] != array[i])
		{
			return (0);
		}
	}
	return (1);
}
