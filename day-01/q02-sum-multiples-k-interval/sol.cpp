// sum multiples of k in [L, R], no loop
// trick: sum up to N is k * m * (m + 1) / 2 where m = N / k
// ans = sum(R) - sum(L - 1)
#include <bits/stdc++.h>
using namespace std;

int main() {
  long long L, R, k;
  if (!(cin >> L >> R >> k)) return 0;
  long long a = R / k;
  long long b = (L - 1) / k;
  long long ans = k * (a * (a + 1) / 2 - b * (b + 1) / 2);
  cout << ans;
  return 0;
}
