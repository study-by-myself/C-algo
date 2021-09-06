#include "singly_linked_list.h"

Node* create_node(dataType data)
{
	Node* new = (Node *)malloc(sizeof(Node));
	new->data = data;
	new->next = NULL;
	return new;
}

void appendNode(Node** head, Node* new)
{
	if (*head == NULL)
		*head = new;
	else
	{
		Node* tail = *head;
		while (tail->next != NULL)
			tail = tail->next;
		tail->next = new;
	}
}

void insertAfter(Node *current, Node* new)
{
	new->next = current->next;
	current->next = new;
}

void insertNewHead(Node **head, Node *newHead)
{
	if (*head == NULL)
		*head = newHead;
	else
	{
		newHead->next = *head;
		*head = newHead;
	}
}

void removeNode(Node** head, Node* remove)
{
	if (*head == remove)
	{
		Node *tmp = *head;
		*head = remove->next;
		free(tmp);
	}
	else
	{
		Node *current = *head;
		while (current != NULL && current->next != remove)
			current = current->next;
		if (current != NULL)
			current->next = remove->next;
	}
}

Node *getNodeAt(Node *head, int location)
{
	Node *current = head;

	while (current != NULL && --location > 0)
		current = current->next;
	return current;
}

int getNodeCount(Node* head)
{
	int count = 0;
	Node* current = head;

	while (current != NULL)
	{
		current = current->next;
		count++;
	}
	return count;
}