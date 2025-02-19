#include <iostream>
#include <numeric>

using namespace std;


int main() {
	int a, b;
	int t;

	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> a >> b;
		cout << lcm(a, b) << endl;
	}

	return 0;
}