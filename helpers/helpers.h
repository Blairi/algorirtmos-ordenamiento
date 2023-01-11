#include <string>

#ifndef HELPERS_H
#define HELPERS_H

extern const std::string PATH;

void print_array(int arr[], int size);
int *generate_random_array(int size);
int *generate_inverted_array(int size);
int *generate_sorted_array(int size);

#endif