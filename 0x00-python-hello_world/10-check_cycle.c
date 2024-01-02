#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it or not
 * @list: pointer to the linked list head
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *oldNode, *newNode;

	if (!(list == NULL || list->next == NULL))
	{
		oldNode = list;
		newNode = list->next;

		while (newNode != NULL && newNode->next != NULL)
		{
		if (oldNode == newNode)
			return (1);

		oldNode = oldNode->next;
		newNode = newNode->next->next;
		}
	return (0);
	}
	else
		return (0);
}
