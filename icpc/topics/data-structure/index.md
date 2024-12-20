<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/icpc/index.html">Спортивное программирование</a></li>
  <li class="breadcrumb-item active">Структуры данных</li>
</ol>

# Структуры данных

Стоит знать различные способы представления данных и алгоритмы для их обработки.

# <a id="stack">Стек</a>

Стек (англ. stack – стопка) — абстрактный тип данных, представляющий собой список элементов, организованных по принципу LIFO (англ. last in — first out, «последним пришёл — первым вышел»).

[Здесь](https://www.programiz.com/dsa/stack), вроде, понятно, но на английском.

По принципу стека реализуется вызов функций (например, рекурсия): чтобы обеспечить для функции локальные переменные, все текущее состояние памяти программы закидывается в стек, после чего она проходит по коду вызванной функции; затем из стека достается последнее состояние памяти записывается возвращенное функцией значение и продолжается работа.

Функции стека: `push()`, `pop()` - добавить элемент, забрать элемент.

`STACK_UNDERFLOW` ошибка опустошения - обращение к пустому стеку.
`STACK_OVERFLOW` ошибка переполнения - стек исчерпал выделенную ему память, а мы продолжаем добавлять элементы.

### Python

В принципе, все необходимое реализовано в list структуре: append() - аналог push(), pop() без аргументов работает как pop().


### C

Надо реализовать структуру самостоятельно.

Как [рассказывает умный человек](https://learnc.info/adt/stack.html), сделать это можно 3-мя вариантами:
* на массиве;
* на массиве, но динамически;
* динамически, с помощью указателей.

## Задачи:

<table class="table table-hover">
  <tbody>
    <tr>
      <th scope="row">🐌</th>
      <td><a href="https://codeforces.com/problemset/problem/399/b">399B</a></td>
      <td></td>
    </tr>
    <tr>
      <th scope="row">🐣</th>
      <td><a href="https://codeforces.com/contest/612/problem/C">612C</a>, <a href="https://codeforces.com/problemset/problem/91/B">6191B2C</a></td>
    <td>скобочная последовательность</td>
    </tr>
    <tr>
      <th scope="row">🐤</th>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th scope="row">🐔</th>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

_____________

# <a id="queue">Очередь</a>

У очереди есть голова (head) и хвост (tail).
Работает по принципу FIFO (англ. first in — first out, «первым пришёл — первым вышел»).

Операции добавления `ENQUEUE()` и взятия `DEQUEUE()` элемента.

### Python

```py
from collections import deque
```

Поскольку list медленно обрабатывает добавление и удаление первого элемента, то лучше использовать этот двусвязный список, в котором поддерживаются операции быстрого взятия и добавления как первого, так и последнего элемента (но не из центра по индексу).

### C

Элементы очереди расположены в ячейках которые циклически замкнуты в том смысле, что ячейка 1 следует сразу же после ячейки n в циклическом порядке.

____

# <a name="graf">Графы</a>

*Граф* - это совокупность вершин, соединеных ребрами.

$G = (V, E)$, где $G$ - граф, $V$ - его вершины (узлы), $E$ - ребра (дуги);
$|V|$ - порядок графа (число вершин);
$|E|$ - размер графа (число ребер).

Когда из любой связанной вершины можно перейти в другую вершину и обратно, то такой граф называется *неориентированным*. Если же это условие не выполняется (ребра являются направленными), тогда такой граф называется *ориентированным* или *орграфом*.

Степень вершины - это количество ребер, соединяющих ее с другими вершинами. Сумма всех степеней графа равна удвоенному количеству всех его ребер.

*Изоморфные* графы (каждая вершина одного графа имеет тождественную вершину в другом):

<div class="card border-primary mb-2" style="max-width: 20rem;">
<div class="card-body">
  <img src="https://kvodo.ru/wp-content/uploads/izomorph_graph.jpg"
        alt="изоморфные графы"  focusable="false" width="100%"
        class="d-block user-select-none" />
</div>
</div>

Когда каждому ребру графа поставлено в соответствие некоторое значение, называемое весом ребра, тогда такой граф называют *взвешнным*.

*Путь* - это последовательность вершин, каждая из которых соединена с последующей посредством ребра. Если первая и последняя вершины совпадают, то такой пость называется циклом. Длина пути определяется количеством составляющих его ребер.

<div class="card border-primary mb-2" style="max-width: 10rem;">
  <div class="card-body">
    <img src="{{ site.baseurl }}/img/graf.svg"
          alt="граф"  focusable="false" width="100%"
          class="d-block user-select-none" />
  </div>
</div>

Граф на рис. выше можно представить следующими способами:
<li><b>матрица смежности</b>. Если из $i$ в $j$ существует ребро, то <code>A[i][j] = 1</code>, в противном случае <code>A[i][j] = 0</code>. Получается двуменый массив, размерности $n*n$, где $n$ - число вершин графа.
<pre><code class="language-c">int graph[n][n] = {
{0, 1, 0, 1},
{0, 0, 1, 1},
{0, 1, 0, 0},
{1, 0, 1, 0}};
</code></pre></li>
<li><b>матрица инцидентности.</b> Две вершины $u$ и $v$ являются смежными, если в графе $G$ существует ребро $(u, v)$, в противном случае $u$ и $v$ независимы. Про ребро $(u, v)$ также говорят, что оно инцидентно вершинам $u$ и $v$. Размерность матрицы $n*m$, где $n$ - число вершин, $m$ - число ребер. Если вершина $i$ инцидентна ребру $j$, то <code>A[i][j] = 1</code> (для ориентированного графа 1, если вершина является началом ребра, -1 - если концом), иначе <code>A[i][j] = 0</code>.
<pre><code class="language-c">int graph[n][m] = {
{1, 1, 0, 0, 0},
{-1, 0, 1, 1, 0},
{0, 0, 0, 1, -1},
{0, 1, -1, 0, 1}};
</code></pre></li>
<li><b>список смежности.</b> Требует меньше памяти, потому что не храним нули. Для каждой вершины храним список вершин, в которые из нее можно попасть.
<pre><code class="language-py">graph = { 1 : [2,4], 
          2 : [3,4], 
          3 : [2], 
          4 : [1,3]}
</code></pre></li>
<li><b>список ребер.</b> Список, в каждой строке которого записаны две смежные вершины и вес соединяющего их ребра.
<pre><code class="language-py">graph = { [1,2] : a, 
          [2,4] : c,
          [2,3] : d,
          [3,2] : d,
          [4,3] : e,
          [4,1] : b,
          [1,4] : b}
</code></pre></li>

**Обход графа** - последовательность вершин графа, в которой каждая вершина графа содержится ровно один раз.

### Обход в ширину (Breadth First Search)

<div class="card border-primary mb-2" style="max-width: 50rem;">
  <div class="card-body">
    <img src="{{ site.baseurl }}/img/graf_BFS.svg"
          alt="Обход в ширину"  focusable="false" width="100%"
          class="d-block user-select-none" />
  </div>
</div>

Потребуется очередь (`queue`) и массив посещенных вершин (`vis`).

Алгоритм:

1. Массив `vis` обнуляется, т.е. ни одна вершина графа еще не была посещена.
1. В качестве стартовой выбирается некоторая вершина $p$ и помещается в очередь (в массив `queue`).
1. Вершина $p$ исследуется (помечается как посещенная в `vis`), и все смежные с ней вершины помещаются в конец очереди, а сама она удаляется.
1. Если очередь пуста, то алгоритм останавливается.
1. Посещается вершина $u$, стоящая в начале очереди, помечается как посещенная, и все ее потомки заносятся в конец очереди.
1. Процесс продолжается, начиная с пункта 4.

### Обход в глубину (Depth First Search)

<div class="card border-primary mb-2" style="max-width: 50rem;">
  <div class="card-body">
    <img src="{{ site.baseurl }}/img/graf_DFS.svg"
          alt="Обход в глубину"  focusable="false" width="100%"
          class="d-block user-select-none" />
  </div>
</div>

Рекурсивный алгоритм - функция `DFS(p)`, получающая на вход номер вершины:
1. В массиве `vis` вершина отмечается как посещенная.
1. В цикле для всех смежных ребер:
    * Если вторая вершина $u$ ребра не посещена, то вызвать для нее функцию `DFS(u)`.


## Задачи

<table class="table table-hover">
  <tbody>
    <tr>
      <th scope="row">🐌</th>
      <td><a href="https://codeforces.com/contest/1033/problem/A">1033A</a></td>
    </tr>
    <tr>
      <th scope="row">🐣</th>
      <td></td>
    </tr>
    <tr>
      <th scope="row">🐤</th>
      <td></td>
    </tr>
    <tr>
      <th scope="row">🐔</th>
      <td></td>
    </tr>
  </tbody>
</table>

_____________

# <a id="disjoint-set-union">Cистема непересекающихся множеств</a>

Cтруктура данных, позволяющая объединять непересекающиеся множества и отвечать на несколько запросов про них: «находятся ли элементы $a$ и $b$ в одном множестве» и «чему равен размер данного множества».

Также, в классическом варианте, вводится ещё одна операция — создание нового элемента, который помещается в отдельное множество.

[здесь](https://ru.algorithmica.org/cs/set-structures/dsu/) можно взять код

[чтобы понять получше](http://e-maxx.ru/algo/dsu)

## Задачи

<table class="table table-hover">
  <tbody>
    <tr>
      <th scope="row">🐌</th>
      <td></td>
    </tr>
    <tr>
      <th scope="row">🐣</th>
      <td><a href="https://sp.urfu.ru/qf/2024/qual/statements.pdf">Задача G</a> (Ненавижу шахматы)</td>
    </tr>
    <tr>
      <th scope="row">🐤</th>
      <td></td>
    </tr>
    <tr>
      <th scope="row">🐔</th>
      <td></td>
    </tr>
  </tbody>
</table>


________

# <a id="dynamic_programming">Динамическое программирование</a>

способ решения сложных задач путём разбиения их на более простые подзадачи.

## Задачи

<table class="table table-hover">
  <tbody>
    <tr>
      <th scope="row">🐌</th>
      <td></td>
    </tr>
    <tr>
      <th scope="row">🐣</th>
      <td><a href="https://codeforces.com/contest/1195/problem/C">1195C</a></td>
    </tr>
    <tr>
      <th scope="row">🐤</th>
      <td><a href="https://codeforces.com/contest/1221/problem/D">1221D</a></td>
    </tr>
    <tr>
      <th scope="row">🐔</th>
      <td></td>
    </tr>
  </tbody>
</table>

___

# <a id="greedy_algorithm">Жадные алгоритмы</a>
[1810C](https://codeforces.com/contest/1810/problem/C)


<button type="button" class="btn btn-outline-primary" onclick="window.location.href='#структуры-данных';">Вверх</button>