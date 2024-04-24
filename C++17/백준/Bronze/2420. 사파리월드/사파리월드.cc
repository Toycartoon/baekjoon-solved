#include <iostream>

using namespace std;

int main() {
    long long int n, m;

    cin >> n >> m;
    if (n > m)
        cout << n - m;
    else
        cout << m - n;

    return 0;
}
