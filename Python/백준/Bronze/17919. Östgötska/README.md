# [Bronze II] Östgötska - 17919 

[문제 링크](https://www.acmicpc.net/problem/17919) 

### 성능 요약

메모리: 32412 KB, 시간: 32 ms

### 분류

구현, 문자열

### 제출 일자

2024년 12월 26일 00:53:05

### 문제 설명

<p>Anders talks in the Swedish dialect of <em>östgötska</em>. Unfortunately, this makes it somewhat hard to get a programming job in the Swedish capital of Stockholm. The trendy Stockholm hipsters only accept applicants speaking the standard Swedish dialect, <em>rikssvenska</em>.</p>

<p>To increase his chances of passing interviews, he wishes to practice talking rikssvenska. To help him with this, he wants you to write a program that can determine whenever he accidentally reverts to speaking östgötska.</p>

<p>A simple way of determining if a sentence is written in östgötska is if at least <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c34"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mi class="mjx-n"><mjx-c class="mjx-c25"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn><mi mathvariant="normal">%</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$40\%$</span></mjx-container> of the words in the sentence contains the letter <code>ä</code>. For simplicity, this is encoded as the letter combination <code>ae</code> (meaning any appearance of the substring \texttt{ae} is to be regarded as an occurrence of the letter <code>ä</code>).</p>

### 입력 

 <p>The first and only line of input contains a sequence of space-separated words. Each word consists only of letters <code>a-z</code>. There are at most <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$100$</span></mjx-container> words, and each word contains at most <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$15$</span></mjx-container> letters <code>a-z</code> (meaning that the <code>ae</code> combination counts as two letters for this limit).</p>

### 출력 

 <p>Output "<code>dae ae ju traeligt va"</code> if the input sentence is in östgötska, otherwise output "<code>haer talar vi rikssvenska</code>".</p>

