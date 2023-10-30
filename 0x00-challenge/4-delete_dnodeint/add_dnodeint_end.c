#include <string.h>
#include <stdlib.h>
#include "lists.h"

/**
 * add_dnodeint_end - Add a node at the end of a list
 *
 * @head: The address of the pointer to the first element of the list
 * @n: The number to store in the new element
 *
 * Return: A pointer to the new element
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *current;
	dlistint_t *l;

	current = malloc(sizeof(dlistint_t));
	if (current == NULL)
	{
		return (NULL);
	}
	current->n = n;
	current->next = NULL;
	if (*head == NULL)
	{
		*head = current;
		current->prev = NULL;
		return (current);
	}
	l = *head;
	while (l->next != NULL)
	{
		l = l->next;
	}
	l->next = current;
	current->prev = l;
	return (current);
}
