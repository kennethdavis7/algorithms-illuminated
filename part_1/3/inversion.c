#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int sort_count_inv(int* arr, int n);

int main(void){
    int arr[10] = {54044,14108,79294,29649,25260,60660,2995, 53777, 49689, 9083};
    int inversions = sort_count_inv(arr, 10);
    printf("%i\n", inversions);
}

int sort_count_inv(int* arr, int n){
    if (n == 0 || n == 1){
        return 0;
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

    int first_sub_arr_inv = sort_count_inv(first_sub_arr, first_length);
    int second_sub_arr_inv = sort_count_inv(second_sub_arr, second_length);

    int w = 0, z = 0, split_inv = 0;
    for (int v = 0; v < n; v++) {
        if (w < first_length && z < second_length) {
            if (first_sub_arr[w] <= second_sub_arr[z]) {
                arr[v] = first_sub_arr[w++];
            } else {
                arr[v] = second_sub_arr[z++];
                split_inv += first_length - w;
            }
        } else if (w < first_length) {
            arr[v] = first_sub_arr[w++];
        } else {
            arr[v] = second_sub_arr[z++];
        }
    }

    free(first_sub_arr);
    free(second_sub_arr);

    return first_sub_arr_inv + second_sub_arr_inv + split_inv;
}