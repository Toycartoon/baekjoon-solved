#include <iostream>
#include <cstdint>
#include <vector>


using namespace std;

int main(){
    int n = 0;

    vector<int32_t> a(31, 0);
    for(int i = 0; i < 28; i++) {
        cin >> n;
        a[n-1] = 1;
    }

    for(int i = 0; i < 30; i++) {
        if(a[i] == 0) {
            cout << i+1 << "\n";
        }
    }

    return 0;
}
