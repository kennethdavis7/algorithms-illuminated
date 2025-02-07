#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

typedef struct node {
    int number;
    struct node* next;
} node;

const unsigned int N = 2000003;

node* table[N];

int hash(int number) {
    return (number % N + N) % N; 
}

node* find(int number) {
    int index = hash(number);
    for (node* trav = table[index]; trav != NULL; trav = trav->next) {
        if (trav->number == number) {
            return trav;
        }
    }
    return NULL;
}

void insert(int number) {
    int index = hash(number);
    node* tmp = malloc(sizeof(node));
    tmp->number = number;
    tmp->next = table[index];
    table[index] = tmp;
}

int main(void) {
    struct timespec begin;
    timespec_get(&begin, TIME_UTC);
    FILE* file = fopen("problem12_4.txt", "r");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    int buffer;
    while (fscanf(file, "%i", &buffer) == 1) {
        if (find(buffer) == NULL) {
            insert(buffer);
        }
    }
    fclose(file);

    int interval[2] = {-10000, 10000};
    int total_targets = 0;

    for (int t = interval[0]; t <= interval[1]; t++) {
        bool isTarget = false;
        for (int i = 0; i < N; i++) {
            for (node* trav = table[i]; trav != NULL; trav = trav->next) {
                int complement = t - trav->number;
                node* targetPointer = find(complement);
                if (targetPointer != NULL && targetPointer != trav) { 
                    isTarget = true;
                    break;
                }
            }
            if (isTarget) break;
        }
        if (isTarget) total_targets++;
    }

    printf("%i\n", total_targets);
    struct timespec end;
    timespec_get(&end, TIME_UTC);
    double timeSpent = (end.tv_sec - begin.tv_sec) * 1000 + (end.tv_nsec - begin.tv_nsec) / 1000000.0;
    printf("The time of execution of above program is : %.3fms\n", timeSpent);
    return 0;
}
