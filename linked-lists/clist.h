#include <stdio.h>

#define list_head(list) list->head
#define list_data(elem) elem->data
#define list_next(elem) elem->next

typedef struct node {
    void *data;
    struct node *next;
} node;

typedef struct clist {
    int size;
    int (*match)(const void *key1, const void *key2);
    void (*destroy)(void *data);
    struct node *head;
} Clist;

void create_list(Clist *list, void (*destroy)(void *data));
void destroy_list(Clist *list);
int insert_next(Clist *list, node *elem, const void *data);
int remove_next(Clist *list, node *elem, void **data);
int list_size(Clist *list);
