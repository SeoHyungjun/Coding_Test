#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

using ll = long long;

ll gcd(ll a, ll b) {
    ll tmp;
    if (a < b) {tmp = a;a = b;b = tmp;}

    while (b) {
        tmp = a%b;
        a = b;
        b = tmp;
    }
    return a;
}

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    ll n, a, b;

    std::cin >> n;
    while (n--) {
        std::cin >> a >> b;
        std::cout << a * b / gcd(a, b) << '\n';
    }

    return 0;
}