#include <iostream>

using namespace std;

int main() {
    int ans=0;
    int a;

    for(int i; i < 5; i++) {
        cin >> a;
        ans += a;
    }
    cout << ans << endl;
    return 0;
}
