#include <iostream>

using namespace std;

int main() {
	int n;

	cin >> n;
	int* a = new int[n];

	int mn = 1000001;
	int mx = -1000001;
	
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}

	for (int i = 0; i < n; i++) {
		if (a[i] > mx)
			mx = a[i];
		if (a[i] < mn)
			mn = a[i];
	}

	delete[] a;
	
	cout << mn << " " << mx;
	return 0;
}