#include <iostream>
#include <vector>
#include<algorithm>
using namespace std;


int main() {
    int N = 0;
    cin >> N;
    vector<vector<int>> arr(N + 1, vector<int>(N + 1));
    for (int i = 1; i <= N; i++)
        for (int j = 1; j <= N; j++) cin >> arr[i][j];
    
    int temp = 0;
    vector<vector<int>> add(N+1, vector<int>(N+1));
    for (int i = 1; i <= N; i++) {
        temp = 0;
        for (int j = 1; j <= N; j++) {
            temp += arr[i][j];
            add[i][j] = add[i - 1][j] + temp;
        }
    }

    int top = add[N][N];
    for (int ysize = 1; ysize <= N; ysize++) {
        for (int xsize = 1; xsize <= N; xsize++) {
            for (int i = 0; i <= N-ysize; i++) {
                for (int j = 0; j <= N-xsize; j++) {
                    top = max(top, add[ysize + i][xsize + j] - add[ysize + i][j] - add[i][xsize + j] + add[i][j]);
                }
            }
        }
    }

    cout << top << "\n";
}