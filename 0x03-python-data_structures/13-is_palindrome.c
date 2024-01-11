#include "lists.h"
#include <stddef.h>

/**
 * reverse_list - reverses the second half of the list
 *
 * @her: head of the second half
 * Return: no return
 */
void reverse_list(listint_t **her)
{
	listint_t *previous;
	listint_t *current;
	listint_t *nex;

	previous = NULL;
	current = *her;

	while (current != NULL)
	{
		nex = current->next;
		current->next = previous;
		previous = current;
		current = nex;
	}

	*her = previous;
}

/**
 * compare_list - compares each int of the list
 *
 * @he1: head of the first half
 * @he2: head of the second half
 * Return: 1 if are equals, 0 if not
 */
int compare_list(listint_t *he1, listint_t *he2)
{
	listint_t *temps1;
	listint_t *temps2;

	temps1 = he1;
	temps2 = he2;

	while (temps1 != NULL && temps2 != NULL)
	{
		if (temps1->n == temps2->n)
		{
			temps1 = temps1->next;
			temps2 = temps2->next;
		}
		else
		{
			return (0);
		}
	}

	if (temps1 == NULL && temps2 == NULL)
	{
		return (1);
	}

	return (0);
}

/**
 * is_palindrome - checks if a singly linked list
 * is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palndrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slows, *fasts, *prevs_slow;
	listint_t *scn_halfs, *middles;
	int ispa;

	slows = fasts = prevs_slow = *head;
	middles = NULL;
	ispa = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fasts != NULL && fasts->next != NULL)
		{
			fasts = fasts->next->next;
			prevs_slow = slows;
			slows = slows->next;
		}

		if (fasts != NULL)
		{
			middles = slows;
			slows = slows->next;
		}

		scn_halfs = slows;
		prevs_slow->next = NULL;
		reverse_list(&scn_halfs);
		ispa = compare_list(*head, scn_halfs);

		if (middles != NULL)
		{
			prevs_slow->next = middles;
			middles->next = scn_halfs;
		}
		else
		{
			prevs_slow->next = scn_halfs;
		}
	}
	return (ispa);
}
