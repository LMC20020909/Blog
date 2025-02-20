---
title: 简单dp
date: 2023-03-13 22:23:58
updated: 2023-03-13 22:23:58
categories: 算法
tags: [算法,c++,动态规划]
excerpt: 如题
index_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20230310_bg2.jpg
banner_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20230310_bg2.jpg
---

## 整体思路

![](https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps//img/image-20230313222229049.png)



## 模板题

### [01背包](https://www.acwing.com/problem/content/2/)（组合数问题）

![](https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps//img/01%E8%83%8C%E5%8C%85.png)

#### 二维写法
```cpp
#include <cstdio>
#include <algorithm>

using namespace std;

const int N = 1010;

int n, m;
int v[N], w[N];
int f[N][N];

int main()
{
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; i ++ )
    {
        scanf("%d%d", &v[i], &w[i]);
    }
    for (int i = 1; i <= n; i ++ )
    {
        for (int j = 1; j <= m; j ++ )
        {
            f[i][j] = f[i - 1][j];
            if (j >= v[i]) f[i][j] = max(f[i][j], f[i - 1][j - v[i]] + w[i]);
        }
    }
    printf("%d", f[n][m]);
    return 0;
}
```

#### 一维写法

```cpp
#include <cstdio>
#include <algorithm>

using namespace std;

const int N = 1010;

int n, m;
int v[N], w[N];
int f[N];

int main()
{
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; i ++ ) scanf("%d%d", &v[i], &w[i]);
    for (int i = 1; i <= n; i ++ )
        for (int j = m; j >= v[i]; j -- )
            f[j] = max(f[j], f[j - v[i]] + w[i]);
    printf("%d", f[m]);
    return 0;
}
```



### [摘花生](https://www.acwing.com/problem/content/1017/)（走法问题）

![](https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps//img/%E6%91%98%E8%8A%B1%E7%94%9F.png)

```cpp
#include <cstdio>
#include <algorithm>

using namespace std;

const int N = 110;

int t, r, c, m[N][N], f[N][N];

int main()
{
    scanf("%d", &t);
    while (t -- )
    {
        scanf("%d%d", &r, &c);
        for (int i = 1; i <= r; i ++ )
            for (int j = 1; j <= c; j ++ )
                scanf("%d", &m[i][j]);
        for (int i = 1; i <= r; i ++ )
        {
            for (int j = 1; j <= c; j ++ )
            {
                f[i][j] = max(f[i - 1][j], f[i][j - 1]) + m[i][j];
            }
        }
        printf("%d\n", f[r][c]);
    }
    return 0;
}
```



### [最长上升子序列](https://www.acwing.com/problem/content/897/)

![](https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps//img/zc.png)

```cpp
#include <cstdio>
#include <algorithm>

using namespace std;

const int N = 1010;

int n, a[N], f[N], ans;

int main()
{
    scanf("%d", &n);
    for (int i = 1; i <= n; i ++ ) scanf("%d", &a[i]);
    for (int i = 1; i <= n; i ++ )
    {
        int res = 0;
        for (int j = i - 1; j > 0; j -- )
        {
            if (a[j] < a[i]) res = max(res, f[j]);
        }
        f[i] = res + 1;
        ans = max(ans, f[i]);
    }
    printf("%d", ans);
    return 0;
}
```



## 综合题

### [地宫取宝](https://www.acwing.com/problem/content/1214/)

![](https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps//img/Screenshot_20230313_225158_com.acwing.app.acwing_app.jpg)

```cpp
#include <cstdio>
#include <algorithm>

const int N = 55, MOD = 1000000007;
int n, m, k, ans;
int w[N][N], f[N][N][13][15];

int main()
{
    scanf("%d%d%d", &n, &m, &k);
    for (int i = 1; i <= n; i ++ )
        for (int j = 1; j <= m; j ++ )
        {
            scanf("%d", &w[i][j]);
            w[i][j]++;
        }
    f[1][1][0][0] = 1;
    f[1][1][1][w[1][1]] = 1;
    for (int i = 1; i <= n; i ++ )
    {
        for (int j = 1; j <= m; j ++ )
        {
            for (int u = 0; u <= k; u ++ )
            {
                for (int v = 0; v <= 13; v ++ )
                {
                    int &val = f[i][j][u][v];		//引用，可直接修改原变量
                    val = (val + f[i - 1][j][u][v]) % MOD;
                    val = (val + f[i][j - 1][u][v]) % MOD;
                    if (u > 0 && v == w[i][j])
                    {
                        for (int c = 0; c < v; c ++ )
                        {
                            val = (val + f[i - 1][j][u - 1][c]) % MOD;
                            val = (val + f[i][j - 1][u - 1][c]) % MOD;
                        }
                    }
                }
            }
        }
    }
    for (int i = 0; i <= 13; i ++ )
        ans = (ans + f[n][m][k][i]) % MOD;
    printf("%d", ans);
    return 0;
}
```



### [波动数列](https://www.acwing.com/problem/content/1216/)

```cpp
#include <cstdio>
#include <algorithm>

using namespace std;

const int N = 1010, MOD = 100000007;
int n, s, a, b;
int f[N][N];

int get_mod(int x, int y)
{
    return (x % y + y) % y;
}

int main()
{
    scanf("%d%d%d%d", &n, &s, &a, &b);
    f[0][0] = 1;
    for (int i = 1; i < n; i ++ )
    {
        for (int j = 0; j < n; j ++ )
        {
            f[i][j] = (f[i][j] + f[i - 1][get_mod(j - (n - i) * a, n)]) % MOD;
            f[i][j] = (f[i][j] + f[i - 1][get_mod(j + (n - i) * b, n)]) % MOD;
        }
    }
    printf("%d", f[n - 1][get_mod(s, n)]);
    return 0;
}
```

+ 倍数、整除问题多思考同余定理
+ 数论中余数都是大于等于零的，如$-2\%10=8$，但在c++中$-2\%10=-2$，所以需要变为正余数：$(a\%b+b)\%b$



## tips

+ 注意初始化的问题，要保证循环中的第一次操作能够得到正确的数。一般按照意义进行初始化即可
+ 尤其是求方案数量的问题一定要初始化
+ 一般对于要在代码中用到i-1或j-1的情况，数组下标从1开始，否则从0开始
+ 动态规划数组的维数可以超过两维，可以根据数据范围和时间复杂度推测数组维数
