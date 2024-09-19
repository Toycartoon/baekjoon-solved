#include <iostream>
#include <string>

using namespace std;

int main() {
    string s;

    while(true) {
        if(cin.eof())
            break;
        getline(cin, s);
        cout << s << endl;
    }

    return 0;
}
