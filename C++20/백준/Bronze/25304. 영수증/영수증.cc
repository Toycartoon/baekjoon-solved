#include <iostream>

using namespace std;

int main() {
	unsigned long long int x;
	int n;
	
	unsigned int a;
	int b;

	unsigned long long int ans = 0;

	cin >> x;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> a >> b;
		ans = ans + (a * b);
	}

	if (ans == x) {
		cout << "Yes";
	}
	else {
		cout << "No";
	}

	return 0;
}