#include <iostream>
#include <fstream>

#include "./../helpers.cpp"

using namespace std;

const int MAX = 1000;

void func();
void merge_sort(int arr[], int l, int h);
void merge(int arr[], int l, int h, int r);
int merge_sort_steps(int arr[], int l, int h);
int merge_steps(int arr[], int l, int h, int r);

int main(int argc, char const *argv[])
{
    func();
    return 0;
}


void merge_sort(int arr[], int l, int h)
{
    if (l < h){
        int m = l + (h - l) / 2;
        merge_sort(arr, l, m);
        merge_sort(arr, m + 1, h);
        merge(arr, l, m, h);
    }
}


void merge(int arr[], int l, int m, int r)
{
    // Creating aux arrays
    int left_len = m - l + 1;
    int right_len = r - m;
    int *left = new int[left_len], 
        *right = new int[right_len];

    // Copying elements in aux arrays
    for (int i = 0; i < left_len; i++)
        left[i] = arr[l + i];
    for (int j = 0; j < right_len; j++)
        right[j] = arr[m + 1 + j];

    // Initial index of arrays
    int left_i = 0, right_i = 0;
    int merged_i = l;

    // Merge the aux arrays with the original array
    while (left_i < left_len && right_i < right_len)
    {
        if (left[left_i] <= right[right_i])
        {
            arr[merged_i] = left[left_i];
            left_i ++;
        }
        else
        {
            arr[merged_i] = right[right_i];
            right_i ++;
        }
        merged_i ++;
    }

    // Copying the remaining elements in aux arrays
    // if there are any
    while (left_i < left_len) {
        arr[merged_i] = left[left_i];
        left_i ++;
        merged_i ++;
    }

    while (right_i < right_len) {
        arr[merged_i] = right[right_i];
        right_i ++;
        merged_i ++;
    }

    delete[] left;
    delete[] right;
}


int merge_sort_steps(int arr[], int l, int h)
{
    int steps = 0;
    if (l < h){
        steps ++;
        int m = l + (h - l) / 2;
        steps += merge_sort_steps(arr, l, m);
        steps += merge_sort_steps(arr, m + 1, h);
        steps += merge_steps(arr, l, m, h);
    }
    return steps;
}


int merge_steps(int arr[], int l, int m, int r)
{
    int steps = 0;

    // Creating aux arrays
    int left_len = m - l + 1;
    int right_len = r - m;
    int *left = new int[left_len], 
        *right = new int[right_len];

    // Copying elements in aux arrays
    for (int i = 0; i < left_len; i++)
        left[i] = arr[l + i];
    for (int j = 0; j < right_len; j++)
        right[j] = arr[m + 1 + j];

    // Initial index of arrays
    int left_i = 0, right_i = 0;
    int merged_i = l;

    // Merge the aux arrays with the original array
    while (left_i < left_len && right_i < right_len)
    {
        if (left[left_i] <= right[right_i])
        {
            arr[merged_i] = left[left_i];
            left_i ++;
        }
        else
        {
            arr[merged_i] = right[right_i];
            right_i ++;
        }
        merged_i ++;
        steps ++;
    }

    // Copying the remaining elements in aux arrays
    // if there are any
    while (left_i < left_len) {
        arr[merged_i] = left[left_i];
        left_i ++;
        merged_i ++;
        steps ++;
    }

    while (right_i < right_len) {
        arr[merged_i] = right[right_i];
        right_i ++;
        merged_i ++;
        steps ++;
    }

    delete[] left;
    delete[] right;

    return steps;
}


void func()
{
    ofstream outdata;

    outdata.open( PATH + "/mergesort/data/worst_case.txt" );
    if( !outdata ) { // file couldn't be opened
        cerr << "Error: file could not be opened" << endl;
        exit(1);
    }

    int steps{};

    for (int i = 1; i <= MAX; i++)
    {    
        int *arr = generate_inverted_array( i );
        steps = merge_sort_steps(arr, 0, i - 1);
        outdata << i << ":" << steps << endl;
    }
    outdata.close();

    outdata.open( PATH + "/mergesort/data/best_case.txt" );
    for (int i = 1; i <= MAX; i++)
    {    
        int *arr = generate_sorted_array( i );
        steps = merge_sort_steps(arr, 0, i - 1);
        outdata << i << ":" << steps << endl;
    }
    outdata.close();

    outdata.open( PATH + "/mergesort/data/average_case.txt" );
    for (int i = 1; i <= MAX; i++)
    {    
        int *arr = generate_random_array( i );
        steps = merge_sort_steps(arr, 0, i - 1);
        outdata << i << ":" << steps << endl;
    }
    outdata.close();
}