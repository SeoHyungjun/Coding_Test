#include <stdio.h>

#define size 9

void merge(int *arr, int left, int mid, int right) {
    int i;
    int left_count = left, right_count = mid+1, tmp_count = left;
    int tmp[size] ={0};

    // left_count와 right_count를 인덱스로 배열에서 인덱스에 맞는 값을 비교하여 tmp에 추가
    //만약 left_count 또는 right_count가 먼저 끝(가장 오른쪽)에 도달했을 경우에는
    //한쪽의 데이터는 끝까지 tmp에 저장이 되지 않음(최소 가장 뒤 1개는 저장 x)
    while(left_count <= mid && right_count <= right) {
        if (arr[left_count] < arr[right_count])
            tmp[tmp_count++] = arr[left_count++];
        else 
            tmp[tmp_count++] = arr[right_count++];

        printf("\t");
        for (i=0; i<size; i++) {
            printf("%d ", tmp[i]);
        } printf("\n");
    }
    //앞의 while문이 끝나면 left 또는 right 배열의 최소 1개의 데이터가 tmp에 저장되지 않았으므로

    //오른쪽이 먼저 끝나서 왼쪽에 데이터가 모두 사용되지 않았을 경우
    while( left_count <= mid ) tmp[tmp_count++] = arr[left_count++];
    //왼쪽이 먼저 끝나서 오른쪽에 데이터가 모두 사용되지 않았을 경우
    while( right_count <= right ) tmp[tmp_count++] = arr[right_count++];
    
    printf("\t");
    for (i=0; i<size; i++) {
        printf("%d ", tmp[i]);
    } printf("\n");

    //tmp에는 left부터 right까지의 데이터가 정렬되어 저장되어있으므로 arr에 복사
    for (tmp_count = left; tmp_count <= right; tmp_count++) {
        arr[tmp_count] = tmp[tmp_count];
    }

    for (i=0; i<size; i++) {
        printf("%d ", arr[i]);
    } printf("\n");
    
}

void merge_sort(int *arr, int left, int right) {
    int mid = (left + right)/2;

    if(left < right) {
        printf("%d ~ %d merge sort\n", left, mid);
        merge_sort(arr, left, mid);
        printf("%d ~ %d merge sort\n", mid+1, right);
        merge_sort(arr, mid+1, right);
        printf("merge\n");
        merge(arr, left, mid, right);
    }
}

int main() {
    int arr[size] = {9, 8, 7, 6, 5, 4, 3, 2, 1};
    int i;

    for (i=0; i<size; i++) {
        printf("%d ", arr[i]);
    } printf("\n");

    merge_sort(arr, 0, size-1);

    for (i=0; i<size; i++) {
        printf("%d ", arr[i]);
    } printf("\n");

    return 0;
}