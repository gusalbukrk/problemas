#include <iostream>
using namespace std;

int main() {
    int letras[26] = {0};
    int i, ans = 0;
    char p1[20], p2[20];
    cin >> p1;
    cin >> p2;
    
    for(i = 0; p1[i] != '\0'; i++) {
        letras[p1[i] - 'a']++;
    }
    
    for(i = 0; p2[i] != '\0'; i++) {
        letras[p2[i] - 'a']++;
    }
    
    for(i = 0; i < 26; i++) {
        if(letras[i] > ans) {
            ans = letras[i];
        }
    }
    
    if(ans < 3) {
        cout << "SIM" << endl;
    } else {
        cout << "NAO" << endl;
    }
    
    return 0;
}
