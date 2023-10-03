<ol class="breadcrumb">
  <li class="breadcrumb-item active">Главная</li>
</ol>

<div class="progress">
  <div class="progress-bar progress-bar-striped progress-bar-animated"  id="progressbar" role="progressbar" style="width: 25%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
</div>

<p class="text-primary" align="right">↑ семестр</p>

<br>

<div class="row row-cols-1 row-cols-md-2">
<div class="col-lg-4">
  <div class="card bg-light mb-2" style="max-width: 20rem;">
    <div class="card-body">
       <div id="gauge"></div>
    </div>
  </div>
</div>
<div class="col-lg-4">
<div class="card border-primary mb-2" style="max-width: 20rem;">
  <div class="card-body">
  <img src="https://upload.wikimedia.org/wikipedia/commons/8/8a/Kramskoi_Christ_dans_le_d%C3%A9sert.jpg"
        alt="Христос_в_пустыне_(картина_Крамского)"  focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>
</div>
</div>


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
       $('#gauge').dxCircularGauge('instance').value(fl ? 0 : 1);
       fl = !fl;
     },
       500);
       var d = new Date();
       d = (((1+d.getMonth())%7)-2)*25;
       $('#progressbar').attr('aria-valuenow', d).css('width', d + "%");

 });  
 </script>

<br>

<button type="button" class="btn btn-primary btn-lg" onclick="window.location.href='{{ site.baseurl }}/icpc/index.html';">Спортивное программирование</button>

<button type="button" class="btn btn-primary btn-lg" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/index.html';">Искусственный интеллект</button>

<button type="button" class="btn btn-primary btn-lg" onclick="window.location.href='{{ site.baseurl }}/TIPiS/index.html';">Теория информационных процессов и систем</button>

