# [Bronze III] 아카라카 2 - 32652 

[문제 링크](https://www.acmicpc.net/problem/32652) 

### 성능 요약

메모리: 31120 KB, 시간: 32 ms

### 분류

해 구성하기, 문자열

### 제출 일자

2024년 11월 13일 20:25:17

### 문제 설명

<blockquote>
<p><em>아카라카!</em></p>

<p><em>아카라카(아라)칭 아카라카(아라)쵸 아카라카(아라) 칭칭</em></p>

<p><em>쵸쵸쵸 랄랄라 시스붐바 연세 선수 라플라</em></p>

<p><em>헤이 연세 야!</em></p>
</blockquote>

<p><strong>AKARAKA</strong>(아카라카)는 컴퓨터 과학적 관점으로 바라봤을 때, 튜링도 기립 박수를 치고 갈 가히 최고의 구호라 할 수 있다. <strong>AKARAKA</strong>는 그 자체로도 팰린드롬이고, 접두사이자 접미사인 <strong>AKA</strong> 또한 팰린드롬이기 때문이다. 여기서 팰린드롬은 거꾸로 읽어도 같은 문자열을 뜻한다.</p>

<p>형진이는 <strong>AKARAKA</strong>가 최대한 많이 보이는 문자열을 만들고 싶어졌다. <strong>AKARAKA</strong>가 연속 부분 문자열로 정확히 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$K$</span></mjx-container>번 등장하는 문자열들 중 가장 짧은 문자열을 만들어보자. 그러한 문자열이 존재하며 유일함을 증명할 수 있다.</p>

### 입력 

 <p>첫 번째 줄에 양의 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$K$</span></mjx-container>가 입력으로 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>1</mn><mo>≤</mo><mi>K</mi><mo>≤</mo><mn>50</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(1 \le K \le 50)$</span> </mjx-container></p>

### 출력 

 <p>첫 번째 줄에 길이가 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c37"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$7$</span></mjx-container>인 모든 연속 부분 문자열 중 <strong>AKARAKA</strong>가 정확히 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$K$</span></mjx-container>번 나타나는 가장 짧은 문자열을 출력한다.</p>

