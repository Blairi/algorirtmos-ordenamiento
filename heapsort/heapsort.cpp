#include <iostream>
#include <fstream>

#include "./../helpers.cpp"

using namespace std;

const int MAX = 10;

int left(int i);
int right(int i);
void heapify(int arr[], int n, int i);
void heap_sort(int arr[], int n);

int main(int argc, char const *argv[])
{
    int *arr = generate_random_array(MAX);
    print_array(arr, MAX);
    heap_sort(arr, MAX);
    print_array(arr, MAX);
    return 0;
}


int left(int i){ return 2 * i + 1; }


int right(int i){ return 2 * i + 2; }


void heapify(int arr[], int n, int i)
{
    // Root of tree
    int largest = i;
    // Indexes of children
    int L = left(i);
    int R = right(i);

    // Swapping the root
    if (L < n && arr[L] > arr[largest])
        largest = L;
    
    if (R < n && arr[R] > arr[largest])
        largest = R;

    // If the largest changed, swap and make a recursive call for the sub-tree
    if (largest != i)
    {
        swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}


void heap_sort(int arr[], int n)
{
    // Tree building
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);
 
    for (int i = n - 1; i > 0; i--) {
        // Move as current root the first element
        swap(arr[0], arr[i]);
        // Call to heapify to reduced heap
        heapify(arr, i, 0);
    }
}