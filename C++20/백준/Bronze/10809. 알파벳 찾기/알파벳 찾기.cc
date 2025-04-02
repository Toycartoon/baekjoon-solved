#include <iostream>
#include <string>

using namespace std;

int main() {
	int a[26];
	string s;

	for (int i = 0; i < 26; i++) {
		a[i] = -1;
	}

	cin >> s;
	for (int i = 0; i < s.length(); i++) {
		char x = s[i];

		if (a[int(x) - 97] == -1) {
			a[int(x) - 97] = i;
		}
	}

	for (int i = 0; i < 26; i++) {
		cout << a[i] << ' ';
	}


	return 0;
}