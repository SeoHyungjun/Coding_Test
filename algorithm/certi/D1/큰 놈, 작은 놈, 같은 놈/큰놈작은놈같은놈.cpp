#include<iostream>

int main(int argc, char** argv)
{
	int test_case;
	int T;
	
	std::cin>>T;
	for(test_case = 1; test_case <= T; ++test_case) {
        int a, b;
        
        std::cin >> a >> b;
        std::cout << "#" << test_case << " ";
        if (a < b) std::cout << "<" << '\n';
        else if (a == b) std::cout << "=" << '\n';
        else std::cout << ">" << '\n';
	}
	return 0;
}