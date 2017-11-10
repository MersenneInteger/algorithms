#include "linked_list.h"
#include <stdlib.h>
#include <string.h>

void create_list(List *list, void (*destroy)(void *data))
{
    list->size = 0;
    list->destroy = destroy;
    list->head = NULL;
    list->tail = NULL;
}

void destroy_list(List *list)
{
    void *data;
    while(list_size(list) > 0)
        if(remove_next(list, NULL, (void**)data) == 0 && list->destroy != NULL)
            list->destroy(data);
    memset(list, 0, sizeof(List));
}

int insert_next(List *list, node *elem, const void *data)
{
    node *new_node;
    if((new_node = malloc(sizeof(List))) == NULL)
        return 0; //unsuccessful insertion
    new_node->data = (void*)data;
    if(elem == NULL){
        //insert at beginning
        if(list_size(list) == 0) 
            list->tail = new_node; //make new_node tail
        new_node->next = list->head; //point nodes next to current head
        list->head = new_node;//new_node is new head
    } else {
        //insert after head
        if(elem->next == NULL) //check if elem is tail
            list->tail = new_node; //append at tail of list
        new_node->next = elem->next;
        elem->next = new_node;
    }
    list->size++;
    //successful insertion
    return 1;
}

int remove_next(List *list, node *elem, void **data)
{
    node *old_node;
    //check if list is empty
    if(list_size(list) == 0)
        return 0;
    if(elem == NULL){
        //removing head
        *data = list->head->data; //store heads data
        old_node = list->head; //node to delete set to head
        list->head = list->head->next;//make head whatever old head is pointing to

        if(list_size(list) == 1) //if only node left, make tail
            list->tail = NULL;
    } else {
        //remove elsewhere in list
        if(elem->next == NULL)//if elem is tail, exit
            return 0;
        *data = elem->next->data; //store data of node to be removed
        old_node = elem->next; 
        elem->next = elem->next->next; //point elem->next to oldnode->next

        if(elem->next == NULL)
            list->tail = elem;
    }
    free(old_node);
    list->size--;
    return 1;
}

int list_size(const List *list)
{
    return list->size;
}

int is_head(List *list, const node *elem)
{
    return elem == list->head? 1: 0;
}

int is_tail(const node *elem)
{
    return elem->next == NULL? 1:0;
}

void print_list(List *list, const node *elem)
{
    while(elem != NULL) {
        printf("%p\n", list_data(elem));
        elem = elem->next;
    }
}

int main()
{
    List *list;
    node *elem;

    create_list(list, NULL);
    elem = list_head(list);
    insert_next(list, elem, (int*)5);
    insert_next(list, elem, (int*)3);
    print_list(list, list_head(list));

    elem = list_head(list);
    remove_next(list, elem, &list_data(elem));
    printf("\nRemoving head: \n");
    print_list(list, list_head(list));

    printf("New list: \n");
    insert_next(list, elem, (int*)7);
    insert_next(list, elem, (int*)2);
    print_list(list, list_head(list));

    printf("\nList head: %p\n", list_head(list)->data);
    printf("List tail: %p\n", list_tail(list)->data);
}
