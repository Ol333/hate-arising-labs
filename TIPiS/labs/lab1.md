<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/TIPiS/index.html">ТИПиС</a></li>
  <li class="breadcrumb-item active">ЛР №1</li>
</ol>

<nav>
  <ul></ul>
</nav>

# Разминка

## Пример. А+В

###### ограничение по времени на тест: 1 секунда<br>ограничение по памяти на тест: 256 мегабайт<br>ввод: стандартный ввод<br>вывод: стандартный вывод<br>

Требуется сложить два целых числа А и В.

#### Входные данные

В единственной строке записано два натуральных числа через пробел, не превышающих $10^9$.

#### Выходные данные

В единственную строку нужно вывести одно целое число — сумму чисел А и В.

#### Пример

<table class="table table-hover">
  <thead>
    <tr>
      <th scope="col">Входные данные</th>
      <th scope="col">Выходные данные</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2 3</td>
      <td>5</td>
    </tr>
  </tbody>
</table>

<br><br><br>

## Решение

<script>
  $( function() {
    $( "#tabs" ).tabs();
  } );
  </script>

<div id="tabs">
  <ul>
    <li><a href="#tabs-1">Python</a></li>
    <li><a href="#tabs-2">C#</a></li>
    <li><a href="#tabs-3">C++</a></li>
    <li><a href="#tabs-4">Java</a></li>
  </ul>
  <div id="tabs-1">
    <pre><code class="lang-python">print(sum(map(int,input().split())))</code></pre>
  </div>
  <div id="tabs-2">
    <pre><code class="lang-csharp">using System;

public class Sum{
  private static void Main()
  {
    string[] tokens = Console.ReadLine().Split(' ');
    Console.WriteLine(int.Parse(tokens[0]) + int.Parse(tokens[1]));
  }
}
</code></pre>
  </div>
  <div id="tabs-3">
    <pre><code class="language-cpp">#include &lt;iostream&gt;

using namespace std;

int a,b;

int main()
{
  cin >> a >> b;
  cout << a+b;
  return 0;
}
</code></pre>  
  </div>
  <div id="tabs-4">
    <pre><code class="language-java">import java.io.*;
import java.util.*;

public class Main{
  public static void main(String[] args)
  {
    Scanner in = new Scanner(System.in);
    PrintWriter out = new PrintWriter(System.out);

    int a = in.nextInt();
    int b = in.nextInt();
    out.println(a + b);

    out.flush();
  }
}</code></pre>
  </div>
</div>

## Задание

 <table class="table table-hover">
   <thead>
     <tr>
       <th scope="col">№ варианта</th>
       <th scope="col">Задача</th>
     </tr>
   </thead>
   <tbody>
     <tr class="table-light">
       <th scope="row">1</th>
       <td><a href="http://codeforces.com/problemset/problem/1714/A">1714A - Все любят спать</a></td>
     </tr>
     <tr>
       <th scope="row">2</th>
       <td><a href="https://codeforces.com/problemset/problem/1701/A">1701A - Поляна</a></td>
     </tr>
     <tr class="table-light">
       <th scope="row">3</th>
       <td><a href="http://codeforces.com/problemset/problem/1697/A">1697A - Прогулка по аллее</a></td>
     </tr>
     <tr>
       <th scope="row">4</th>
       <td><a href="http://codeforces.com/problemset/problem/1692/C">1692C - Где слон?</a></td>
     </tr>
     <tr class="table-light">
       <th scope="row">5</th>
       <td><a href="http://codeforces.com/problemset/problem/1684/A">1684A - Много цифр</a></td>
     </tr>
     <tr>
       <th scope="row">6</th>
       <td><a href=" http://codeforces.com/problemset/problem/1676/A">1676A - Счастливый?</a></td>
     </tr>
     <tr class="table-light">
       <th scope="row">7</th>
       <td><a href="http://codeforces.com/problemset/problem/1675/A">1675A - Еда для животных</a></td>
     </tr>
    </tbody>
</table>

Прислать на почту bobrovskaya_op@surgu.ru скриншот принятой задачи на  codeforces или код решения.

 <div class="row">
   <div class="col-lg-12">
     <ul class="list-unstyled">
       <li class="float-end">
         <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#разминка';">Вверх</button>
       </li>
       <li>
         <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/TIPiS/labs/lab2.html';">ЛР №2 →</button>
       </li>
     </ul>
   </div>
 </div>
