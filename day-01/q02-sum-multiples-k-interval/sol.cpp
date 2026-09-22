#include<bits/stdc++.h>

using namespace std;


int main(){
  int L,R, k ;
  cin >> L>> R >> k ; 

  int count = (R-L)/k + 1 ;
  int ans  = count *(R+L) / 2 ; 
  cout << ans << endl; 
}