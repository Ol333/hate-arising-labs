<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/icpc/index.html">Спортивное программирование</a></li>
  <li class="breadcrumb-item active">Алгоритмы</li>
</ol>

# Алгоритмы

Полезно знать.

## Бинарный поиск

Требуется отсортированный массив.

  <ul class="nav nav-tabs" role="tablist">
  <li class="nav-item" role="presentation">
    <a class="nav-link active" data-bs-toggle="tab" href="#mean" aria-selected="true" role="tab">Смысл</a>
  </li>
  <li class="nav-item" role="presentation">
    <a class="nav-link" data-bs-toggle="tab" href="#anim" aria-selected="false" tabindex="-1" role="tab">Анимация</a>
  </li>
</ul>
<div id="myTabContent" class="tab-content">
  <div class="tab-pane fade show active" id="mean" role="tabpanel">
    <div class="card border-primary mb-2" style="max-width: 30rem;">
        <div class="card-body">
          <img src="{{ site.baseurl }}/img/bin_search.svg"
              alt="Пример"  focusable="false" width="100%"
              class="d-block user-select-none" />
        </div>
      </div>
  </div>
  <div class="tab-pane fade" id="anim" role="tabpanel">
    <div class="card border-primary mb-2" style="max-width: 30rem;">
      <div class="card-body">
        <img src="https://static.tildacdn.com/tild3566-6335-4661-b661-396439326665/binary-and-linear-se.gif"
            alt="Пример"  focusable="false" width="100%"
            class="d-block user-select-none" />
      </div>
    </div>
  </div>
</div>

``` python
def f(a, aim):
  left = -1
  right = len(a)
  while (left < right):
      middle = left + (right - left) // 2
      if a[middle] < aim:
          left = middle + 1
      else:
          right = middle - 1
  return left
  ```

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