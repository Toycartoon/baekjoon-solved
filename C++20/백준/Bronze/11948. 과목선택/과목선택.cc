#include <iostream>
#include <algorithm>

using namespace std;

bool desc(int a, int b) {
    return a > b;
}

int main() {
    int a[4];
    int b[3];

    for(int i = 0; i < 4; i++) {
        cin >> a[i];
    }
    for(int i = 0; i < 2; i++) {
        cin >> b[i];
    }

    sort(a, a+4, desc);
    sort(b, b+2, desc);

    int ans = 0;

    for(int i = 0; i < 3; i++)
        ans += a[i];
    ans += b[0];

    cout << ans << endl;
}
