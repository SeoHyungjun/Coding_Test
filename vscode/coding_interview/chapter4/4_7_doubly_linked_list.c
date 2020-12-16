#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
    int data;
    struct Node *prev;
    struct Node *next;
}Node;

int ListLength(Node *head) {
    int count = 1;
    Node *cur = head;
    if( head == NULL) return 0;
    while (cur->next != NULL) {
        cur = cur->next;
        count++;
    }
    return count;
}

void insertNode(Node **head, int data, int position) {
    Node *NewNode = NULL, *cur = NULL;
    int count = 1;

    if (ListLength(*head) < position-1 ) {
        printf("out of range\n");
        return;
    }

    //새로운 노드 생성
    NewNode = (Node*)malloc(sizeof(Node));
    //노드 생성 실패 확인
    if(!NewNode) {
        printf("Memory Error\n");
        return;
    }
    NewNode->data = data;
    
    //리스트의 맨 앞에 삽입하는 경우
    if (position == 1) {
        if(*head != NULL)
            (*head)->prev = NewNode;
        NewNode->prev = NULL;
        NewNode->next = *head;
        (*head) = NewNode;
    }
    
    //리스트의 중간 또는 맨뒤에 삽입하는 경우
    else {
        cur = *head;
        while( (count < position-1) && (cur->next != NULL)) {
            cur = cur->next;
            count++;
        }
        if(count < position-1) {
            printf("position does not exist.\n");
            return;
        }
        NewNode->next = cur->next;
        NewNode->prev = cur;
        if (cur->next != NULL)
            cur->next->prev = NewNode;
        cur->next = NewNode;
        return;
    }
}

void deleteNode(Node **head, int position){
    Node *cur = *head, *temp;
    int count = 1;

    if (*head == NULL) {
        printf("List is empty.\n");
        return;
    }

    //맨앞 노드 삭제 할 경우
    if(position == 1) {
        *head=(*head)->next;
        //맨앞 노드 한개일 경우 NULL이 오면 실행이 안되므로
        if (*head != NULL) {
            (*head)->prev = NULL;
            free(cur);
            return;
        }
    }
    //중간 또는 맨뒤 노드 삭제 할 경우
    else {
        while ( (count < position) && (cur->next != NULL) ) {
            cur = cur->next;
            count++;
        }
        if (count != position) {
            printf("position does not exist.\n");
            return;
        }

        (cur->prev)->next = cur->next;
        if (cur->next != NULL ){
            (cur->next)->prev = cur->prev;
        }
        free(cur);
        return;
    }
}

void ListPrint(Node *head) {
    Node * cur = head;
    int count = 0;

    while(cur != NULL) {
        printf("%d -> ", cur->data);
        count++;
        cur = cur->next;
    }
    printf("NULL\nListLength : %d\n", count);
}

int main() {
    int menu;
    int data, position;
    Node *head;

    while(1) {
        printf("\n\nselect menu\n");
        printf("1. List Length Check\n");
        printf("2. List data check\n");
        printf("3. insert new node\n");
        printf("4. delete node\n");
        printf("5. exit\n");
        printf("select number of menu: ");
        scanf("%d", &menu);

        switch(menu) {
            case 1:
                printf("ListLength is %d\n", ListLength(head));
                break;
            case 2:
                ListPrint(head);
                break;
            case 3:
                printf("data : ");
                scanf("%d", &data);
                printf("position : ");
                scanf("%d", &position);
                insertNode(&head, data, position);
                break;
            case 4:
                printf("position : ");
                scanf("%d", &position);
                deleteNode(&head, position);
                break;
            case 5:
                return 0;
        }
    }
}
