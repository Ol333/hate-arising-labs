<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/index.html">ИИ</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/big-data/index.html">Обработка данных</a></li>
  <li class="breadcrumb-item active">ЛР №2</li>
</ol>

<nav>
  <ul></ul>
</nav>

# Продолжаем подготовку данных

## Задание 1
Проверить возникают ли приведенные ниже ошибки в известных вам (и доступных на машине) языках программирования высокого уровня.

Онлайн компилятор (если у вас нет ПО): <https://www.onlinegdb.com/online_c_compiler#>

#### 1. Ошибка вызванная точностью представления числа в формате IEEE754

```c
#include "stdio.h"

int main(int argc, char *argv[])
{
    float a, b, f;
    a = 123456789;
    b = 123456788;     
    f = a - b;  
    printf("Result: %f\n", f);
    return 0;
}
```
> Result: 8.000000  (Ответ должен быть 1.000000)

#### 2. Ошибки связанные с неправильным приведением типов данных. Дикие ошибки.

Эти ошибки вызваны тем, что исходное число представленное в формате single и в формате double обычно не равны друг другу.

Например: исходное число 123456789,123456789

Single: 4CEB79A3=+123456792,0(dec)

Double: 419D6F34547E6B75=+123456789,12345679104328155517578125

Разница между Single и Double составит: 2,87654320895671844482421875

```c
#include "stdio.h"

int main(int argc, char *argv[])
{    
    float a;
    double b, f;
    a = 123456789.123457;
    b = 123456789.123457;     
    f = a - b;  
    printf("Result: %f\n", f);
    return 0;
}
```
> Result: 2.876543 (должен быть 0)

#### 3. Ошибка в приведении промежуточных данных

{% tabs big_data_lab2_3 %}

{% tab big_data_lab2_3 Visual Basic (Visual Studio) %}

```vb
Private Sub Command1_Click()
            Dim a As Single
            Dim b As Single
            Dim c As Single

            a = 1
            b = 3
            c = a / b
            c = c - 1 / 3
            Text1.Text = c

        End Sub
```
> Результат: 9,934108E-09 (Должен быть 0.0)	
{% endtab %}

{% tab big_data_lab2_3 C %}

```c
#include "stdio.h"

int main(int argc, char *argv[])
{    
    printf("%f\n", 0.6000006 + 0.09999994);
    float a, b, c;
    a = 1;
    b = 3;
    c = a / b;
    c = c - 1.0f/3;
    printf("Result: %f\n", c);
    return 0;
}
```
> 0.700001

> Result: 0.000000
{% endtab %}

{% endtabs %}


#### 4. Ошибки вызванные сдвигом мантисс. Циклические дыры.

```c
#include "stdio.h"

int main(int argc, char *argv[])
{   
    float a;                        //вес таблетки в кг
    float c;                        //продукции в бункере в кг
    long n;                         //количество циклов;

    c = 300;                        //исходный вес бункера
    a = 0.00001;                    //вес таблетки

    for (n = 1; n < 10000000; n++)
        c = c - a;                  //одна таблетка забирается фасовочной машиной

    printf("Result: %f\n", c);      //измененный вес бункера
    return 0;
}
```
> Result: 300.000000

В данном примере фасовочная машина забрала из бункера 100 кг продукции, а вес продукции в бункере не изменился. Почему не изменился?

Потому, что мантиссы чисел 300 и 0,00001 не пересекаются для формата single .
 
#### 5. Ошибки коммутативности

<div class="table-responsive">
<table class="table table-hover border-primary">
  <thead>
    <tr>
      <th scope="col">0 → 100 (↓)</th>
      <th scope="col">0 ← 100 (↑)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0.0000000000000000000000000</td>
      <td>-0.0000000000142500213018426</td>
    </tr>
    <tr>
      <td>0.0100000000000000002081668</td>
      <td>0.0099999999857499789063242</td>
    </tr>
    <tr>
      <td>0.0200000000000000004163336</td>
      <td>0.0199999999857499791144910</td>
    </tr>
    <tr>
      <td>0.0299999999999999988897770</td>
      <td>0.0299999999857499810573813</td>
    </tr>
    <tr>
      <td>0.0400000000000000008326673</td>
      <td>0.0399999999857499830002716</td>
    </tr>
    <tr>
      <td>0.0500000000000000027755576</td>
      <td>0.0499999999857499849431619</td>
    </tr>
    <tr>
      <td>0.0600000000000000047184479</td>
      <td>0.0599999999857499868860522</td>
    </tr>
    <tr>
      <td>…</td>
      <td>...</td>
    </tr>
    <tr>
      <td>99.8900000000141972122946754</td>
      <td>99.8899999999999437250153278</td>
    </tr>
    <tr>
      <td>99.9000000000142023282023729</td>
      <td>99.8999999999999488409230253</td>
    </tr>
    <tr>
      <td>99.9100000000142074441100704</td>
      <td>99.9099999999999539568307227</td>
    </tr>
    <tr>
      <td>99.9200000000142125600177678</td>
      <td>99.9199999999999590727384202</td>
    </tr>
    <tr>
      <td>99.9300000000142176759254653</td>
      <td>99.9299999999999641886461177</td>
    </tr>
    <tr>
      <td>99.9400000000142227918331628</td>
      <td>99.9399999999999693045538152</td>
    </tr>
    <tr>
      <td>99.9500000000142279077408602</td>
      <td>99.9499999999999744204615126</td>
    </tr>
    <tr>
      <td>99.9600000000142330236485577</td>
      <td>99.9599999999999795363692101</td>
    </tr>
    <tr>
      <td>99.9700000000142381395562552</td>
      <td>99.9699999999999846522769076</td>
    </tr>
    <tr>
      <td>99.9800000000142432554639527</td>
      <td>99.9799999999999897681846051</td>
    </tr>
    <tr>
      <td>99.9900000000142483713716501</td>
      <td>99.9899999999999948840923025</td>
    </tr>
    <tr>
      <td>100.0000000000142534872793476</td>
      <td>100.0000000000000000000000000</td>
    </tr>
   </tbody>
</table>
</div>

```python
variable_d = 100
variable_u = 0
for i in range(1000000000):
    variable_d -= 1/1000000000
    variable_u += 1/1000000000
print(variable_d, variable_u)
```
> 101.00000363545405 -0.9999999925399329


#### 6. Ошибки при обработке циклов

{% tabs big_data_lab2_6 %}

{% tab big_data_lab2_6 C# %}

```csharp
using System;

namespace o_mko
{
    class Program
    {
        static void Main(string[] args)
        {
            double x = 0.2;
            for (int i = 0; i < 40; i++)
            {
                x -= 0.1;
                if (x == 0)
                    Console.WriteLine("ok");
            }
        }
    }
}
```

Result: ok	
{% endtab %}

{% tab big_data_lab2_6 C++ %}

```cpp
#include <iostream>

using namespace std;

int main()
{

    double x = 0.2;
    for (int i = 0; i < 40; i++)
    {
        x -= 0.01;
        if (x == 0)
            cout << "ok";
    }
}
```
Result: ⚪
{% endtab %}

{% endtabs %}

Проблему представления чисел решает создание специализированных библиотек обработки чисел. Обычно для представления числа используют массивы данных, что позволяет не ограничиваться машинными словами и оперировать числами имеющими практически не ограниченное число знаков.  Но при этом используются особые процедуры обработки чисел и, как следствие, существенное замедление вычислений.

Вторым направлением, часто используемым на практике, является переход от вещественных чисел к целым, но он имеет тоже большие ограничения использования.
 
## Задание 2
Скачать данные с температурой по городам с [Kaggle](https://www.kaggle.com/datasets/sudalairajkumar/daily-temperature-of-major-cities). Если очень не хочется регистрироваться на сайте, архив ([2data.zip](https://disk.yandex.ru/d/s6LPb1jWMCzl9A)) можно взять в папке с заданием.

Есть мнение, что обработка чисел `int16`, занимающих 2 байта, должна производиться быстрее, чем обработка `float64`, занимающих 4 байта. Звучит логично. Проверяем на колонке температуры.

Использовать Jupyter Notebook ([шаблон](../../../files/AI-big-data/2lab_blank.ipynb), в котором практически все прописано).

## Задание 3
* Создаем файл Excel следующего вида:

<div class="table-responsive">
<table class="table table-hover border-primary table-bordered ">
  <thead>
    <tr>
      <th scope="col">x1\x2</th>
      <th scope="col">1</th>
      <th scope="col">..</th>
      <th scope="col">100</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>$Y = ax_1+bx_2$</td>
      <td> </td>
      <td> </td>
    </tr>
    <tr>
      <th scope="row">..</th>
      <td> </td>
      <td> </td>
      <td> </td>
    </tr>
    <tr>
      <th scope="row">100</th>
      <td> </td>
      <td> </td>
      <td> </td>
    </tr>
   </tbody>
</table>
</div>

<div class="table-responsive">
 <table class="table table-hover border-primary table-bordered">
   <thead>
     <tr class="table-dark">
       <th scope="col">№ варианта</th>
       <th scope="col">Функция $Y$</th>
     </tr>
   </thead>
   <tbody>
     <tr>
       <th scope="row">1</th>
       <td>$4x_1 - 2x_2$</td>
     </tr>
     <tr>
       <th scope="row">2</th>
       <td>$3x_1 + 8x_2$</td>
     </tr>
     <tr>
       <th scope="row">3</th>
       <td>$-4x_1 + 7x_2$</td>
     </tr>
     <tr>
       <th scope="row">4</th>
       <td>$6x_1 + 5x_2$</td>
     </tr>
     <tr>
       <th scope="row">5</th>
       <td>$-5x_1 - 3x_2$</td>
     </tr>
     <tr>
       <th scope="row">6</th>
       <td>$9x_1 + 2x_2$</td>
     </tr>
     <tr>
       <th scope="row">7</th>
       <td>$2x_1 - 4x_2$</td>
     </tr>
    </tbody>
</table>
</div>

* Строим 3D график.

* Добавляем к $Y$ небольшой шум в интервале [0.01; 0.1].

* Строим 3D график.

* Переводим полученные данные в 3 столбца: $x_1$, $x_2$, $y$.

* Сохраняем в формате .csv.

(Или делаем все то же самое, но Python кодом и сохраняем в `csv`)

\# Импортируем в Python код во 2-й лабе по ИНС для обучения однослойной сети из одного нейрона с 2 входами. 

## Задание 4

Найдите красивую картинку (у вас должен быть `jpg` файл с цветным изображением). Будем готовить данные для бинарной классификации.

Получаем `numpy.array` с цветами пикселей картинки.

Выбираем один цвет, который присутствует на картинке. Выделяем несколько участков изображения, где этот цвет присутствует, и где отсутствует. Из этих участков создаем набор данных для обучения:

<div class="table-responsive">
<table class="table table-hover border-primary table-bordered ">
  <thead>
    <tr>
      <th scope="col">R</th>
      <th scope="col">G</th>
      <th scope="col">B</th>
      <th scope="col">Is it our color?</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>255</td>
      <td>255</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <td>0</td>
      <td>0</td>
      <td>255</td>
      <td>0</td>
    </tr>
   </tbody>
</table>
</div>

\# Импортируем в Python код во 2-й лабе по ИНС для обучения однослойной сети из одного нейрона с 3 входами.

<div class="row">
  <div class="col-lg-12">
    <ul class="list-unstyled">
      <li class="float-end">
        <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#продолжаем-подготовку-данных';">Вверх</button>
      </li>
      <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/big-data/labs/lab3.html';">ЛР №3 →</button>
     </li>
      <li>
        <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/big-data/labs/lab1.html';">← ЛР №1</button>
      </li>
    </ul>
  </div>
</div>