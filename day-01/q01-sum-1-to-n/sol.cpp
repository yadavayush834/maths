// sum 1 to n without loop
// trick: ans = n * (n + 1) / 2
#include <bits/stdc++.h>
using namespace std;

int main() {
  long long n;
  if (!(cin >> n)) return 0;
  long long ans = n * (n + 1) / 2;
  cout << ans;
  return 0;
}
