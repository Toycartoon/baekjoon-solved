# [Bronze III] 스티커 나눠주기 - 33868 

[문제 링크](https://www.acmicpc.net/problem/33868) 

### 성능 요약

메모리: 32412 KB, 시간: 40 ms

### 분류

구현

### 제출 일자

2025년 5월 23일 02:30:38

### 문제 설명

<p>제5회 SMUPC를 맞이하여 연재는 대회 참가자에게 숙명여자대학교 '눈송이 프렌즈' 캐릭터 중 하나가 그려진 스티커를 한 개씩 나눠주려고 한다.</p>

<p>스티커를 나눠주는 방법은 아래와 같다.</p>

<ol>
	<li>"<span style="color:#009874;"><strong>맞았습니다!!</strong></span>" 결과를 받은 $N$개의 제출 중 가장 큰 시간 $T$와 가장 짧은 코드 길이 $B$를 찾는다.</li>
	<li>$1$에서 구한 $T$와 $B$를 곱한다.</li>
	<li>$2$에서 구한 값을 눈송이 프렌즈 캐릭터 수인 $7$로 나눈 나머지에 따라 해당하는 캐릭터가 그려진 스티커를 나눠준다.
	<ul>
		<li>나머지가 $0$일 경우: <span style="color:#e74c3c;"><code>튜리</code></span></li>
		<li>나머지가 $1$일 경우: <span style="color:#e74c3c;"><code>눈덩이</code></span></li>
		<li>나머지가 $2$일 경우: <span style="color:#e74c3c;"><code>눈꽃송이</code></span></li>
		<li>나머지가 $3$일 경우: <span style="color:#e74c3c;"><code>로로</code></span></li>
		<li>나머지가 $4$일 경우: <span style="color:#e74c3c;"><code>꽃송이</code></span></li>
		<li>나머지가 $5$일 경우: <span style="color:#e74c3c;"><code>눈송이</code></span></li>
		<li>나머지가 $6$일 경우: <span style="color:#e74c3c;"><code>눈결이</code></span></li>
	</ul>
	</li>
</ol>

<p>연재는 편의상 눈송이 프렌즈 캐릭터를 번호로 관리하려고 한다. <span style="color:#e74c3c;"><code>튜리</code></span>는 $1$번, <span style="color:#e74c3c;"><code>눈덩이</code></span>는 $2$번, <span style="color:#e74c3c;"><code>눈꽃송이</code></span>는 $3$번, <span style="color:#e74c3c;"><code>로로</code></span>는 $4$번, <span style="color:#e74c3c;"><code>꽃송이</code></span>는 $5$번, <span style="color:#e74c3c;"><code>눈송이</code></span>는 $6$번, <span style="color:#e74c3c;"><code>눈결이</code></span>는 $7$번이다.</p>

<p>대회 참가자가 받게 될 스티커에 그려진 캐릭터의 번호를 출력하는 프로그램을 작성하자.</p>

### 입력 

 <p>첫째 줄에 대회 참가자가 "<span style="color:#009874;"><strong>맞았습니다!!</strong></span>" 결과를 받은 제출의 개수 $N$ 이 주어진다. $(1 \leq N \leq 100)$</p>

<p>둘째 줄부터 $N$개의 줄에 걸쳐 제출 코드에 대한 시간 $T$와 코드 길이 $B$가 공백으로 구분되어 주어진다. $(1 \leq T \leq 1\,500; 50 \leq B \leq 5\,000)$</p>

<p>주어지는 입력은 모두 정수이다.</p>

### 출력 

 <p>대회 참가자가 받게 될 스티커에 그려진 캐릭터의 번호를 출력한다.</p>

