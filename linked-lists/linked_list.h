#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    void *data;
    struct node *next;
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
int remove_next(List *list, node *elem, void **data);
int list_size(const List *list);
struct node *head(const List *list);
struct node *tail(const List *list);
int is_head(const node *elem);
int is_tail(const node *elem);
void list_data(const node *elem);
struct node *list_next(const node *elem);
