#include "dlist.h"
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
        if(remove_node(list, list_tail(list), (void**)&data) == 0 && list->destroy != NULL)
            list->destroy(data);
    memset(list, 0, sizeof(list));
}

int insert_next(List *list, node *elem, const void *data)
{
    node *new_node;
    if(elem == NULL && list_size(list) != 0)
        return 0;
    if((new_node = malloc(sizeof(node))) == NULL)
        return 0;
    new_node->data = (void*)data;

    //if list is empty
    if(list_size(list) == 0) {
        list->head = new_node;
        list->tail = new_node;
        list->head->next = NULL;
        list->head->prev = NULL;
    } else {
        new_node->next = elem->next;
        new_node->prev = elem;
        if(elem->next == NULL) //if elem is tail
            list->tail = new_node; //make new_node tail
        else
            elem->next->prev = new_node; //new_node is prev to what elem->next pointed to
        elem->next = new_node; //insert new_node after elem
    }
    list->size++;
    return 1; //successful insertion
}

int insert_prev(List *list, node *elem, const void *data)
{
    node *new_node;
    if(elem == NULL && list_size(list) != 0)
        return 0;
    if((new_node = (void*)malloc(sizeof(node))) == NULL)
        return 0;
    new_node->data = (void*)data;
    
    //if list is empty
    if(list_size(list) == 0) {
        list->head = new_node;
        list->tail = new_node;
        list->head->next = NULL;
        list->head->prev = NULL;
    } else {
        new_node->prev = elem->prev; //add new_node before elem
        new_node->next = elem;
        if(elem->prev == NULL) //check if elem was head
            list->head = new_node; //make new_node head
        else
            elem->prev->next = new_node; //element whose next is pointing to elem,
        elem->prev = new_node;       //point to new node
    }
    list->size++;
    return 1;
}

int remove_node(List *list, node *elem, void **data)
{
    //prevent return from empty list
    if(elem == NULL || list_size(list) == 0) 
        return 0;
    *data = elem->data;
    if(elem == list->head) {
        list->head = elem->next; //remove head
        if(list->head == NULL)
            list->tail == NULL; //list is empty
        else
            elem->next->prev = NULL; //elem->next is head, prev points to NULL
    } else {
        elem->prev->next = elem->next; //detatch elem from list
        if(elem->next == NULL)
            list->tail = elem->prev; //make new tail
        else
            elem->next->prev = elem->prev; //set node after elems prev to node before elem
    }
    free(elem);
    list->size--;
    return 1;
}

int list_size(const List *list)
{
    return list->size;
}

int is_head(const node *elem)
{
    elem->prev == NULL? 1: 0;
}

int is_tail(const node *elem)
{
    elem->next == NULL? 1: 0;
}

void print_list_forward(List *list, const node *elem)
{
    while(elem != NULL){
        printf("%p\n", list_data(elem));
        elem = elem->next;
    }
}

void print_list_backward(List *list, const node *elem)
{
    while(elem != NULL) {
        printf("%p\n", list_data(elem));
        elem = elem->prev;
    }
}

int main(int argc, char **argv)
{
    List *list;
    node *elem;
    
    create_list(list, NULL);
    
    insert_next(list, list_head(list), (int*)2);
    insert_next(list, list_head(list), (int*)8);
    printf("Forwards: \n");
    print_list_forward(list, list_head(list));

    printf("\nBackwards: \n");
    elem = list_tail(list);
    insert_prev(list, elem, (int*)3);
    print_list_backward(list, elem);

    elem = list_head(list);
    remove_node(list, elem, &list_data(elem));
    printf("\nAfter removing head\n");
    print_list_forward(list, list_head(list));
    
    destroy_list(list);
}
