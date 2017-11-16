#include <stdlib.h>
#include <string.h>
#include "clist.h"

void create_list(Clist *list, void (*destroy)(void *data))
{
    list->size = 0;
    list->destroy = destroy;
    list->head = NULL;
}

void destroy_list(Clist *list)
{
    void *data;
    while(list_size(list) > 0)
        if(remove_next(list, list->head, (void**)&data) == 0 && list->destroy != NULL)
            list->destroy(data);
    memset(list, 0, sizeof(Clist));
}
int insert_next(Clist *list, node *elem, const void *data)
{
    node *new_node;
    if((new_node = malloc(sizeof(node))) == NULL)
        return 0;
    new_node->data = (void *)data;

    if(list_size(list) == 0) { //check if list is empty
        new_node->next = new_node; //point new_node to itself
        list->head = new_node; //make head of list
    } else { //check if list is non-empty
        new_node->next = elem->next; //point new_node to what elem was pointed to
        elem->next = new_node; //point elem to new_node
    }
    list->size++;
    return 1; //successful insertion
}
int remove_next(Clist *list, node *elem, void **data)
{
    node *old_node;
    if(list_size(list) == 0)
        return 0;
    *data = elem->next->data;
    if(elem->next == elem) {//check if only element in list
        old_node = elem->next; //remove elem after node, if only elem, it points to itself
        list->head = NULL;
    } else {
        old_node = elem->next;
        elem->next = elem->next->next; //point elem to whatever removed node was pointing to
    }
    free(old_node);
    list->size--;
    return 1; //successful removal
}

int list_size(Clist *list)
{
    return list->size;
}

void print_list(Clist *list, const node *elem)
{
    for(int i = 0; i < list_size(list); i++) {
        printf("%p\n", list_data(elem));
        elem = elem->next;
    }
}

int main()
{
    Clist *list;
    node *elem;

    create_list(list, NULL);
    elem = list_head(list);
    insert_next(list, elem, (int*)7);
    insert_next(list, list->head, (int*)9);
    print_list(list, list_head(list));
    destroy_list(list);
}
