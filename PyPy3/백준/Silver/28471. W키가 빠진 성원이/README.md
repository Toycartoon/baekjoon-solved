# [Silver I] W키가 빠진 성원이 - 28471 

[문제 링크](https://www.acmicpc.net/problem/28471) 

### 성능 요약

메모리: 197296 KB, 시간: 1492 ms

### 분류

너비 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2024년 10월 28일 09:05:45

### 문제 설명

<p>성원이는 게임을 너무 열심히 한 나머지 키보드의 W키가 빠져버리게 되었다. 그럼에도 게임이 하고 싶었던 성원이는 W키 없이도 할 수 있는 게임을 찾아 나섰다. 그러다 한 게임을 찾았는데, 보통의 게임에서 WASD를 이용해 캐릭터를 움직이는 것과 달리, 이 게임에서는 <span style="color:#e74c3c;"><code>Q</code></span>, <span style="color:#e74c3c;"><code>W</code></span>, <span style="color:#e74c3c;"><code>E</code></span>, <span style="color:#e74c3c;"><code>A</code></span>, <span style="color:#e74c3c;"><code>D</code></span>, <span style="color:#e74c3c;"><code>Z</code></span>, <span style="color:#e74c3c;"><code>X</code></span>, <span style="color:#e74c3c;"><code>C</code></span> 키를 이용해 $8$방향으로 캐릭터를 움직일 수 있었다. 물론 성원이는 W키를 누르지 못하기 때문에 W키를 제외한 나머지 $7$개의 키만을 이용해 캐릭터를 움직일 수 있다. 각 키를 눌렀을 때 세부적인 이동 방식은 다음과 같다.</p>

<ul>
	<li><span style="color:#e74c3c;"><code>Q</code></span>: 왼쪽 위 대각선으로 $1$칸 이동</li>
	<li><span style="color:#e74c3c;"><code>W</code></span>: 위쪽으로 $1$칸 이동</li>
	<li><span style="color:#e74c3c;"><code>E</code></span>: 오른쪽 위 대각선으로 $1$칸 이동</li>
	<li><span style="color:#e74c3c;"><code>A</code></span>: 왼쪽으로 $1$칸 이동</li>
	<li><span style="color:#e74c3c;"><code>D</code></span>: 오른쪽으로 $1$칸 이동</li>
	<li><span style="color:#e74c3c;"><code>Z</code></span>: 오른쪽 아래 대각선으로 $1$칸 이동</li>
	<li><span style="color:#e74c3c;"><code>X</code></span>: 아래쪽으로 $1$칸 이동</li>
	<li><span style="color:#e74c3c;"><code>C</code></span>: 왼쪽 아래 대각선으로 $1$칸 이동</li>
</ul>

<p>이 게임은 $N\times N$의 게임판 위에서 앞선 $8$방향(성원이의 경우 $7$방향)의 키 조작을 통해 목적지에 도달하는 것이 목표이다. 게임판은 빈 공간이 "<code>.</code>", 이동할 수 없는 공간인 벽이 "<code>#</code>", 목적지가 "<code>F</code>"로 주어진다. 그리고 게임을 시작하기 전에 빈 공간 중 어느 지점에 캐릭터를 둘 지 결정할 수 있다. 단, 벽이나 목적지 위에는 캐릭터를 둘 수 없다. 목적지는 항상 한 개 존재한다.</p>

<pre style="text-align: center;">#.#
.#.
.#<code>F</code></pre>

<p>게임판이 위와 같이 주어졌다고 하면, 성원이는 맨 왼쪽 아래에 캐릭터를 두지만 않는다면 목적지에 도달할 수 있다. 성원이를 위해 목적지에 도달할 수 있도록 하는 시작 지점의 개수를 구해주자.</p>

### 입력 

 <p>첫 번째 줄에 정수 $N$이 주어진다. $(1 \le N \le 2000)$</p>

<p>두 번째 줄부터 $N$개의 줄에 걸쳐 게임판이 주어진다.</p>

### 출력 

 <p>첫 번째 줄에 성원이가 목적지에 도달할 수 있도록 하는 시작 지점의 개수를 출력한다.</p>

