#include <iostream>
#include <string>
#include <set>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N;
    std::string name, enter;
    std::set<std::string> in_company;

    std::cin >> N;
    while (N--) {
        std::cin >> name >> enter;
        if (enter == "enter") in_company.emplace(name);
        else in_company.erase(name);
    }

    for (auto it = in_company.rbegin(); it != in_company.rend(); ++it) std::cout << *it << "\n";

    return 0;
}