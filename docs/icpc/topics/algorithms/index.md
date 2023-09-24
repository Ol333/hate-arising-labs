[Главная]({{ site.baseurl }}) >> [Спортивное программирование]({{ site.baseurl }}/icpc/index.html)

# Алгоритмы

Полезно знать.

## Бинарный поиск

Требуется отсортированный массив.

<script>
  $( function() {
    $( "#tabs" ).tabs();
  } );
  </script>
  
<div id="tabs">
  <ul>
    <li><a href="#tabs-1">Смысл</a></li>
    <li><a href="#tabs-2">Анимация</a></li>
    <li><a href="#tabs-3">Python</a></li>
  </ul>
  <div id="tabs-1">
    ![Алгоритм]({{ site.baseurl }}/img/bin_search.xml)
  </div>
  <div id="tabs-2">
    ![Анимированный алгоритм](https://static.tildacdn.com/tild3566-6335-4661-b661-396439326665/binary-and-linear-se.gif)
  </div>
  <div id="tabs-3">
    <!--Код
    ```python
    def f(a, aim):
        left = 0
        right = n-1
        while (left < right)
            middle = (left + right) // 2
            if a[middle] >= aim:
                left = middle
            else:
                right = middle -1
        if a[left] >= aim:
            return a[left]
    ```    -->
      <div class="markdown-body editormd-preview-container" previewcontainer="true" style="padding: 20px;"><pre class="prettyprint linenums prettyprinted" style=""><ol class="linenums"><li class="L0"><code class="lang-python"><span class="pln">    </span><span class="kwd">def</span><span class="pln"> f</span><span class="pun">(</span><span class="pln">a</span><span class="pun">,</span><span class="pln"> aim</span><span class="pun">):</span></code></li><li class="L1"><code class="lang-python"><span class="pln">        left </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span></code></li><li class="L2"><code class="lang-python"><span class="pln">        right </span><span class="pun">=</span><span class="pln"> n</span><span class="pun">-</span><span class="lit">1</span></code></li><li class="L3"><code class="lang-python"><span class="pln">        </span><span class="kwd">while</span><span class="pln"> </span><span class="pun">(</span><span class="pln">left </span><span class="pun">&lt;</span><span class="pln"> right</span><span class="pun">)</span></code></li><li class="L4"><code class="lang-python"><span class="pln">            middle </span><span class="pun">=</span><span class="pln"> </span><span class="pun">(</span><span class="pln">left </span><span class="pun">+</span><span class="pln"> right</span><span class="pun">)</span><span class="pln"> </span><span class="pun">//</span><span class="pln"> </span><span class="lit">2</span></code></li><li class="L5"><code class="lang-python"><span class="pln">            </span><span class="kwd">if</span><span class="pln"> a</span><span class="pun">[</span><span class="pln">middle</span><span class="pun">]</span><span class="pln"> </span><span class="pun">&gt;=</span><span class="pln"> aim</span><span class="pun">:</span></code></li><li class="L6"><code class="lang-python"><span class="pln">                left </span><span class="pun">=</span><span class="pln"> middle</span></code></li><li class="L7"><code class="lang-python"><span class="pln">            </span><span class="kwd">else</span><span class="pun">:</span></code></li><li class="L8"><code class="lang-python"><span class="pln">                right </span><span class="pun">=</span><span class="pln"> middle </span><span class="pun">-</span><span class="lit">1</span></code></li><li class="L9"><code class="lang-python"><span class="pln">        </span><span class="kwd">if</span><span class="pln"> a</span><span class="pun">[</span><span class="pln">left</span><span class="pun">]</span><span class="pln"> </span><span class="pun">&gt;=</span><span class="pln"> aim</span><span class="pun">:</span></code></li><li class="L0"><code class="lang-python"><span class="pln">            </span><span class="kwd">return</span><span class="pln"> a</span><span class="pun">[</span><span class="pln">left</span><span class="pun">]</span></code></li></ol></pre>
        
</div>
  </div>
</div>



|  | Задача |
| :-: |-|
| 🐌 | |
| 🐣  | |
| 🐤  | [91B](https://codeforces.com/problemset/problem/91/B) |
| 🐔 | [2 задача](https://codeforces.com/gym/100881/attachments) (Космическое поселение) |
