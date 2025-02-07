#include <stdio.h>
#include <math.h>
#include <stdlib.h>

void merge_sort(int* arr, int n);

int main(void){
    int n = 12;
    int arr[12] = {5,4,1,8,7,2,6,9,9,10,12,9};

    merge_sort(arr, n);
    
    for(int i = 0; i < n; i++){
        printf("%i ", arr[i]);
    }
}

void merge_sort(int* arr, int n){
    if(n == 1){
        return;
    }

    int first_length = ceil(n/2.0);
    int second_length = n - first_length;

    int* first_sub_arr = malloc(first_length * sizeof(int));
    int* second_sub_arr = malloc(second_length * sizeof(int));

    for(int i = 0; i < first_length; i++){
        first_sub_arr[i] = arr[i];
    }

    for(int j = 0; j < second_length; j++){
        second_sub_arr[j] = arr[first_length + j];
    }

    merge_sort(first_sub_arr, first_length);
    merge_sort(second_sub_arr, second_length);

    int w = 0, z = 0;
    for (int v = 0; v < n; v++) {
        if (w < first_length && z < second_length) {
            if (first_sub_arr[w] <= second_sub_arr[z]) {
                arr[v] = first_sub_arr[w++];
            } else {
                arr[v] = second_sub_arr[z++];
            }
        } else if (w < first_length) {
            arr[v] = first_sub_arr[w++];
        } else {
            arr[v] = second_sub_arr[z++];
        }
    }

    free(first_sub_arr);
    free(second_sub_arr);
}

// For debugging
    // printf("%i\n", first_length);

    // for(int k = 0; k < first_length; k++){
    //     printf("%i ", first_sub_arr[k]);
    // }
    // printf("\n\n");

    // printf("%i\n", second_length);
    // for(int g = 0; g < second_length; g++){
    //     printf("%i ", second_sub_arr[g]);
    // }
    // printf("\n\n");
