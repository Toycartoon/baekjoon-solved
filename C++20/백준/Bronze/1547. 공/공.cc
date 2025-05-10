#include <iostream>

using namespace std;

int main() {
    bool a[3] = {true, false, false};
    int m;
    int x, y;

    cin >> m;
    for (int i = 0; i < m; i++) {
        cin >> x >> y;
        bool temp = a[y-1];

        a[y-1] = a[x-1];
        a[x-1] = temp;
    }

    for (int i = 0; i < 3; i++) {
        if (a[i]) {
            cout << i+1 << endl;
            break;
        }
    }

    return 0;
}