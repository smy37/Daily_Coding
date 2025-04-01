#include <vector>
#include <iostream>
using namespace std;

int MOD = 20170805;

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int solution(int m, int n, vector<vector<int>> city_map) {
    int answer = 0;
    int t_sum = 0;
    vector<pair<int,int>> stack;
    for (int i = 0; i < m*n; i++)
    {
        stack.push_back(make_pair(0,0));
    }
    stack[0].first = 1;
    for (int i = 0; i < m; i++)
    {
        for (int j =0; j < n; j++)
        {
            if (city_map[i][j] == 0)
            {
                t_sum = (stack[i*n+j].first + stack[i*n+j].second)%MOD;
                if (j+1 < n){stack[i*n+j+1].first = t_sum;}
                if (i+1 < m){stack[(i+1)*n+j].second = t_sum;}
            }
            else if (city_map[i][j] == 1)
            {
                continue;
            }
            else if (city_map[i][j] == 2)
            {
                if (j+1 < n) {stack[i*n+j+1].first = stack[i*n+j].first%MOD;}
                if (i+1 < m) {stack[(i+1)*n+j].second = stack[i*n+j].second%MOD;}
            }
        }
    }
    
    answer = stack[m*n-1].first+stack[m*n-1].second;
    answer = answer%MOD;
    return answer;
}



///////// 처음에 시도했던 풀이, BFS를 썼기 때문에 시간초과가 발생하였다.     //////////

//#include <vector>
//#include <iostream>
//using namespace std;
//
//int MOD = 20170805;
//
//// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
//int solution(int m, int n, vector<vector<int>> city_map) {
//    int answer = 0;
//    vector<vector<int>> stack;
//    int cur_x = 0;
//    int cur_y = 0;
//    if (cur_x + 1 < m)
//    {
//        vector<int> temp = {1, 0, 0};
//        stack.push_back(temp);
//    }
//
//    if (cur_y +1 < n)
//    {
//        vector<int> temp = {0, 1, 1};
//        stack.push_back(temp);
//    }
//
//    vector<int> cur;
//
//    while(stack.size()>0)
//    {
//        cur = stack.back();
//        stack.pop_back();
//
//        if (cur[0] == m-1 && cur[1] == n-1)
//        {
//            answer +=1;
//        }
//        else if (city_map[cur[0]][cur[1]] == 0)
//        {
//            if (cur[0]+1 < m)
//            {
//                vector<int> temp = {cur[0]+1, cur[1], 0};
//                stack.push_back(temp);
//            }
//            if (cur[1]+1 < n)
//            {
//                vector<int> temp = {cur[0], cur[1]+1, 1};
//                stack.push_back(temp);
//            }
//        }
//        else if (city_map[cur[0]][cur[1]] == 1)
//        {
//            continue;
//        }
//        else if (city_map[cur[0]][cur[1]] == 2)
//        {
//            if (cur[2] == 0)
//            {
//                if (cur[0]+1 < m)
//                {
//                    vector<int> temp = {cur[0]+1, cur[1], 0};
//                    stack.push_back(temp);
//                }
//            }
//            else if (cur[2] == 1)
//            {
//                if (cur[1]+1 < n)
//                {
//                    vector<int> temp = {cur[0], cur[1]+1, 1};
//                    stack.push_back(temp);
//                }
//            }
//
//        }
//    }
//
//    answer = answer%MOD;
//    return answer;
//}