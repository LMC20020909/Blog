### 输入处理（ACM 模式）

- 读整行

  ```python
  import sys
  
  input = sys.stdin.readline
  
  a, b = map(int, input().split())
  print(a + b)
  ```

- 读到文件末尾 EOF

  ```python
  import sys
  
  for line in sys.stdin:
      nums = list(map(int, line.split()))
      print(sum(nums))
  ```

  