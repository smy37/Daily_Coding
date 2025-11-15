#include <iostream>
#include <vector>
#include <utility>
#include <stack>

using namespace std;

int main() {
	int N; 
	cin >> N;

	vector<vector<int>> window_dependency(N);
	vector<pair<int, int>> exit_l; 

	for (int i = 0; i < N; i++){
		int r1, c1, r2, c2;
		cin >> r1 >> c1 >> r2 >> c2;
		int exit_x = r1, exit_y = c2;

		for (int j = 0; j < (int)exit_l.size(); j++){
			auto [r, c] = exit_l[j];
			if (r1 <= r && r <= r2 && c1 <= c && c <= c2){
				window_dependency[j].push_back(i);
			}
		}
		exit_l.push_back({exit_x, exit_y});
	}

	vector<bool> visited(N, false);
	stack<int> st;

	st.push(0);
	visited[0] = true;

	while (!st.empty()){
		int cur = st.top();
		st.pop();
		
		for (int nxt : window_dependency[cur]){
			if (!visited[nxt]){
				st.push(nxt);
				visited[nxt] = true;
			}
		}
	}

	int answer = 0;
	for (bool b : visited){
		if (b){
			answer += 1;
		}
	}
	
	cout << answer << "\n";

	return 0;
}
