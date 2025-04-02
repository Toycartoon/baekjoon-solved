#include <iostream>

using namespace std;

int main() {
	int h, m;

	cin >> h >> m;
	m = m - 45;

	if (m < 0) {
		--h;
		m = m + 60;
	}
	if (h < 0)
		h = h + 24;

	cout << h << " " << m;

	return 0;
}