#include <iostream>

using namespace std;


int oper(int a, int b) {
	return (a + b) * (a - b);
}

int main() {
	int a, b;

	cin >> a >> b;
	cout << oper(a, b) << endl;

	return 0;
}