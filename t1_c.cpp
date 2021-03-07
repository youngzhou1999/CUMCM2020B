#include <iostream>
using namespace std;
int type[31] = {0, 1, 1, 0, 2, 0, 1, 2, 0, 1, 1, 2, 1, 0, 1, 1, 1, 2, 2, 1, 1, 0, 0, 1, 0, 2, 1, 0, 0, 1, 1};
int war[3] = {5, 8, 10};
int food[3] = {7, 6, 10};
int main()
{
    int n = 8;
    int sum1 = 0, sum2 = 0;
    int start;
    int end;
    for (int i = start; i <= end; i++)
    {
        sum1 += war[type[i]];
        sum2 += food[type[i]];
    }
    sum1 *= 3;
    sum2 *= 3;
    cout << sum1 << " " << sum2 << endl; //从第start天挖矿到第end天水和食物所需水和食物箱数
    cout << sum1 * 3 + sum2 * 2 << endl; // 第start天挖矿到第end天水和食物所需水和食物总重量
    cout << endl;
    cout << endl;
    cout << endl;
    sum1 = 0;
    sum2 = 0;
    int start1;
    int end1;
    34 for (int i = start1; i <= end1; i++)
    {
        if (type[i] == 2)
        {
            sum1 += war[type[i]];
            sum2 += food[type[i]];
        }
        else
        {
            sum1 += war[type[i]] * 2;
            sum2 += food[type[i]] * 2;
        }
    }
    cout << sum1 << " " << sum2 << endl; //从第start1天行走到第end1天水和食物所需水和食物箱数
    cout << sum1 * 3 + sum2 * 2 << endl; // 第start1天行走到第end1天水和食物所需水和食物总重量
    cout << endl;
    cout << endl;
    cout << endl;
    return 0;
}
