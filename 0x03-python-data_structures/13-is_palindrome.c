#include "lists.h"
#include <stddef.h>

short checkPalindrome(listint_t **, listint_t **);

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to pointer of head of listint_t
 * Return: 1 if it's a palindrome, 0 if it is not
 */
int is_palindrome(listint_t **head)
{
	listint_t *tail = *head;

	return (checkPalindrome(head, &tail));
}
/**
 * checkPalindrome - checks for a palindrome recursively
 * @head: pointer to pointer of head of listint_t
 * @tail: pointer to pointer of tail of the list
 *
 * checks the head (start node) and tail(end node)
 * and compares them if the match or not
 * recursively compares head and tail till hits mid
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
short checkPalindrome(listint_t **head, listint_t **tail)
{
	short palindromeOrNot, currentPalindrome;

	if (*head != NULL)
	{
	palindromeOrNot = checkPalindrome(&(*head)->next, tail);
	currentPalindrome = ((*head)->n == (*tail)->n);
	*tail = (*tail)->next;

	return (palindromeOrNot && currentPalindrome);
	}
	else
		return (1);
}
