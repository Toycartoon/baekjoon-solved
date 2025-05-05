#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    int n;
    int a[1000];

    cin >> n;
    
    int mx = 0;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        mx = max(mx, a[i]);
    }

    double sum = 0.0;
    for (int i = 0; i < n; i++) {
        sum = sum + ((double)a[i] / mx * 100);
    }

    cout.precision(3);
    cout << fixed << sum / n << endl;

    return 0;
}
