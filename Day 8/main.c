// NOT FINISHED
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <unistd.h>

struct Node {
    char value[3];
    struct Node* right;
    struct Node* left;
};

typedef struct Node node;

bool is_zzz(char* value) {
    return strcmp(value, "ZZZ") == 0;
}

int to_zzz(node* begin, char* str) {
    int count = 0;
    int i = 0;
    node* current = begin;
    while (!(is_zzz(current->value))) {
        if (str[i] == '\0') i = -1;
        if (str[i] == 'r') {
            current = current->right;
            count++;
        }
        if (str[i] == 'l') {
            current = current->left;
            count++;
        }
        i++;
    }
    return count;
}

/*
test.txt:
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
*/

void parse_input(node* begin, char* instructions) {

}

int main() {
    node* begin = malloc(sizeof(node));
    char* instructions = malloc(sizeof(char) * 100);
    parse_input(begin);
    printf("%d\n", to_zzz(begin, "RL"));
    return 0;
}