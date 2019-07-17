# 190717 python -day3

## Python

### benchmark

```python
import time

start = time.time()

# code

end = time.time()
print(end - start)
```

### tip

- `for _ in range()` : _ 는 별 의미 없을 때 쓰는 약속 (convention : 규칙, 오류가 나지는 않지만 관용적으로 쓰는 표현)

### Error

'int' object is not iterable : 정수 객체는 반복 가능하지 않음