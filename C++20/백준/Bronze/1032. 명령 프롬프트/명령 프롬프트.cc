#include <iostream>
#include <string>

using namespace std;

int main() {
    int n;
    string s[50];

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> s[i];
    }
    
    char v;
    for (int x = 0; x < s[0].length(); x++) {
        v = s[0][x];
        for (int i = 0; i < n; i++) {
            if (s[i][x] != v) {
                v = '?';
                break;
            }
        }
        cout << v;
    }

    return 0;
}
