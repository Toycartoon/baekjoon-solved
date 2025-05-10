#include <iostream>

using namespace std;

int main() {
    int a, b, c, d;
    cin >> a >> b >> c;
    cin >> d;

    c = c + d;
    b = b + (c / 60);
    c = c % 60;
    a = a + (b / 60);
    b = b % 60;
    a = a % 24;

    cout << a << " " << b << " " << c << endl;

    return 0;
}