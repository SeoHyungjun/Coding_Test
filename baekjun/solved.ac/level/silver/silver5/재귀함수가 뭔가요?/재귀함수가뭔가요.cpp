#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int N;

void print_underbar(int n) {for (int i = 0; i < n; ++i) std::cout << "____";}   

void dfs(int depth) {
    print_underbar(depth);
    std::cout << "\"재귀함수가 뭔가요?\"\n";
    print_underbar(depth);
    if (depth == N) std::cout << "\"재귀함수는 자기 자신을 호출하는 함수라네\"\n";
    else {
        std::cout << "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n";
        print_underbar(depth); 
        std::cout << "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n";
        print_underbar(depth); 
        std::cout << "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"\n";
        dfs(depth + 1);
    }
    print_underbar(depth); std::cout << "라고 답변하였지.\n";
}

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);

    std::cin >> N;
    std::cout << "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.\n";
    dfs(0);

    return 0;
}