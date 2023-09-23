[Главная]({{ site.baseurl }}) >> [Спортивное программирование]({{ site.baseurl }}/icpc/index.html)

# Алгоритмы

Полезно знать.

## Бинарный поиск

Требуется отсортированный массив.

![Алгоритм]({{ site.baseurl }}/img/bin_search.xml)

```python
def f(a, aim):
    left = 0
    right = n-1
    while (left < right)
        middle = (left + right) // 2
        if a[middle] >= aim:
            left = middle
        else:
            right = middle -1
    if a[left] >= aim:
        return a[left]
```

|  | Задача |
| :-: |-|
| 🐌 | |
| 🐣  | |
| 🐤  | [91B](https://codeforces.com/problemset/problem/91/B) |
| 🐔 | [2 задача](https://codeforces.com/gym/100881/attachments) (Космическое поселение) |
