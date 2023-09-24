[Главная]({{ site.baseurl }}) >> [Спортивное программирование]({{ site.baseurl }}/icpc/index.html)

# Сортировки

Надо знать.

# <a id="quick_sort">Быстрая сортировка</a>

<script>
  $(() => {
   const gauge = $('#gauge').dxCircularGauge({
    scale: {
      startValue: 0,
      endValue: 10,
      tick: {
        color: '#9c9c9c',
      },
      minorTick: {
        color: '#9c9c9c',
        visible: true,
      },
      tickInterval: 0.5,
      minorTickInterval: 0.25,
    },
    rangeContainer: {
      backgroundColor: 'none',
    },
    title: {
      text: 'Скорость сдачи лаб (шт./сут.)',
      font: { size: 28 },
    },
    value: 0,
  });
    fl = false;
    setInterval(() => {
      gauge.value(fl ? 0 : 1);
      fl = !fl;
    },
      500);
  
});  
</script>
<div id="gauge"></div>

