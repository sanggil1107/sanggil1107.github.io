---
layout: post
title: "[알고리즘] 퀵정렬"
category: [알고리즘]
---
<br>

`퀵정렬`에 대해 알아보자
<!-- more -->
<hr>


```python
def merge(arr, low, high):
    temp = []
    mid = (low + high) // 2
    i, j = low, mid + 1

    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= high:
        temp.append(arr[j])
        j += 1

    for k in range(low, high + 1):
        arr[k] = temp[k - low]

    return arr


def merge_sort(arr, low, high):
    if (low >= high):
        return  # base case

    mid = (low + high) // 2

    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)

    sorted_array = merge(arr, low, high)

    return sorted_array
```
```java

private void solve() {
    int[] array = { 230, 10, 60, 550, 40, 220, 20 };
 
    mergeSort(array, 0, array.length - 1);
 
    for (int v : array) {
        System.out.println(v);
    }
}
 
public static void mergeSort(int[] array, int left, int right) {
    if (left < right) {
        int mid = (left + right) / 2;
 
        mergeSort(array, left, mid);
        mergeSort(array, mid + 1, right);
        merge(array, left, mid, right);
    }
}
 
public static void merge(int[] array, int left, int mid, int right) {
    int[] L = Arrays.copyOfRange(array, left, mid + 1);
    int[] R = Arrays.copyOfRange(array, mid + 1, right + 1);
 
    int i = 0, j = 0, k = left;
    int ll = L.length, rl = R.length;
 
    while (i < ll && j < rl) {
        if (L[i] <= R[j]) {
            array[k] = L[i++];
        } else {
            array[k] = R[j++];
        }
        k++;
    }
 
    while (i < ll) {
        array[k++] = L[i++];
    }
 
    while (j < rl) {
        array[k++] = R[j++];
    }
}
```