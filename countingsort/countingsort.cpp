#include <iostream>
#include <fstream>

#include "./../helpers/helpers.h"

using namespace std;


const int MAX = 10;


void func();
int *counting_sort(int A[], int n, int high);

int main(int argc, char const *argv[])
{
    // func();
    int *arr = generate_inverted_array(MAX);
    print_array(arr, MAX);
    int *sorted = counting_sort(arr, MAX, 10);
    print_array(sorted, MAX);
    return 0;
}


int *counting_sort(int A[], int n, int high)
{
    // Arrays creating
    int *C = new int[ high + 1 ];
    int *B = new int[ n ];

    // Initialize them
    initialize_array(C, high + 1);
    initialize_array(B, n);

    // Counting
    for (int i = 0; i < n; i++)
        C[ A[i] ] = C[ A[i] ] + 1;
    
    for (int i = 1; i < high + 1; i++)
        C[i] = C[i] + C[i - 1];
    
    // Sorting
    for (int i = n - 1; i != -1; i--)
    {
        B[ C[A[i]] - 1 ] = A[i];
        C[ A[i] ] = C[ A[i] ] - 1;
    }
    
    // Return array copy already sorted of original array
    return B;
}


void func()
{
    ofstream outdata;

    outdata.open( PATH + "/countingsort/data/worst_case.txt" );
    if( !outdata ) { // file couldn't be opened
        cerr << "Error: file could not be opened" << endl;
        exit(1);
    }

    int steps{};

    // Worst case
    for (int i = 1; i <= MAX; i++)
    {    
        int *arr = generate_sorted_array( i );
        // steps = quick_sort_steps(arr, 0, i - 1);
        outdata << i << ":" << steps << endl;
    }
    outdata.close();

    // Best case
    outdata.open( PATH + "/countingsort/data/best_case.txt" );
    for (int i = 1; i <= MAX; i++)
    {    
        int *arr = generate_random_array( i );
        // steps = quick_sort_steps(arr, 0, i - 1);
        outdata << i << ":" << steps << endl;
    }
    outdata.close();

    // Average case
    outdata.open( PATH + "/countingsort/data/average_case.txt" );
    for (int i = 1; i <= MAX; i++)
    {
        int *arr = generate_random_array( i );
        // steps = quick_sort_steps(arr, 0, i - 1);
        outdata << i << ":" << steps << endl;
    }
    outdata.close();
}