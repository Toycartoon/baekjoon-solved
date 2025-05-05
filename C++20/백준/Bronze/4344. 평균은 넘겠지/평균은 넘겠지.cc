#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main() {
    int c, n;

    cin >> c;
    for (int i = 0; i < c; i++) {
        cin >> n;

        int a[1000];
        int sum = 0;
        for (int x = 0; x < n; x++) {
            cin >> a[x];
            sum = sum + a[x];
        }

        float avg = (float)sum / n;
        int temp = 0;
        
        for (int x = 0; x < n; x++) {
            if (a[x] > avg)
                temp++;
        }

        cout.precision(3);
        cout << fixed << (float)temp * 100 / n << "%" << endl;
    }

    return 0;
}
