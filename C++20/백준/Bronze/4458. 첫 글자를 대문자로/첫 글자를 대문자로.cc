#include <iostream>
#include <string>

using namespace std;

int main() {
    int n;
    string s;

    cin >> n;
    cin.ignore();
    for (int a = 0; a < n; a++) {
        getline(cin, s);
        for (int i = 0; i < s.length(); i++) {
            if (i == 0 && 97 <= s[i] && (int)s[i] <= 122) {
                cout << (char)((int)s[i] - 32);
            }
            else
                cout << s[i];
        }
        cout << endl;
    }
    return 0;
}
