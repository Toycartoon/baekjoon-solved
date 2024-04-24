#include <iostream>
#include <cstdint>
#include <vector>


using namespace std;

int main(){
    int n, v;
    cin >> n;

    vector<int32_t> a(n+1, 0);
    for(int i = 0; i < n; i++)
        cin >> a[i];

    cin >> v;

    int ans = 0;
    for(int i = 0; i < n; i++) {
        if(a[i] == v) {
            ans++;
        }
    }

    cout << ans;
    return 0;
}
