#include <iostream>

using namespace std;

int main() {
    cin.tie(nullptr);
    cout.tie(nullptr);
    cin.sync_with_stdio(false);
    cout.sync_with_stdio(false);
    int a, b, n;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> a >> b;
        cout << a + b << "\n";
    }

    return 0;
}
