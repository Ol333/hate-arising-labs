<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/icpc/index.html">Спортивное программирование</a></li>
  <li class="breadcrumb-item active">Алгоритмы</li>
</ol>

# Алгоритмы

Полезно знать.

## Бинарный поиск

Требуется **отсортированный** массив.

{% tabs algorithm_bin_search %}

{% tab algorithm_bin_search Смысл %}
<div class="card border-primary mb-2" style="max-width: 30rem;">
  <div class="card-body">
    <img src="{{ site.baseurl }}/img/bin_search.svg"
        alt="Пример"  focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>
{% endtab %}

{% tab algorithm_bin_search Анимация %}
<div class="card border-primary mb-2" style="max-width: 30rem;">
  <div class="card-body">
    <img src="https://static.tildacdn.com/tild3566-6335-4661-b661-396439326665/binary-and-linear-se.gif"
        alt="Пример"  focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>
{% endtab %}

{% tab algorithm_bin_search Код %}

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
{% endtab %}

{% endtabs %}

## Задачи:

<table class="table table-hover">
  <tbody>
    <tr>
      <th scope="row">🐌</th>
      <td></td>
    </tr>
    <tr>
      <th scope="row">🐣</th>
      <td></td>
    </tr>
    <tr>
      <th scope="row">🐤</th>
      <td><a href="https://codeforces.com/problemset/problem/91/B">91B</a></td>
    </tr>
    <tr>
      <th scope="row">🐔</th>
      <td><a href="https://codeforces.com/gym/100881/attachments">2 задача</a> (Космическое поселение)</td>
    </tr>
  </tbody>
</table>


Поиск хешированием

Теория чисел

Алгоритм Евклида

Решето Эратосфена

<button type="button" class="btn btn-outline-primary" onclick="window.location.href='#алгоритмы';">Вверх</button>