#include <stdio.h>

#define list_head(list) list->head
#define list_tail(list) list->tail
#define list_data(elem) elem->data
#define list_next(elem) elem->next
#define list_prev(elem) elem->prev

typedef struct node {
    void *data;
    struct node *next;
    struct node *prev;
} node;

typedef struct linked_list {
    int size;
    int (*match)(const void *key1, const void *key2);
    void (*destroy)(void *data);
    struct node *head;
    struct node *tail;
} List;

void create_list(List *list, void (*destroy)(void *data));
void destroy_list(List *list);
int insert_next(List *list, node *elem, const void *data);
int insert_prev(List *list, node *elem, const void *data);
int remove_node(List *list, node *elem, void **data);
int list_size(const List *list);
int is_head(const node *elem);
int is_tail(const node *elem);

