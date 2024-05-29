#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, m, x;

    cin >> n >> m;
    vector<vector<int>> a(n, vector<int> (m));
    vector<vector<int>> b(n, vector<int> (m));

    for(int i=0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            cin >> x;
            a[i][j] = x;
        }
    }
    for(int i=0; i < n; i++) {
        for(int j=0; j < m; j++) {
            cin >> x;
            b[i][j] = x;
        }
    }

    vector<vector<int>> ans(n, vector<int> (m));
    for(int i=0; i < n; i++) {
        for(int j=0 ; j < m; j++) {
            ans[i][j] = a[i][j] + b[i][j];
        }
    }

    for(int i=0; i < n; i++) {
        for(int j=0; j < m; j++) {
            cout << ans[i][j] << " ";
        }
        cout << "\n";
    }

    return 0;
}
