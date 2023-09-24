[Главная]({{ site.baseurl }}) >> [Спортивное программирование]({{ site.baseurl }}/icpc/index.html)

# Алгоритмы

Полезно знать.

## Бинарный поиск

Требуется отсортированный массив.

<script>
  $( function() {
    $( "#tabs" ).tabs();
  } );
  </script>
  
<div id="tabs">
  <ul>
    <li><a href="#tabs-1">Смысл</a></li>
    <li><a href="#tabs-2">Python</a></li>
  </ul>
  <div id="tabs-1">
    ![Алгоритм]({{ site.baseurl }}/img/bin_search.xml)
  </div>
  <div id="tabs-2">
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
  </div>
  </div>
</div>



|  | Задача |
| :-: |-|
| 🐌 | |
| 🐣  | |
| 🐤  | [91B](https://codeforces.com/problemset/problem/91/B) |
| 🐔 | [2 задача](https://codeforces.com/gym/100881/attachments) (Космическое поселение) |
