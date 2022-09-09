#include <iostream>
#include <string>

std::string str;
int alpha[26];
long long f[21];

void factorial() {
    f[0] = 1;
    for (int i = 1; i < 21; ++i) f[i] = f[i-1] * i;
}

long long solve(int idx) {
    if (idx == str.length() - 1) return 0;
    long long result = 0;

    for (int i = 25; i >= 0; --i) {
        if (alpha[i] == 0 || 'A' + i > str[idx]) continue;
        --alpha[i];
        if ('A' + i == str[idx]) {
            result += solve(idx+1);
        }
        else {
            int cnt = 0; 
            long long div = 1;
            for (int j = 0; j < 26; ++j) {
                if (alpha[j] == 0) continue;
                cnt += alpha[j];
                div *= f[alpha[j]];
            }
            result += f[cnt] / div;
        }
        ++alpha[i];
    }
    return result;
}

int main(int argc, char** argv) {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
	int test_case, T;

    factorial();
	std::cin >> T;
	for(test_case = 1; test_case <= T; ++test_case) {
        std::cin >> str;

        for (int i = 0; i < 26; ++i) alpha[i] = 0;
        for (int i = 0; i < str.length(); ++i) ++alpha[str[i] - 'A'];

        std::cout << "#" << test_case << ' ' << solve(0) << '\n';
	}
	return 0;
}