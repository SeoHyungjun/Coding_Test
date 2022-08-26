#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<pair<int, int> > v(8);
    for (int i = 0; i < 8; i++) {
        cin >> v[i].first;
        v[i].second = i+1;
    }

    sort(v.begin(), v.end(), greater<pair<int, int> >());

    int sum = 0;
    vector<int> idx;
    for (int i = 0; i < 5; i++) {
        sum += v[i].first;
        idx.push_back(v[i].second);
    }

    cout << sum << endl;

    sort(idx.begin(), idx.end());
    for(int i = 0; i < idx.size(); i++)
        cout << idx[i] << " ";

    return 0;
}