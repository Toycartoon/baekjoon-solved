#include <iostream>

using namespace std;

int main() {
    int t, n;

    cin >> t;
    for(int i = 0; i < t; i++) {
        cin >> n;
        int ans = 0;
        int x;

        for(int j = 0; j < n; j++) {
            cin >> x;
            ans += x;
        }

        cout << ans << endl;
    }


    return 0;
}
