# [Bronze I] 랜덤 게임? - 27865 

[문제 링크](https://www.acmicpc.net/problem/27865) 

### 성능 요약

메모리: 30352 KB, 시간: 172 ms

### 분류

구현, 수학, 확률론, 무작위화

### 제출 일자

2023년 7월 30일 22:18:36

### 문제 설명

<p>이 문제는 <strong>인터랙티브</strong> 문제이다.</p>

<p>처음에 인터랙터는 $1$부터 $N$까지 정수 중에서 균등한 확률로 수를 하나를 뽑는다. 질문을 통해 인터랙터가 현재 가지고 있는 수를 맞추면 이 문제를 맞힐 수 있다.</p>

<p>당신은 다음과 같은 질문을 최대 $20\,000$번 할 수 있다.</p>

<ul>
	<li>현재 가지고 있는 수가 $x$인가? $(1\le x\le N)$</li>
</ul>

<p>만약 질문의 답이 '아니오.'라면 인터랙터는 현재 가지고 있는 수를 버리고 새로 수를 뽑는다.</p>

### 입력 

 <p>양의 정수 $N$이 주어진다. $(1 \le N \le 1\,000)$</p>

### 출력 

 <p>다음을 표준 출력 스트림(stdout)으로 한 줄에 출력하여, 인터랙터가 가지고 있는 수가 무엇인지 질문할 수 있다.</p>

<ul>
	<li><span style="color:#e74c3c;"><code>? x</code></span> : 현재 인터랙터가 가지고 있는 수가 $x$인지 확인한다. $(1\le x\le N)$</li>
</ul>

<p>질문을 한 뒤, 당신은 인터랙터에게서 문자 하나를 입력받아서 질문의 답을 알 수 있다.</p>

<ul>
	<li><span style="color:#e74c3c;"><code>Y</code></span> : 현재 인터랙터가 가지고 있는 수는 $x$와 같다.</li>
	<li><span style="color:#e74c3c;"><code>N</code></span> : 현재 인터랙터가 가지고 있는 수는 $x$와 다르다. 이후 인터랙터는 현재 가지고 있는 수를 버리고 새로 수를 뽑는다. 수를 뽑을 때는 질문의 답을 참고하지 않고 $1$부터 $N$까지 정수 중에서 균등한 확률로 수를 하나를 뽑는다.</li>
</ul>

<p>질문을 한 후에는 반드시 표준 출력 버퍼를 flush 해야 하고, 표준 입력 스트림(stdin)을 통해 질문에 대한 답을 입력받아야 한다. 그렇지 않으면, <strong><span style="color:#fa7268;">시간 초과</span></strong> 또는 <strong><span style="color:#8d6bd8;">런타임 에러</span></strong>를 받는다. 범위를 벗어난 $x$값을 질문하거나 잘못된 형식으로 질문하면 <span style="color:#e74c3c;"><strong>틀렸습니다</strong></span>를 받는다. 또한 $20\,000$회 넘게 질문을 하면 <span style="color:#e74c3c;"><strong>틀렸습니다</strong></span>를 받는다.</p>

<p>만약 인터랙터가 현재 가지고 있는 수를 알아낸 경우, 표준 출력 스트림으로 다음 한 줄을 출력한다.</p>

<ul>
	<li><span style="color:#e74c3c;"><code>! y</code></span> : 현재 인터랙터가 가지고 있는 수는 $y$이다.</li>
</ul>

<p>답을 출력한 이후에는 표준 출력 버퍼를 비우고 프로그램을 바로 종료하여야 한다. 그렇지 않으면 예상하지 못한 채점 결과를 받을 수 있다.</p>

<p>각 언어별로 표준 출력 버퍼를 flush하는 방법은 다음과 같다.</p>

<ul>
	<li>C: <code>fflush(stdout)</code></li>
	<li>C++: <code>std::cout << std::flush</code></li>
	<li>Java: <code>System.out.flush()</code></li>
	<li>Python: <code>sys.stdout.flush()</code></li>
</ul>

