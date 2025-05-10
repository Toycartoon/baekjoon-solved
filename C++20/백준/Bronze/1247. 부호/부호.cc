#include <iostream>

using namespace std;

int main() {
    for (int i=0; i<3; i++) {
        int n;
        __int128 s = 0;

        cin >> n;
        for (int x=0; x<n; x++) {
            long long int a;
            cin >> a;
            s = s + a;
        }

        if (s > 0) {
            cout << "+" << endl;
        }
        else if (s < 0) {
            cout << "-" << endl;
        }
        else {
            cout << "0" << endl;
        }
    }
}