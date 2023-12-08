#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <unistd.h>

struct Node {
    char* value;
    struct Node* right;
    struct Node* left
};

typedef struct Node node;

bool is_zzz(char* str) {
    if (strlen(str) != 3) return false;
    if (str[0] != 'z') return false;
    if (str[1] != 'z') return false;
    if (str[2] != 'z') return false;
    return true;
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

void parse_input(node* begin) {
    FILE* file = fopen("test.txt", "r");
    char* line = NULL;
    size_t len = 0;
    ssize_t read;
    node* current = begin;
    while ((read = getline(&line, &len, file)) != -1) {
        char* token = strtok(line, " =");
        char* value = strtok(NULL, " =");
        current->value = token;
        if (value != NULL) {
            if (value[0] == '(') {
                node* left = malloc(sizeof(node));
                node* right = malloc(sizeof(node));
                current->left = left;
                current->right = right;
                parse_input(left);
                parse_input(right);
            }
        }
        current = current->right;
    }
    fclose(file);
}

int main() {
    node* begin = malloc(sizeof(node));
    parse_input(begin);
    printf("%d\n", to_zzz(begin, "RL"));
    return 0;
}