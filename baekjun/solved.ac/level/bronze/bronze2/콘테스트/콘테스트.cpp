#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);
    
    int W[10], K[10];
    for (auto &it : W) cin >> it;
    for (auto &it : K) cin >> it;

    sort(W, W+10);
    sort(K, K+10);

    cout << W[9] + W[8] + W[7] << " " << K[9] + K[8] + K[7];
    
    return 0;
}