#include <iostream>
#include <string>

using namespace std;

int main() {
    int n;
    string s;

    cin >> n;
    cin >> s;

    int alpha[26];
    for (int i = 0; i < 26; i++) {
        alpha[i] = 0;
    }

    for (int i = 0; i < n; i++) {
        alpha[s[i] - 'A']++;
    }

    int ans = 100000;
    char w[5] = {'H', 'I', 'A', 'R', 'C'};

    for (int i = 0; i < 5; i++) {
        ans = min(ans, alpha[w[i]-'A']);
    }

    cout << ans << endl;
    return 0;
}