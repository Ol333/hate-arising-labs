<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/OOP/index.html">ООП</a></li>
  <li class="breadcrumb-item active">ЛР №3</li>
</ol>

# Объектно-ориентированное проектирование

Пример:

{% tabs example %}

{% tab example Описание %}
One Ring to rule them all.
{% endtab %}

{% tab example UML %}
<div class="card border-primary mb-2" style="max-width: 30rem;">
  <div class="card-body">
    <img src="{{ site.baseurl }}/img/oop_3lab.svg"
        alt="Диаграмма классов"  focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>
{% endtab %}

{% tab example class Ring %}

``` csharp
class Ring
{
    private Someone[] all;
    private static Ring instance;
    private Ring() 
    {
        all = new Someone[]{new Someone(), new Someone(), new Someone(), new Someone(), new Someone(), new Someone(), new Someone(), new Someone(), new Someone(),
                new Someone(), new Someone(), new Someone(), new Someone(), new Someone(), new Someone(), new Someone(),
                new Someone(), new Someone(), new Someone()};
    }

    public static Ring getInstance()
    {
        if (instance == null)
            instance = new Ring();
        return instance;
    }
    public void toRule(string s)
    {
        foreach (var person in all)
        {
            person.getRuled(s.Split(':')[1]);
        }
    }

    public string getFirstMinionWill()
    {
        return all[0].getState();
    }
}
```
{% endtab %}

{% tab example class Someone %}

``` csharp
class Someone
{
    private string will = "free will";
    private string aim = "doing something neutral";

    public void getRuled(string s)
    {
        will = "not free will";
        aim = s;
    }

    public string getState()
    {
        return "This Someone have " + will + " and will " + aim;
    }
}
```
{% endtab %}

{% tab example Main %}

``` csharp
Ring ring = Ring.getInstance();
Console.WriteLine(ring.getFirstMinionWill());

ring.toRule("Dark Lord's will: retrieve the Ring!");
Console.WriteLine(ring.getFirstMinionWill());
```
{% endtab %}

{% tab example Результат %}

``` console
This Someone have free will and will doing something neutral
This Someone have not free will and will  retrieve the Ring!
```
{% endtab %}

{% endtabs %}


# Задание

## Приемлемо

* По словесному описанию составить UML диаграмму классов (все существительные должны превратиться в классы или поля классов, глаголы - в методы).
* Реализовать в коде спроектированные классы.
* Реализовать описанный текстом сценарий взаимодействия объектов в основном теле программы.

___

## Выше ожидаемого

* Отобразить сценарий на UML диаграмме последовательностей.

___

## Превосходно

* Оформить классы в виде пользовательской библиотеки, подключаемой к проекту.

<div class="table-responsive">
<table class="table table-hover border-primary  table-bordered">
  <thead>
    <tr class="table-dark">
      <th scope="col">№ варианта</th>
      <th scope="col">Текст (из Вредных советов Григория Остера)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>Потерявшийся ребёнок<br>
Должен помнить, что его<br>
Отведут домой, как только<br>
Назовёт он адрес свой.<br>
Надо действовать умнее,<br>
Говорите: «Я живу<br>
Возле пальмы с обезьяной<br>
На далёких островах».<br>
Потерявшийся ребёнок,<br>
Если он не дурачок,<br>
Не упустит верный случай<br>
В разных странах побывать.</td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>Кто не прыгал из окошка<br>
Вместе с маминым зонтом,<br>
Тот лихим парашютистом<br>
Не считается пока.<br>
Не лететь ему, как птице,<br>
Над взволнованной толпой,<br>
Не лежать ему в больнице<br>
С забинтованной ногой.</td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td>Если вас поймала мама<br>
За любимым делом вашим,<br>
Например, за рисованьем<br>
В коридоре на обоях,<br>
Объясните ей, что это –<br>
Ваш сюрприз к Восьмому марта.<br>
Называется картина:<br>
«Милой мамочки портрет».</td>
    </tr>
    <tr>
      <th scope="row">4</th>
      <td>Никогда вопросов глупых<br>
Сам себе не задавай,<br>
А не то ещё глупее<br>
Ты найдёшь на них ответ.<br>
Если глупые вопросы<br>
Появились в голове,<br>
Задавай их сразу взрослым.<br>
Пусть у них трещат мозги.</td>
    </tr>
    <tr>
      <th scope="row">5</th>
      <td>Посещайте почаще<br>
Театральный буфет.<br>
Там пирожные с кремом,<br>
С пузырьками вода.<br>
Как дрова на тарелках<br>
Шоколадки лежат,<br>
И сквозь трубочку можно<br>
Пить молочный коктейль.<br>
Не просите билеты<br>
На балкон и в партер,<br>
Пусть дадут вам билеты<br>
В театральный буфет.<br>
Уходя из театра,<br>
Унесёте с собой<br>
Под трепещущим сердцем,<br>
В животе, бутерброд.</td>
    </tr>
    <tr>
      <th scope="row">6</th>
      <td>Если вы по коридору<br>
Мчитесь на велосипеде,<br>
А навстречу вам из ванной<br>
Вышел папа погулять,<br>
Не сворачивайте в кухню,<br>
В кухне – твёрдый холодильник.<br>
Тормозите лучше в папу.<br>
Папа мягкий. Он простит.</td>
    </tr>
    <tr>
      <th scope="row">7</th>
      <td>Главным делом жизни вашей<br>
Может стать любой пустяк.<br>
Надо только твёрдо верить,<br>
Что важнее дела нет.<br>
И тогда не помешает<br>
Вам ни холод, ни жара,<br>
Задыхаясь от восторга,<br>
Заниматься чепухой.</td>
    </tr>
    <tr>
      <th scope="row">8</th>
      <td>Бейте палками лягушек.<br>
Это очень интересно.<br>
Отрывайте крылья мухам,<br>
Пусть побегают пешком.<br>
Тренируйтесь ежедневно,<br>
И наступит день счастливый –<br>
Вас в какое-нибудь царство<br>
Примут главным палачом.</td>
    </tr>
    <tr>
      <th scope="row">9</th>
      <td>Если вы собрались другу<br>
Рассказать свою беду,<br>
Брать за пуговицу друга<br>
Бесполезно – убежит,<br>
И на память вам оставит<br>
Эту пуговицу друг.<br>
Лучше дать ему подножку,<br>
На пол бросить, сверху сесть<br>
И тогда уже подробно<br>
Рассказать свою беду.</td>
    </tr>
    <tr>
      <th scope="row">10</th>
      <td>Если ты пришёл к знакомым,<br>
Не здоровайся ни с кем.<br>
Слов: «пожалуйста», «спасибо»<br>
Никому не говори.<br>
Отвернись и на вопросы<br>
Ни на чьи не отвечай.<br>
И тогда никто не скажет<br>
Про тебя, что ты болтун.</td>
    </tr>
    <tr>
      <th scope="row">11</th>
      <td>Если ты пришёл на ёлку,<br>
Свой подарок требуй сразу,<br>
Да гляди, чтоб ни конфеты<br>
Не зажилил Дед Мороз.<br>
И не вздумай беззаботно<br>
Приносить домой остатки.<br>
Как наскачут папа с мамой –<br>
Половину отберут.</td>
    </tr>
    <tr>
      <th scope="row">12</th>
      <td>Возьми густой вишнёвый сок<br>
И белый мамин плащ.<br>
Лей аккуратно сок на плащ –<br>
Появится пятно.<br>
Теперь, чтоб не было пятна<br>
На мамином плаще,<br>
Плащ надо сунуть целиком<br>
В густой вишнёвый сок.<br>
Возьми вишнёвый мамин плащ<br>
И кружку молока.<br>
Лей аккуратно молоко –<br>
Появится пятно.<br>
Теперь, чтоб не было пятна<br>
На мамином плаще,<br>
Плащ надо сунуть целиком<br>
В кастрюлю с молоком.<br>
Возьми густой вишнёвый сок<br>
И белый мамин плащ.<br>
Лей аккуратно…</td>
    </tr>
   </tbody>
</table>
</div>

<div class="row">
  <div class="col-lg-12">
   <ul class="list-unstyled">
     <li class="float-end">
       <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#экспертные-оценки';">Вверх</button>
     </li>
     <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/OOP/labs/lab4.html';">ЛР №4 →</button>
     </li>
     <li>
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/OOP/labs/lab2.html';">← ЛР №2</button>
     </li>
   </ul>
  </div>
</div>
