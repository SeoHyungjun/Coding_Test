#include <bits/stdc++.h>
typedef long long ll;
#define REP(a,b) for(int i=a;i<=b;++i)
const ll inf = LONG_MAX;
#define N 500500
ll n,k, arr[N], fen[N], cnt[N];

const ll mod = 1e9+7;

void upt(int k, ll x) {
    while (k<=N) {
        fen[k] += x;
        k+=k&-k;
    }
}

ll qry(int k) {
    ll ret=0;
    while (k>=1) {
        ret += fen[k];
        k-=k&-k;
    }
    return ret;
}

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int T; 

    std::cin>>T;
    for (int I=1; I<=T; ++I) {
        std::cin >> n >> k;
        ll ans = 0;
        REP(1,n) {
            std::cin >> arr[i];
            ans += k*qry(N-arr[i]-1);
            ans %= mod;
            upt(N-arr[i], 1);
        }
        REP(1,n) {
            ans += ((k-1)*k/2)%mod * qry(N-arr[i]-1)%mod;
            ans %= mod;
        }
        std::cout << "#" << I << " " << ans << "\n";
        memset(fen, 0, sizeof fen);
    }
    return 0;
}