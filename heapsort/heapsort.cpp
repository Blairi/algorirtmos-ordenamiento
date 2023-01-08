#include <iostream>
#include <fstream>

#include "./../helpers.cpp"

using namespace std;

const int MAX = 1000;

int left(int i);
int right(int i);
void heapify(int arr[], int n, int i);
void heap_sort(int arr[], int n);
int heapify_steps(int arr[], int n, int i);
int heap_sort_steps(int arr[], int n);

int main(int argc, char const *argv[])
{
    int *arr = generate_random_array(MAX);
    // print_array(arr, MAX);
    int steps = heap_sort_steps(arr, MAX);
    // print_array(arr, MAX);
    cout << "Steps: " << steps << endl;
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


int heapify_steps(int arr[], int n, int i)
{
    int steps = 0;
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
        steps += heapify_steps(arr, n, largest);
    }

    steps ++;

    return steps;
}


int heap_sort_steps(int arr[], int n)
{
    int steps = 0;
    // Tree building
    for (int i = n / 2 - 1; i >= 0; i--)
        steps += heapify_steps(arr, n, i);
 
    for (int i = n - 1; i > 0; i--) {
        // Move as current root the first element
        swap(arr[0], arr[i]);
        // Call to heapify to reduced heap
        steps += heapify_steps(arr, i, 0);
    }
    return steps;
}

