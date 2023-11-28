<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/TIPiS/index.html">ТИПиС</a></li>
  <li class="breadcrumb-item active">ЛР №7</li>
</ol>

<nav>
  <ul></ul>
</nav>

# Бинарные файлы

Преодолеваем страх перед битами, байтами и поразрядными операциями.
Эти навыки понадобятся в следующей лабораторной.

Вывод на экран целого числа в двоичной форме:

<script>
  $( function() {
    $( "#tabs" ).tabs();
  } );
  </script>

<div id="tabs">
  <ul>
    <li><a href="#tabs-1">Python</a></li>
    <li><a href="#tabs-2">C</a></li>
    <li><a href="#tabs-3">C++</a></li>
  </ul>
  <div id="tabs-1">
    <pre><code class="lang-python">number = 5
print(f"number = {number:0b}")
print(bin(number))</code></pre>
  </div>
  <div id="tabs-2">
    <pre><code class="lang-c">#include &lt;stdio.h&gt;

void print_binary(int n)
{
    int a[10], i;
    for (i = 0; n > 0; i++)
    {
        a[i] = n % 2;
        n = n / 2;
    }
    for (i = i - 1; i >= 0; i--) 
    {
        printf("%d", a[i]);
    }
    return 0;
}

int main()
{
  int number = 5;
  print_binary(number);
}</code></pre>
  </div>
  <div id="tabs-3">
    <pre><code class="language-cpp">#include &lt;bitset&gt;

using namespace std;

void print_binary(int a)
{
  std::bitset<8> x(a);
  std::cout << x << '\n';

  return 0;
}

int main()
{
  int number = 5;
  print_binary(number);
}</code></pre>  
  </div>
</div>

<br><br>

Логические операции одинаковые во всех языках:

<table class="table table-hover border-primary">
  <thead>
    <tr>
      <th scope="col">Описание</th>
      <th scope="col">Применение в коде</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>логическое умножение чисел $x$ и $y$</td>
      <td>x & y</td>
    </tr>
    <tr>
      <td>логическое сложение чисел $x$ и $y$</td>
      <td>x | y</td>
    </tr>
    <tr>
      <td>логическое исключающее ИЛИ чисел $x$ и $y$</td>
      <td>x ^ y</td>
    </tr>
    <tr>
      <td>инверсия числа $x$</td>
      <td>~ x</td>
    </tr>
    <tr>
      <td>сдвигает число $x$ влево на $y$ разрядов</td>
      <td>x << y</td>
    </tr>
    <tr>
      <td>сдвигает число $x$ вправо на $y$ разрядов</td>
      <td>x >> y</td>
    </tr>
   </tbody>
</table>


## Задание 1. Поразрядные операции, двоичная запись

Выполнить задание по варианту. Считывание данных (десятичного числа/чисел) происходит с консоли. Программа выводит в консоль представление числа в двоичной форме и результат своей работы.

Постарайтесь использовать операции из таблицы выше, а не работу со строками.

<table class="table table-hover">
  <thead>
    <tr>
      <th scope="col">№ варианта</th>
      <th scope="col">Задача</th>
    </tr>
  </thead>
  <tbody>
    <tr class="table-active">
      <th scope="row">1</th>
      <td>Определить, делится ли число на 2, не используя операцию нахождения остатка от деления (%)</td>
    </tr>
    <tr class="table-primary">
      <th scope="row">2</th>
      <td>Возвести 2 в степень m, не используя операции возведения в степень и умножения</td>
    </tr>
    <tr class="table-active">
      <th scope="row">3</th>
      <td>Для натурального числа поcчитать количество единиц, стоящих на нечетных местах в его двоичной форме</td>
    </tr>
    <tr class="table-primary">
      <th scope="row">4</th>
      <td>Найти сумму двух двоичных чисел (например, 0110 и 0100)</td>
    </tr>
    <tr class="table-active">
      <th scope="row">5</th>
      <td>Для натурального числа поcчитать количество нулей, стоящих на нечетных местах в его двоичной форме</td>
    </tr>
    <tr class="table-primary">
      <th scope="row">6</th>
      <td>Умножить число на 2, не используя операции умножения и сложения</td>
    </tr>
    <tr class="table-active">
      <th scope="row">7</th>
      <td>Разделить число на 2, не используя операцию деления</td>
    </tr>
    <tr class="table-primary">
      <th scope="row">8</th>
      <td>Для натурального числа поcчитать количество нулей, стоящих на четных местах в его двоичной форме</td>
    </tr>
    <tr class="table-active">
      <th scope="row">9</th>
      <td>Возвести 1024 в степень (1/m), не используя операции возведения в степень, деления и умножения</td>
    </tr>
    <tr class="table-primary">
      <th scope="row">10</th>
      <td>Найти произведение двух двоичных чисел (например, 0110 и 0100)</td>
    </tr>
    <tr class="table-active">
      <th scope="row">11</th>
      <td>Для натурального числа осуществить циклический сдвиг битов влево на N позиций</td>
    </tr>
    <tr class="table-primary">
      <th scope="row">12</th>
      <td>Для натурального числа поcчитать количество единиц, стоящих на четных местах в его двоичной форме</td>
    </tr>
   </tbody>
</table>

## Задание 2. Символы и работа с файлами

1. Записать свою строку в бинарный файл.

2. Считать строку из своего бинарного файла и вывести на экран.

3. Считать строку из бинарного [файла]({{ site.baseurl }}/files/TIPiS/7lab_input2.bin) в кодировке UTF-8.

Если не знаете, в чем посмотреть бинарный файл, и у вас есть Visual Studio, то [можно](https://learn.microsoft.com/ru-ru/cpp/windows/binary-editor?view=msvc-170) в ней.

## Задание 3. Шеснадцатиричный код результата операции

<ol>
<li>Написать программу, в которой с помощью вводимых с клавиатуры параметров $Р_1$, $Р_2$, $Р_3$ и $Р_4$, формируется число $А_{16}$ и выводится на экран в двоичном и шестнадцатеричном формате. Пример:

<div class="table-responsive">
<table class="table table-bordered">
  <tbody>
    <tr class="table-active">
      <td>№ разряда</td>
      <td>15</td>
      <td>14</td>
      <td>13</td>
      <td>12</td>
      <td>11</td>
      <td>10</td>
      <td>09</td>
      <td>08</td>
      <td>07</td>
      <td>06</td>
      <td>05</td>
      <td>04</td>
      <td>03</td>
      <td>02</td>
      <td>01</td>
      <td>00</td>
    </tr>
    <tr>
      <td>$A_2$</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>$A_{16}$</td>
      <td colspan="4">9</td>
      <td colspan="4">A</td>
      <td colspan="4">2</td>
      <td colspan="4">E</td>
    </tr>
    <tr class="table-active">
      <td>№ разряда</td>
      <td colspan="4">3</td>
      <td colspan="4">2</td>
      <td colspan="4">1</td>
      <td colspan="4">0</td>
    </tr>
  </tbody>
</table>
</div>
</li>

<li>Написать программу, которая бы считывала с клавиатуры число $А_{16}$ в шестнадцатеричном формате и выводила значение параметров $Р_1$, $Р_2$, $Р_3$, ($Р_4$).
Параметры $Р_2$, $Р_3$, ($Р_4$) должны быть выведены в виде десятичных чисел, а параметр $Р_1$ в виде словесного выражения, как указано в варианте.</li>

<li>То же, что и в предыдущем пункте, только считать $А_{16}$ из бинарного [файла]({{ site.baseurl }}/files/TIPiS/7lab_input3.bin).</li>

<li>Записать $А_{16}$ в новый файл, затем инвертировать биты в $А_{16}$ и дозаписать в тот же файл. Показать, что файл бинарный и в нем записано именно то, что требуется.</li>



<div class="table-responsive">
<table class="table table-hover">
  <thead>
    <tr>
      <th scope="col">№ варианта</th>
      <th scope="col">Задача</th>
    </tr>
  </thead>
  <tbody>
    <tr class="table-active">
      <th scope="row">1</th>
      <td>Код ошибки при работе с диском $A_{16}$ включает в себя несколько информационных полей ($Р_1$, $Р_2$, $Р_3$ и $Р_4$) и имеет вид:
      <table class="table table-bordered">
        <tbody>
          <tr>
            <td>№ разряда</td>
            <td>15</td>
            <td>14</td>
            <td>13</td>
            <td>12</td>
            <td>11</td>
            <td>10</td>
            <td>09</td>
            <td>08</td>
            <td>07</td>
            <td>06</td>
            <td>05</td>
            <td>04</td>
            <td>03</td>
            <td>02</td>
            <td>01</td>
            <td>00</td>
          </tr>
          <tr>
            <td>Смысл</td>
            <td>$K$</td>
            <td>$A_1$</td>
            <td>$A_0$</td>
            <td>$R_2$</td>
            <td>$R_1$</td>
            <td>$R_0$</td>
            <td>$0$</td>
            <td>$1$</td>
            <td>$D_7$</td>
            <td>$D_6$</td>
            <td>$D_5$</td>
            <td>$D_4$</td>
            <td>$D_3$</td>
            <td>$D_2$</td>
            <td>$D_1$</td>
            <td>$D_0$</td>
          </tr>
        </tbody>
      </table>
      $P_1 = K$ – тип производимой операции (0: "чтение", 1: "запись"),<br>
      $P_2 = A_1A_0$ – код области диска, в которой произошла ошибка,<br>
      $P_3 = R_2R_1R_0$ – допустимые реакции на возникшую ошибку,<br>
      $P_4 = D_1...D_0$ – номер диска, на котором произошла ошибка.
      </td>
    </tr>
    <tr class="table-primary">
      <th scope="row">2</th>
      <td>Формат представления даты в некоторых системах $A_{16}$ включает в себя несколько информационных полей ($Р_1$, $Р_2$ и $Р_3$) и имеет вид:
      <table class="table table-active table-bordered">
        <tbody>
          <tr>
            <td>№ разряда</td>
            <td>15</td>
            <td>14</td>
            <td>13</td>
            <td>12</td>
            <td>11</td>
            <td>10</td>
            <td>09</td>
            <td>08</td>
            <td>07</td>
            <td>06</td>
            <td>05</td>
            <td>04</td>
            <td>03</td>
            <td>02</td>
            <td>01</td>
            <td>00</td>
          </tr>
          <tr>
            <td>Смысл</td>
            <td>$D_4$</td>
            <td>$D_3$</td>
            <td>$D_2$</td>
            <td>$D_1$</td>
            <td>$D_0$</td>
            <td>$M_3$</td>
            <td>$M_2$</td>
            <td>$M_1$</td>
            <td>$M_0$</td>
            <td>$Y_6$</td>
            <td>$Y_5$</td>
            <td>$Y_4$</td>
            <td>$Y_3$</td>
            <td>$Y_2$</td>
            <td>$Y_1$</td>
            <td>$Y_0$</td>
          </tr>
        </tbody>
      </table>
      $P_1 = M_3...M_0$ – месяц (1: "январь", 2: "февраль", ... 12: "декабрь"),<br>
      $P_2 = D_4...D_0$ – день,<br>
      $P_3 = Y_6...Y_0$ – год.
      </td>
    </tr>
    <tr class="table-active">
      <th scope="row">3</th>
      <td>Физический адрес доступа к данным на диске $A_{16}$ включает в себя несколько информационных полей ($Р_1$, $Р_2$ и $Р_3$) и имеет вид:
      <table class="table table-bordered">
        <tbody>
          <tr>
            <td>№ разряда</td>
            <td>15</td>
            <td>14</td>
            <td>13</td>
            <td>12</td>
            <td>11</td>
            <td>10</td>
            <td>09</td>
            <td>08</td>
            <td>07</td>
            <td>06</td>
            <td>05</td>
            <td>04</td>
            <td>03</td>
            <td>02</td>
            <td>01</td>
            <td>00</td>
          </tr>
          <tr>
            <td>Смысл</td>
            <td>$D_1$</td>
            <td>$D_0$</td>
            <td>$0$</td>
            <td>$0$</td>
            <td>$H_6$</td>
            <td>$H_5$</td>
            <td>$H_4$</td>
            <td>$H_3$</td>
            <td>$H_2$</td>
            <td>$H_1$</td>
            <td>$H_0$</td>
            <td>$S_4$</td>
            <td>$S_3$</td>
            <td>$S_2$</td>
            <td>$S_1$</td>
            <td>$S_0$</td>
          </tr>
        </tbody>
      </table>
      $P_1 = D_1D_0$ – номер головки (0: "головка 1", 1: "головка 2", 2: "головка 3", 3: "головка 4"),<br>
      $P_2 = Р_6...Р_0$ – номер дорожки,<br>
      $P_3 = S_4...S_0$ – номер сектора.
      </td>
    </tr>
    <tr class="table-primary">
      <th scope="row">4</th>
      <td>Элемент списка безопасности объекта в некоторой системе $A_{16}$ включает в себя несколько информационных полей ($Р_1$, $Р_2$ и $Р_3$) и имеет вид:
      <table class="table table-active table-bordered">
        <tbody>
          <tr>
            <td>№ разряда</td>
            <td>15</td>
            <td>14</td>
            <td>13</td>
            <td>12</td>
            <td>11</td>
            <td>10</td>
            <td>09</td>
            <td>08</td>
            <td>07</td>
            <td>06</td>
            <td>05</td>
            <td>04</td>
            <td>03</td>
            <td>02</td>
            <td>01</td>
            <td>00</td>
          </tr>
          <tr>
            <td>Смысл</td>
            <td>$1$</td>
            <td>$U_7$</td>
            <td>$U_6$</td>
            <td>$U_5$</td>
            <td>$U_4$</td>
            <td>$U_3$</td>
            <td>$U_2$</td>
            <td>$U_1$</td>
            <td>$U_0$</td>
            <td>$0$</td>
            <td>$0$</td>
            <td>$RW_1$</td>
            <td>$RW_0$</td>
            <td>$X$</td>
            <td>$0$</td>
            <td>$0$</td>
          </tr>
        </tbody>
      </table>
      $P_1 = RW_1RW_0$ – права на чтение и запись объекта (0: "и чтение, и запись запрещены", 1: "разрешено чтение, но запись запрещена", 2: "запрещено чтение, но разрешена перезапись", 3: "и чтение, и запись разрешены"),<br>
      $P_2 = X$ – право на запуск программы,<br>
      $P_3 = U_7...U_0$ – идентификатор пользователя.
      </td>
    </tr>
    <tr class="table-active">
      <th scope="row">5</th>
      <td>Формат команды работы с памятью микроконтроллера $A_{16}$ включает в себя несколько информационных полей ($Р_1$, $Р_2$, и $Р_3$) и имеет вид:
      <table class="table table-bordered">
        <tbody>
          <tr>
            <td>№ разряда</td>
            <td>15</td>
            <td>14</td>
            <td>13</td>
            <td>12</td>
            <td>11</td>
            <td>10</td>
            <td>09</td>
            <td>08</td>
            <td>07</td>
            <td>06</td>
            <td>05</td>
            <td>04</td>
            <td>03</td>
            <td>02</td>
            <td>01</td>
            <td>00</td>
          </tr>
          <tr>
            <td>Смысл</td>
            <td>$B_1$</td>
            <td>$B_0$</td>
            <td>$1$</td>
            <td>$O$</td>
            <td>$0$</td>
            <td>$0$</td>
            <td>$A_8$</td>
            <td>$A_7$</td>
            <td>$A_6$</td>
            <td>$A_5$</td>
            <td>$A_4$</td>
            <td>$A_3$</td>
            <td>$A_2$</td>
            <td>$A_1$</td>
            <td>$A_0$</td>
            <td>$0$</td>
          </tr>
        </tbody>
      </table>
      $P_1 = O$ – тип операции (0: "чтение", 1: "запись"),<br>
      $P_2 = B_1B_0$ – номер банка памяти,<br>
      $P_3 = A_8...A_0$ – адрес ячейки памяти в пределах выбранного банка.
      </td>
    </tr>
    <tr class="table-primary">
      <th scope="row">6</th>
      <td>Формат представления текущего времени в некоторых системах $A_{16}$ включает в себя несколько информационных полей ($Р_1$, $Р_2$ и $Р_3$) и имеет вид:
      <table class="table table-active table-bordered">
        <tbody>
          <tr>
            <td>№ разряда</td>
            <td>15</td>
            <td>14</td>
            <td>13</td>
            <td>12</td>
            <td>11</td>
            <td>10</td>
            <td>09</td>
            <td>08</td>
            <td>07</td>
            <td>06</td>
            <td>05</td>
            <td>04</td>
            <td>03</td>
            <td>02</td>
            <td>01</td>
            <td>00</td>
          </tr>
          <tr>
            <td>Смысл</td>
            <td>$S_4$</td>
            <td>$S_3$</td>
            <td>$S_2$</td>
            <td>$S_1$</td>
            <td>$S_0$</td>
            <td>$M_5$</td>
            <td>$M_4$</td>
            <td>$M_3$</td>
            <td>$M_2$</td>
            <td>$M_1$</td>
            <td>$M_0$</td>
            <td>$H_4$</td>
            <td>$H_3$</td>
            <td>$H_2$</td>
            <td>$H_1$</td>
            <td>$H_0$</td>
          </tr>
        </tbody>
      </table>
      $P_1 = H_4...H_0$ – часы (0: "1 AM", 1: "2 AM", ... 11: "11 AM", 12: "12 AM", 13: "1 PM", 14: "2 PM", ... 24: "12 PM"),<br>
      $P_2 = M_5...M_0$ – минуты,<br>
      $P_3 = S_4...S_0$ – секунды.
      </td>
    </tr>
    <tr class="table-active">
      <th scope="row">7</th>
      <td>Формат информационного пкаета в некоторой системе передачи данных $A_{16}$ включает в себя несколько информационных полей ($Р_1$, $Р_2$ и $Р_3$) и имеет вид:
      <table class="table table-bordered">
        <tbody>
          <tr>
            <td>№ разряда</td>
            <td>15</td>
            <td>14</td>
            <td>13</td>
            <td>12</td>
            <td>11</td>
            <td>10</td>
            <td>09</td>
            <td>08</td>
            <td>07</td>
            <td>06</td>
            <td>05</td>
            <td>04</td>
            <td>03</td>
            <td>02</td>
            <td>01</td>
            <td>00</td>
          </tr>
          <tr>
            <td>Смысл</td>
            <td>$T_2$</td>
            <td>$T_1$</td>
            <td>$T_0$</td>
            <td>$0$</td>
            <td>$S_3$</td>
            <td>$S_2$</td>
            <td>$S_1$</td>
            <td>$S_0$</td>
            <td>$L_7$</td>
            <td>$L_6$</td>
            <td>$L_5$</td>
            <td>$L_4$</td>
            <td>$L_3$</td>
            <td>$L_2$</td>
            <td>$L_1$</td>
            <td>$L_0$</td>
          </tr>
        </tbody>
      </table>
      $P_1 = T_2...T_0$ – тип пакета (0: "первый пакет фрейма", 1...6: "$i$-й пакет фрейма", 7: "последний пакет фрейма"),<br>
      $P_2 = S_3...S_0$ – идентификатор источника,<br>
      $P_3 = L_7...L_0$ – длина пакета.
      </td>
    </tr>
    <tr class="table-primary">
      <th scope="row">8</th>
      <td>Формат регистра управления аналого-цифровым преобразователем микроконтроллера $A_{16}$ включает в себя несколько информационных полей ($Р_1$, $Р_2$, $Р_3$ и $Р_4$) и имеет вид:
      <table class="table table-active table-bordered">
        <tbody>
          <tr>
            <td>№ разряда</td>
            <td>15</td>
            <td>14</td>
            <td>13</td>
            <td>12</td>
            <td>11</td>
            <td>10</td>
            <td>09</td>
            <td>08</td>
            <td>07</td>
            <td>06</td>
            <td>05</td>
            <td>04</td>
            <td>03</td>
            <td>02</td>
            <td>01</td>
            <td>00</td>
          </tr>
          <tr>
            <td>Смысл</td>
            <td>$P$</td>
            <td>$F_7$</td>
            <td>$F_6$</td>
            <td>$F_5$</td>
            <td>$F_4$</td>
            <td>$F_3$</td>
            <td>$F_2$</td>
            <td>$F_1$</td>
            <td>$F_0$</td>
            <td>$1$</td>
            <td>$1$</td>
            <td>$X$</td>
            <td>$0$</td>
            <td>$0$</td>
            <td>$C_1$</td>
            <td>$C_0$</td>
          </tr>
        </tbody>
      </table>
      $P_1 = C_1C_0$ – коэффициент деления тактовой частоты (0: "нет деления", 1: "деление на 2", 2: "деление на 4", 3: "деление на 8"),<br>
      $P_2 = F_7...F_0$ – тактовая частота (в кГц),<br>
      $P_3 = P$ – флаг прерывания аналого-цифрового преобразователя,<br>
      $P_4 = X$ – бит разрешения прерываний от аналого-цифрового преобразователя.
      </td>
    </tr>
    <tr class="table-active">
      <th scope="row">9</th>
      <td>Формат регистра управления сегментом памяти в системе с реальной памятью $A_{16}$ включает в себя несколько информационных полей ($Р_1$, $Р_2$ и $Р_3$) и имеет вид:
      <table class="table table-bordered">
        <tbody>
          <tr>
            <td>№ разряда</td>
            <td>15</td>
            <td>14</td>
            <td>13</td>
            <td>12</td>
            <td>11</td>
            <td>10</td>
            <td>09</td>
            <td>08</td>
            <td>07</td>
            <td>06</td>
            <td>05</td>
            <td>04</td>
            <td>03</td>
            <td>02</td>
            <td>01</td>
            <td>00</td>
          </tr>
          <tr>
            <td>Смысл</td>
            <td>$T_4$</td>
            <td>$T_3$</td>
            <td>$T_2$</td>
            <td>$T_1$</td>
            <td>$T_0$</td>
            <td>$1$</td>
            <td>$A$</td>
            <td>$0$</td>
            <td>$L_7$</td>
            <td>$L_6$</td>
            <td>$L_5$</td>
            <td>$L_4$</td>
            <td>$L_3$</td>
            <td>$L_2$</td>
            <td>$L_1$</td>
            <td>$L_0$</td>
          </tr>
        </tbody>
      </table>
      $P_1 = A$ – признак активности задачи (0: "задача неактивна", 1: "задача активна"),<br>
      $P_2 = T_4...T_0$ – идентификатор задачи,<br>
      $P_3 = L_7...L_0$ – длина сегмента.
      </td>
    </tr>
    <tr class="table-primary">
      <th scope="row">10</th>
      <td>Формат слова состояния устройства ввода/вывода $A_{16}$ включает в себя несколько информационных полей ($Р_1$, $Р_2$ и $Р_3$) и имеет вид:
      <table class="table table-active table-bordered">
        <tbody>
          <tr>
            <td>№ разряда</td>
            <td>15</td>
            <td>14</td>
            <td>13</td>
            <td>12</td>
            <td>11</td>
            <td>10</td>
            <td>09</td>
            <td>08</td>
            <td>07</td>
            <td>06</td>
            <td>05</td>
            <td>04</td>
            <td>03</td>
            <td>02</td>
            <td>01</td>
            <td>00</td>
          </tr>
          <tr>
            <td>Смысл</td>
            <td>$C_4$</td>
            <td>$C_3$</td>
            <td>$C_2$</td>
            <td>$C_1$</td>
            <td>$C_0$</td>
            <td>$0$</td>
            <td>$F_1$</td>
            <td>$F_0$</td>
            <td>$N_7$</td>
            <td>$N_6$</td>
            <td>$N_5$</td>
            <td>$N_4$</td>
            <td>$N_3$</td>
            <td>$N_2$</td>
            <td>$N_1$</td>
            <td>$N_0$</td>
          </tr>
        </tbody>
      </table>
      $P_1 = F_1F_0$ – биты состояния (0: "при предыдущей операции ошибки не произошло и устройство не занято в данный момент", 1: "при предыдущей операции ошибки не произошло и устройство занято", 2: "устройство не занято, но при выполнении предыдущей операции произошла ошибка", 3: "устройство занято и при выполнении предыдущей операции произошла ошибка"),<br>
      $P_2 = C_4...C_0$ – код состояния устройства,<br>
      $P_3 = N_7...N_0$ – количество байт, переданных при предыдущей операции.
      </td>
    </tr>
    <tr class="table-active">
      <th scope="row">11</th>
      <td>Формат команды обмена между содержимым регистра и содержимым памяти некоторого процессора $A_{16}$ включает в себя несколько информационных полей ($Р_1$, $Р_2$, $Р_3$ и $Р_4$) и имеет вид:
      <table class="table table-bordered">
        <tbody>
          <tr>
            <td>№ разряда</td>
            <td>15</td>
            <td>14</td>
            <td>13</td>
            <td>12</td>
            <td>11</td>
            <td>10</td>
            <td>09</td>
            <td>08</td>
            <td>07</td>
            <td>06</td>
            <td>05</td>
            <td>04</td>
            <td>03</td>
            <td>02</td>
            <td>01</td>
            <td>00</td>
          </tr>
          <tr>
            <td>Смысл</td>
            <td>$1$</td>
            <td>$B$</td>
            <td>$I_3$</td>
            <td>$I_2$</td>
            <td>$I_1$</td>
            <td>$I_0$</td>
            <td>$0$</td>
            <td>$R_3$</td>
            <td>$R_2$</td>
            <td>$R_1$</td>
            <td>$R_0$</td>
            <td>$0$</td>
            <td>$S_3$</td>
            <td>$S_2$</td>
            <td>$S_1$</td>
            <td>$S_0$</td>
          </tr>
        </tbody>
      </table>
      $P_1 = B$ – бит, указывающий тип обмена (0: "обмен байтами", 1: "обмен двухбайтовыми словами"),<br>
      $P_2 = S_3...S_0$ – адрес регистра-источника,<br>
      $P_3 = R_3...R_0$ – адрес регистра-получателя, <br>
      $P_4 = I_3...I_0$ – адрес промежуточного регистра.
      </td>
    </tr>
    <tr class="table-primary">
      <th scope="row">12</th>
      <td>Формат двухоперандной команды с сохранением результата во внешнем регистре микроконтроллера $A_{16}$ включает в себя несколько информационных полей ($Р_1$, $Р_2$, $Р_3$ и $Р_4$) и имеет вид:
      <table class="table table-active table-bordered">
        <tbody>
          <tr>
            <td>№ разряда</td>
            <td>15</td>
            <td>14</td>
            <td>13</td>
            <td>12</td>
            <td>11</td>
            <td>10</td>
            <td>09</td>
            <td>08</td>
            <td>07</td>
            <td>06</td>
            <td>05</td>
            <td>04</td>
            <td>03</td>
            <td>02</td>
            <td>01</td>
            <td>00</td>
          </tr>
          <tr>
            <td>Смысл</td>
            <td>$O_2$</td>
            <td>$O_1$</td>
            <td>$O_0$</td>
            <td>$V_3$</td>
            <td>$V_2$</td>
            <td>$V_1$</td>
            <td>$V_0$</td>
            <td>$R_3$</td>
            <td>$R_2$</td>
            <td>$R_1$</td>
            <td>$R_0$</td>
            <td>$S_3$</td>
            <td>$S_2$</td>
            <td>$S_1$</td>
            <td>$S_0$</td>
            <td>$1$</td>
          </tr>
        </tbody>
      </table>
      $P_1 = O_3...O_0$ – код команды (0: "сложение", 1: "вычитание", 2: "логическое И", 3: "логическое ИЛИ", 4: "логическое ИСКЛЮЧАЮЩЕЕ ИЛИ", 5..7: "не используются"),<br>
      $P_2 = V_3...C_0$ – адрес регистра-получателя,<br>
      $P_3 = S_3...S_0$ – адрес регистра-источника 1,<br>
      $P_4 = R_3...R_0$ – адрес регистра-источника 2.
      </td>
    </tr>
   </tbody>
</table>
</div>

<div class="row">
  <div class="col-lg-12">
   <ul class="list-unstyled">
     <li class="float-end">
       <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#бинарные-файлы';">Вверх</button>
     </li>
     <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/TIPiS/labs/lab8.html';">ЛР №8 →</button>
     </li>
     <li>
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/TIPiS/labs/lab6.html';">← ЛР №6</button>
     </li>
   </ul>
  </div>
</div>