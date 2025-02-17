#include <iostream>

using namespace std;


long long int oper(long long int a, long long int b) {
	return (a + b) * (a - b);
}

int main() {
	long long int a, b;

	cin >> a >> b;
	cout << oper(a, b) << endl;

	return 0;
}