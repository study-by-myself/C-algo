#ifndef SINGLY_LINKED_LIST_H
#define SINGLY_LINKED_LIST_H

#include <stdio.h>
#include <stdlib.h>

typedef int dataType;

typedef struct Snode {
	dataType data;
	struct Snode *next;
}	Node;




#endif