#include <iostream>
#include <cstdint>
#include <vector>

using namespace std;

int main() {
    int n, x;
    cin >> n >> x;

    vector<int32_t> a(n+1, 0);
    for(int i = 0; i < n; i++)
        cin >> a[i];

    for(int i = 0; i < n; i++) {
        if(a[i] < x)
            cout << a[i] << " ";
    }

    return 0;
}
