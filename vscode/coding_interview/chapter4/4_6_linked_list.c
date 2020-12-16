#include <stdio.h>
#include <stdlib.h>

typedef struct ListNode{
    int data;
    struct ListNode *next;
}ListNode;


void Listdelete(ListNode **head, int position);
void ListInsert(ListNode **head, int data, int position);
int ListLength(ListNode *head);
void ListPrint(ListNode *head);

int main() {
    int menu;
    int data, position;
    ListNode *head;

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
                ListInsert(&head, data, position);
                break;
            case 4:
                printf("position : ");
                scanf("%d", &position);
                Listdelete(&head, position);
                break;
            case 5:
                return 0;
        }
    }
}

void Listdelete(ListNode **head, int position) {
    int count = 1;
    ListNode *before, *cur = *head;
    
    //리스트가 비어있을 경우 그냥 종료
    if (*head == NULL) {
        printf("List is Empty\n");
        return;
    }

    //맨 앞을 지우는 경우
    if (position == 1) {
        *head = cur->next;
        free(cur);
        return;
    }
    
    //중간 또는 마지막을 지우는 경우
    else {
        while( (count < position) && (cur != NULL)) {
            count++;
            before = cur;
            cur = cur->next;
        }

        //내가 지정한 위치(position) 전까지 갔는데 position이 없을 경우
        if(cur == NULL) printf("position is not exist.\n");
        else {
            before->next = cur->next;
            free(cur);
        }
    }
}

void ListInsert(ListNode **head, int data, int position) {
    int count = 1;
    ListNode *newNode, *before, *cur;
    newNode = (ListNode*)malloc(sizeof(ListNode));
    
    if (ListLength(*head) < position-1 ) {
        printf("%d ", ListLength(*head));
        printf("%d\n", position-1);
        printf("out of range\n");
        return;
    }

    if(!newNode) {
        printf("Memory Error\n");
        return;
    }
    newNode->data = data;
    cur = *head;
    //맨 앞에 삽입해서  head가 바뀌는 경우
    if (position == 1) {
        newNode->next = cur;
        *head = newNode;
    }
    //중간 또는 맨뒤에 삽입될 경우
    else {
        while( (count < position) && (cur != NULL) ){
            //before->next가 삽입하려는 노드를 가리켜야하므로 이전의 노드를 기억해야함
            before = cur;
            cur = cur->next;
            count++;
        }
        before->next = newNode;
        newNode->next = cur;
    }
}

int ListLength(ListNode *head) {
    ListNode *cur = head;
    int count = 0;

    while(cur != NULL) {
        count++;
        cur = cur->next;
    }
    return count;
}

void ListPrint(ListNode *head) {
    ListNode * cur = head;
    int count = 0;

    while(cur != NULL) {
        printf("%d -> ", cur->data);
        count++;
        cur = cur->next;
    }
    printf("NULL\nListLength : %d\n", count);
}