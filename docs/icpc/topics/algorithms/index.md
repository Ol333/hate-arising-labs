<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/icpc/index.html">Спортивное программирование</a></li>
  <li class="breadcrumb-item active">Алгоритмы</li>
</ol>

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
    <li><a href="#tabs-2">Анимация</a></li>
    <li><a href="#tabs-3">Python</a></li>
  </ul>
  <div id="tabs-1">
    <div class="card border-primary mb-2" style="max-width: 30rem;">
        <div class="card-body">
          <img src="{{ site.baseurl }}/img/bin_search.svg"
              alt="Пример"  focusable="false" width="100%"
              class="d-block user-select-none" />
        </div>
      </div>
  </div>
  <div id="tabs-2">
    <div class="card border-primary mb-2" style="max-width: 30rem;">
      <div class="card-body">
        <img src="https://static.tildacdn.com/tild3566-6335-4661-b661-396439326665/binary-and-linear-se.gif"
            alt="Пример"  focusable="false" width="100%"
            class="d-block user-select-none" />
      </div>
    </div>
  </div>
  <div id="tabs-3">
    <pre><code class="language-python">def f(a, aim):
  left = -1
  right = len(a)
  while (left < right):
      middle = left + (right - left) // 2
      if a[middle] < aim:
          left = middle + 1
      else:
          right = middle - 1
  return left
    </code></pre>  
  </div>
</div>



|  | Задача |
| :-: |-|
| 🐌 | |
| 🐣  | |
| 🐤  | [91B](https://codeforces.com/problemset/problem/91/B) |
| 🐔 | [2 задача](https://codeforces.com/gym/100881/attachments) (Космическое поселение) |


Поиск хешированием

Теория чисел

Алгоритм Евклида

Решето Эратосфена

<button type="button" class="btn btn-outline-primary" onclick="window.location.href='#алгоритмы';">Вверх</button>