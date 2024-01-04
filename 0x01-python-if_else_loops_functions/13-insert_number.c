#include "lists.h"

/**
 *insert_node - Inserts a number into sorted singly-linked list
 *@head: Pointer the head of the linked list
 *@number: The number to insert
 *
 *Return: NULL in case of failure
 *	a pointer to the new mode
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *neu;

	neu = malloc(sizeof(listint_t));
	if (neu == NULL)
		return (NULL);
	neu->n = number;

	if (node == NULL || node->n >= number)
	{
		neu->next = node;
		*head = neu;
		return (neu);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	neu->next = node->next;
	node->next = neu;

	return (neu);
}
