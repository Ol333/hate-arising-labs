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

### Решение

{% tabs TIPIiS_lab1 %}

{% tab TIPIiS_lab1 Python %}
``` python
print(sum(map(int,input().split())))
```
{% endtab %}

{% tab TIPIiS_lab1 C# %}

``` csharp
using System;

public class Sum{
  private static void Main()
  {
    string[] tokens = Console.ReadLine().Split(' ');
    Console.WriteLine(int.Parse(tokens[0]) + int.Parse(tokens[1]));
  }
}
```
{% endtab %}

{% tab TIPIiS_lab1 C++ %}

``` cpp
#include <iostream>;

using namespace std;

int a,b;

int main()
{
  cin >> a >> b;
  cout << a+b;
  return 0;
}
```
{% endtab %}

{% tab TIPIiS_lab1 Java %}

``` java
import java.io.*;
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
}
```
{% endtab %}

{% tab TIPIiS_lab1 C %}

```c 
#include <stdio.h>

int main()
{
    long long int a, b;
    scanf("%lld %lld", &a, &b);
    printf("%lld", a + b);
}
```
{% endtab %}

{% tab TIPIiS_lab1 JavaScript v8 %}

```javascript
    var x = readline().split(' ');
    print(+x[0]+(+x[1]));
```
{% endtab %}

{% tab TIPIiS_lab1 Node.js %}

``````javascript 
    const readline = require('readline').createInterface({
          input: process.stdin,
          output: process.stdout
        });
    
    readline.question('', t => {
          
            temp = t.split(' ');
            console.log( +temp[0] + (+temp[1]) );
            
      readline.close();
    });
```
{% endtab %}

{% endtabs %}

___


## Пояснение к формату данных

Это лабораторная с автоматической проверкой. Это значит, что в проверяющей системе для каждой задачи есть набор тестов для проверки правильности решения.

Эти тесты имеют строгий формат, который описывается в частях [Входные данные](#входные-данные) и [Выходные данные](#выходные-данные):
* Ограничения, прописанные в условии строго соблюдаются, поэтому ***не нужно проверять вводимые данные***.
* Формат ввода и вывода должен строго соблюдаться *вами*: после запуска программы вы вставляете (Ctrl+V) данные из примера ввода, и программа возвращает данные, которые указаны в примере вывода, ни больше, ни меньше ***(без комментариев пользователю)***.

## Задание 📑 🐾

* Решить задачу по варианту.
* Чтобы сдать лабораторную, нужно сделать **одно из следующего**:
  * Прислать на почту bobrovskaya_op@surgu.ru **код решения**.
  * Если вы зарегистрировались на сайте Codeforces, показать на паре **принятую задачу** или прислать на почту bobrovskaya_op@surgu.ru **скриншот принятой задачи**.

<div class="table-responsive">
 <table class="table table-hover border-primary table-bordered">
   <thead>
     <tr class="table-dark">
       <th scope="col">№ варианта</th>
       <th scope="col">Задача</th>
     </tr>
   </thead>
   <tbody>
     <tr>
       <th scope="row">1</th>
       <td><a href="http://codeforces.com/problemset/problem/1714/A" target="_blank">1714A - Все любят спать</a></td>
     </tr>
     <tr>
       <th scope="row">2</th>
       <td><a href="https://codeforces.com/problemset/problem/1701/A" target="_blank">1701A - Поляна</a></td>
     </tr>
     <tr>
       <th scope="row">3</th>
       <td><a href="http://codeforces.com/problemset/problem/1697/A" target="_blank">1697A - Прогулка по аллее</a></td>
     </tr>
     <tr>
       <th scope="row">4</th>
       <td><a href="https://codeforces.com/problemset/problem/2148/A" target="_blank">2148A - Возвышенная последовательность</a></td>
     </tr>
     <tr>
       <th scope="row">5</th>
       <td><a href="http://codeforces.com/problemset/problem/1684/A" target="_blank">1684A - Много цифр</a></td>
     </tr>
     <tr>
       <th scope="row">6</th>
       <td><a href=" http://codeforces.com/problemset/problem/1676/A" target="_blank">1676A - Счастливый?</a></td>
     </tr>
     <tr>
       <th scope="row">7</th>
       <td><a href="http://codeforces.com/problemset/problem/1675/A" target="_blank">1675A - Еда для животных</a></td>
     </tr>
     <tr>
       <th scope="row">8</th>
       <td><a href="https://codeforces.com/contest/1923/problem/A" target="_blank">1923A - Перемещение фишек</a></td>
     </tr>
     <tr>
       <th scope="row">9</th>
       <td><a href="https://codeforces.com/contest/1033/problem/A" target="_blank">1033A - Побег короля</a></td>
     </tr>
     <tr>
       <th scope="row">10</th>
       <td><a href="https://codeforces.com/contest/1816/problem/A" target="_blank">1816A - Ян навещает Мэри</a></td>
     </tr>
     <tr>
       <th scope="row">11</th>
       <td><a href="https://codeforces.com/contest/2014/problem/A" target="_blank">2014A - Робин Помогает</a></td>
     </tr>
     <tr>
       <th scope="row">12</th>
       <td><a href="https://codeforces.com/contest/1774/problem/A" target="_blank">1774A - Добавьте плюсы и минусы</a></td>
     </tr>
    </tbody>
</table>
</div>

 <div class="row">
   <div class="col-lg-12">
     <ul class="list-unstyled">
       <li class="float-end">
         <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#разминка';">Вверх</button>
       </li>
       <li class="float-end">
         <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/TIPiS/labs/lab2.html';">ЛР №2 →</button>
       </li>
     </ul>
   </div>
 </div>
