#include <iostream>
#include <fstream>

#include "./../helpers/helpers.h"

using namespace std;

const int MAX = 1000;

void bubble_sort(int arr[], int n);
int bubble_sort_steps(int arr[], int n);


int main(int argc, char const *argv[])
{
    ofstream outdata;

    outdata.open( PATH + "/bubblesort/data/worst_case.txt" );
    if( !outdata ) { // file couldn't be opened
        cerr << "Error: file could not be opened" << endl;
        exit(1);
    }

    int steps{};

    for (int i = 1; i <= MAX; i++)
    {    
        int *arr = generate_inverted_array( i );
        steps = bubble_sort_steps( arr, i );
        outdata << i << ":" << steps << endl;
    }
    outdata.close();

    outdata.open( PATH + "/bubblesort/data/best_case.txt" );
    for (int i = 1; i <= MAX; i++)
    {    
        int *arr = generate_sorted_array( i );
        steps = bubble_sort_steps( arr, i );
        outdata << i << ":" << steps << endl;
    }
    outdata.close();

    outdata.open( PATH + "/bubblesort/data/average_case.txt" );
    for (int i = 1; i <= MAX; i++)
    {    
        int *arr = generate_random_array( i );
        steps = bubble_sort_steps( arr, i );
        outdata << i << ":" << steps << endl;
    }
    outdata.close();

    return 0;
}


void bubble_sort(int arr[], int n)
{
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - i - 1; j++)
            if (arr[i] > arr[j + 1]) swap(arr[j], arr[j + 1]);
}


int bubble_sort_steps(int arr[], int n)
{
    int steps {0};
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            steps++;
            if (arr[j] > arr[j + 1])
            {
                swap(arr[j], arr[j + 1]);
                steps++;
            }
        }
    }
    return steps;
}