#include <iostream>
#include <fstream>

#include "./../helpers/helpers.h"

using namespace std;


const int MAX = 1000;


void func();
int partition(int arr[], int low, int high);
void quick_sort(int arr[], int low, int high);
std::pair <int, int> partition_steps(int arr[], int low, int high);
int quick_sort_steps(int arr[], int low, int high);


int main(int argc, char const *argv[])
{
    func();
    return 0;
}


int partition(int arr[], int low, int high)
{
    int pivot = arr[high];
    int i = low - 1;
  
    for (int j = low; j <= high - 1; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }

    swap(arr[i + 1], arr[high]);

    return (i + 1);
}


void quick_sort(int arr[], int low, int high)
{
    if (low < high) {
        // Pivot
        int pi = partition(arr, low, high);
  
        // Recursive calls separated by the pivot
        quick_sort(arr, low, pi - 1);
        quick_sort(arr, pi + 1, high);
    }
}


std::pair <int, int> partition_steps(int arr[], int low, int high)
{
    int steps = 0;

    int pivot = arr[high];
    int i = low - 1;
  
    for (int j = low; j <= high - 1; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
            steps ++;
        }
        steps ++;
    }

    swap(arr[i + 1], arr[high]);

    // Returning the pivot and num. of steps as pair
    return { i + 1, steps };
}


int quick_sort_steps(int arr[], int low, int high)
{
    int steps = 0;

    if (low < high) {

        std::pair <int, int> result = partition_steps(arr, low, high);

        int pi = result.first;

        int step = result.second;
        steps += step;
  
        // Recursive calls separated by the pivot
        steps += quick_sort_steps(arr, low, pi - 1);
        steps += quick_sort_steps(arr, pi + 1, high);

    }

    steps ++;

    return steps;
}


void func()
{
    ofstream outdata;

    outdata.open( PATH + "/quicksort/data/worst_case.txt" );
    if( !outdata ) { // file couldn't be opened
        cerr << "Error: file could not be opened" << endl;
        exit(1);
    }

    int steps{};

    // Worst case
    for (int i = 1; i <= MAX; i++)
    {    
        int *arr = generate_sorted_array( i );
        steps = quick_sort_steps(arr, 0, i - 1);
        outdata << i << ":" << steps << endl;
    }
    outdata.close();

    // Best case
    outdata.open( PATH + "/quicksort/data/best_case.txt" );
    for (int i = 1; i <= MAX; i++)
    {    
        int *arr = generate_random_array( i );
        steps = quick_sort_steps(arr, 0, i - 1);
        outdata << i << ":" << steps << endl;
    }
    outdata.close();

    // Average case
    outdata.open( PATH + "/quicksort/data/average_case.txt" );
    for (int i = 1; i <= MAX; i++)
    {
        int *arr = generate_random_array( i );
        steps = quick_sort_steps(arr, 0, i - 1);
        outdata << i << ":" << steps << endl;
    }
    outdata.close();
}