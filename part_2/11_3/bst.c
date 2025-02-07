#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct node{
    int value;
    int size;
    struct node* parent;
    struct node* leftChild;
    struct node* rightChild;
} node;

node* root;

int select(int orderStat){
    node* trav = root;
    int currentOrder = orderStat;
    while (1){
        int leftChildSize = trav->leftChild != NULL ? trav->leftChild->size : 0;
        if (currentOrder == (leftChildSize + 1)){
            return trav->value;
        }else if(currentOrder <= leftChildSize){
            trav = trav->leftChild;
        }else if(trav->rightChild != NULL && currentOrder > (leftChildSize + 1)){
            currentOrder = currentOrder - (leftChildSize + 1);
            trav = trav->rightChild;
        }else{
            return 0;
        }
    }
}

void insert(int value){
    node* tmp = malloc(sizeof(node));
    tmp->value = value;
    tmp->leftChild = NULL;
    tmp->rightChild = NULL;
    tmp->parent = NULL;
    tmp->size = 1;

    if(root == NULL){
        root = tmp;
        return;
    }

    node* trav = root;
    while (trav != NULL){
        int pivot = trav->value;
        trav->size++;
        if (value <= pivot){
            if (trav->leftChild == NULL) {
                trav->leftChild = tmp;
                tmp->parent = trav;
                trav = NULL;
            }else{
                trav = trav->leftChild;
            }
        }else{
            if (trav->rightChild == NULL){
                trav->rightChild = tmp;
                tmp->parent = trav;
                trav = NULL;
            }else{
                trav = trav->rightChild;
            }
        }
    }

    return;
}

int main(void){
    struct timespec begin;
    timespec_get(&begin, TIME_UTC);
    root = NULL;

    FILE* file = fopen("problem11_3.txt", "r");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    int sum = 0;
    int buffer;
    while (fscanf(file, "%i", &buffer) == 1) { 
        insert(buffer);
        int totalNodes = root->size;
        if (totalNodes % 2 == 0){
            sum += select(totalNodes / 2);
        }else{
            sum += select((totalNodes + 1) / 2);
        }
    }

    printf("%i\n", sum % 10000);

    fclose(file);

    struct timespec end;
    timespec_get(&end, TIME_UTC);
    double timeSpent = (end.tv_sec - begin.tv_sec) * 1000 + (end.tv_nsec - begin.tv_nsec) / 1000000.0;
    printf("The time of execution of above program is : %.3fms\n", timeSpent);
    return 0;
}