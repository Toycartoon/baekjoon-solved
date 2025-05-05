#include <iostream>

using namespace std;

int main() {
    int n;
    int ans = 1;

    cin >> n;
    int a = n / 10;
    int b = n % 10;
    int x = (b * 10) + (a + b) % 10;

    while (x != n) {
        a = x / 10;
        b = x % 10;

        x = (b * 10) + (a + b) % 10;
        ans++;
    }

    cout << ans << endl;

    return 0;
}
