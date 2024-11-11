# [Silver II] binary는 호남선 - 23306 

[문제 링크](https://www.acmicpc.net/problem/23306) 

### 성능 요약

메모리: 13820 KB, 시간: 28 ms

### 분류

애드 혹

### 제출 일자

2024년 11월 1일 15:48:33

### 문제 설명

<blockquote>
<p><em>binary는 호남선~</em></p>

<p><em>num row column char에~</em></p>
</blockquote>

<p><strong>binary는 호남선</strong>은 총 $N$개의 <strong><span style="color:#e74c3c;"><code>0</code></span></strong>과 <strong><span style="color:#e74c3c;"><code>1</code></span></strong>로 표현할 수 있다. <strong><span style="color:#e74c3c;"><code>0</code></span></strong>은 저지대를 지나는 철로를 나타내고, <strong><span style="color:#e74c3c;"><code>1</code></span></strong>은 고지대를 지나는 철로를 나타낸다.</p>

<p><strong>binary는 호남선</strong>의 구간은 연속된 두 개의 철로를 뜻한다. <strong><span style="color:#e74c3c;"><code>01</code></span></strong>은 오르막 구간, <strong><span style="color:#e74c3c;"><code>10</code></span></strong>은 내리막 구간, <strong><span style="color:#e74c3c;"><code>00</code></span></strong>과 <strong><span style="color:#e74c3c;"><code>11</code></span></strong>은 평탄한 구간이다.</p>

<p><strong>binary는 호남선</strong>의 각 구간이 어떤 구간인지 파악하고 상대적 많고 적음을 알아내는 것은, 철로의 유지보수를 위해 매우 중요한 일이다.</p>

### 입력 

 <p><strong>binary는 호남선</strong>의 철로 길이 $N$이 주어진다. ($8 \leq N < 2\ 048$)</p>

### 출력 

 <p>다음을 표준 출력 스트림(stdout)으로 한 줄에 출력하여, 해당 위치의 철로가 무언인지 알아낼 수 있다.</p>

<ul>
	<li><span style="color:#e74c3c;"><code>?</code></span> $k$ : 왼쪽부터 $k$번째 철로를 출력한다. ($1 \leq k \leq N$)</li>
</ul>

<p>각 질문을 출력한 후에는 반드시 표준 출력 버퍼를 <strong>flush</strong> 해야 하고, 표준 입력 스트림(stdin)을 통해 질문에 대한 답을 입력받아야 한다. 그렇지 않으면, <span style="color:#fa7268;">시간 초과</span> 또는 <u>런타임에러</u>를 받는다.</p>

<p>질문하는 $k$의 범위가 철로 구간을 벗어나는 경우, <span style="color:#dd4124;">틀렸습니다</span>를 받는다.</p>

<p>질문은 최대 $\lfloor log_2 N \rfloor$번 할 수 있고, 이보다 더 많이 질문을 하면 <span style="color:#dd4124;">틀렸습니다</span>를 받는다.</p>

<p>최대 $\lfloor log_2 N \rfloor$번의 질문을 이용해, 정답을 아래의 표준 출력 스트림(stdout)을 이용해 한 번만 출력한다.</p>

<ul>
	<li><span style="color:#e74c3c;"><code>!</code></span> $a$ : binary는 호남선에서 오르막 구간의 수가 내리막 구간의 수보다 많다면 <strong><span style="color:#e74c3c;"><code>1</code></span></strong>을, 같다면 <strong><span style="color:#e74c3c;"><code>0</code></span></strong>을, 적다면 <strong><span style="color:#e74c3c;"><code>-1</code></span></strong>을 출력한다.</li>
</ul>

<p>그 후 반드시 표준 출력 버퍼를 <strong>flush</strong>해야 하고, 프로그램을 종료한다. 이것은 질문 횟수에 포함되지 않는다.</p>

