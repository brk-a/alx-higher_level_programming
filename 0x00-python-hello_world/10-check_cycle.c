#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * list - linked list
 *
 * Return: 0 if cycle, 1 if no cycle
 */

int check_cycle(listint_t *list)
{
listint_t *i, *j;

i = list;
j = list;

while (i && j)
{
if (j->next == NULL)
return (0);
i = i->next;
j = j->next->next;
if (i == j)
return (1);
}

return (0);
}
