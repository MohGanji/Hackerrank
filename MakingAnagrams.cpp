// The problem is here:
// https://www.hackerrank.com/challenges/ctci-making-anagrams

#include <cmath>
#include <iostream>

using namespace std;

int main(){
    string a, b;
    cin >> a >> b;
    
    int lettersA[26] = {0}, lettersB[26] = {0};
    
    
    for (int i = 0 ; i < a.length() ; i++){
        lettersA[int(a[i] - 'a')]++;
    }
    for (int i = 0 ; i < b.length() ; i++){
        lettersB[int(b[i] - 'a')]++;
    }
    int ans = 0;
    for (int i = 0 ; i < 26 ; i++){
        ans += abs(lettersB[i] - lettersA[i]);
    }
    cout << ans << endl;
    
    
    return 0;
}
