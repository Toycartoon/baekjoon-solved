#include <iostream>

using namespace std;

int main() {
    int n, x;
    long long int ans = 0;

    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> x;
            ans += x;
        }
    }

    cout << ans << endl;
    return 0;
}