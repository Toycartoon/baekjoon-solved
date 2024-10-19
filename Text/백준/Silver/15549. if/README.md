# [Silver V] if - 15549 

[문제 링크](https://www.acmicpc.net/problem/15549) 

### 성능 요약

메모리: 4528 KB, 시간: 0 ms

### 분류

애드 혹

### 제출 일자

2024년 10월 20일 03:09:22

### 문제 설명

<p>다음 프로그램을 실행시켰을 때, "<code>true</code>"를 출력하는 변수 <code>x</code>의 자료형과 값을 찾는 프로그램을 작성하시오.</p>

<div><div id="highlighter_493738" class="syntaxhighlighter  java"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div><div class="line number3 index2 alt2">3</div><div class="line number4 index3 alt1">4</div><div class="line number5 index4 alt2">5</div><div class="line number6 index5 alt1">6</div><div class="line number7 index6 alt2">7</div><div class="line number8 index7 alt1">8</div><div class="line number9 index8 alt2">9</div><div class="line number10 index9 alt1">10</div><div class="line number11 index10 alt2">11</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="java keyword">import</code> <code class="java plain">java.util.*;</code></div><div class="line number2 index1 alt1"><code class="java keyword">public</code> <code class="java keyword">class</code> <code class="java plain">Main {</code></div><div class="line number3 index2 alt2"><code class="java spaces">    </code><code class="java keyword">public</code> <code class="java keyword">static</code> <code class="java keyword">void</code> <code class="java plain">main(String[] args) {</code></div><div class="line number4 index3 alt1"><code class="java spaces">        </code><code class="java plain">??? x = ???;</code></div><div class="line number5 index4 alt2"><code class="java spaces">        </code><code class="java keyword">if</code> <code class="java plain">(x != </code><code class="java value">0</code> <code class="java plain">&& x == -x) {</code></div><div class="line number6 index5 alt1"><code class="java spaces">            </code><code class="java plain">System.out.println(</code><code class="java string">"true"</code><code class="java plain">);</code></div><div class="line number7 index6 alt2"><code class="java spaces">        </code><code class="java plain">} </code><code class="java keyword">else</code> <code class="java plain">{</code></div><div class="line number8 index7 alt1"><code class="java spaces">            </code><code class="java plain">System.out.println(</code><code class="java string">"false"</code><code class="java plain">);</code></div><div class="line number9 index8 alt2"><code class="java spaces">        </code><code class="java plain">}</code></div><div class="line number10 index9 alt1"><code class="java spaces">    </code><code class="java plain">}</code></div><div class="line number11 index10 alt2"><code class="java plain">}</code></div></div></td></tr></tbody></table></div></div>

<p>실행 환경은 BOJ 채점 서버의 Java 실행 환경과 같다.</p>

### 입력 

 <p>입력은 없다.</p>

### 출력 

 <p>첫째 줄에 변수 <code>x</code>의 자료형과 값을 공백으로 구분해 출력한다. 자료형은 <code>int</code>와 <code>long</code>만 가능하다. 출력한 값이 자료형에 알맞지 않은 경우에는 틀리게 된다.</p>

<p>값은 아래 소스가 런타임 에러 없이 읽을 수 있는 값을 의미한다.</p>

<div><div id="highlighter_772046" class="syntaxhighlighter  java"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div><div class="line number3 index2 alt2">3</div><div class="line number4 index3 alt1">4</div><div class="line number5 index4 alt2">5</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="java plain">String val = </code><code class="java string">"유저가 출력한 값"</code><code class="java plain">;</code></div><div class="line number2 index1 alt1"><code class="java comments">// int의 경우</code></div><div class="line number3 index2 alt2"><code class="java keyword">int</code> <code class="java plain">temp = Integer.parseInt(val);</code></div><div class="line number4 index3 alt1"><code class="java comments">// long의 경우</code></div><div class="line number5 index4 alt2"><code class="java keyword">long</code> <code class="java plain">temp = Long.parseLong(val);</code></div></div></td></tr></tbody></table></div></div>

