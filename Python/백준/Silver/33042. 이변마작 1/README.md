# [Silver IV] 이변마작 1 - 33042 

[문제 링크](https://www.acmicpc.net/problem/33042) 

### 성능 요약

메모리: 32412 KB, 시간: 32 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 구현, 트리를 사용한 집합과 맵

### 제출 일자

2024년 12월 28일 14:17:59

### 문제 설명

<p>마작의 <strong>패</strong><sup>牌</sup>는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c34"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>34</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$34$</span></mjx-container>종류의 패가 각각 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c34"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$4$</span></mjx-container>장씩, 총 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c36"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>136</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$136$</span></mjx-container>장으로 이루어져 있습니다. 패의 종류는 다음과 같습니다.</p>

<table class="table table-bordered">
	<thead>
		<tr>
			<th scope="col">모양</th>
			<th scope="col">이름</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><img alt="" src="https://upload.acmicpc.net/8b398835-395f-42b9-b41e-d987003f58c5/-/preview/" style="vertical-align: middle; height: 3em; display: inline-block;" class="no-responsive"></td>
			<td>만수패<sup>萬數牌</sup></td>
		</tr>
		<tr>
			<td colspan="2">패에 쓰여 있는 한자에 따라 <code><span style="color:#e74c3c;">1m</span></code>, <code><span style="color:#e74c3c;">2m</span></code>, <code><span style="color:#e74c3c;">3m</span></code>, <code><span style="color:#e74c3c;">4m</span></code>, <code><span style="color:#e74c3c;">5m</span></code>, <code><span style="color:#e74c3c;">6m</span></code>, <code><span style="color:#e74c3c;">7m</span></code>, <code><span style="color:#e74c3c;">8m</span></code>, <code><span style="color:#e74c3c;">9m</span></code>으로 총 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$9$</span></mjx-container>개의 종류가 있습니다.</td>
		</tr>
		<tr>
			<td><img alt="" src="https://upload.acmicpc.net/2c88822d-aa08-4291-bd78-66d5249a6ad2/-/preview/" style="vertical-align: middle; height: 3em; display: inline-block;" class="no-responsive"></td>
			<td>통수패<sup>筒數牌</sup></td>
		</tr>
		<tr>
			<td colspan="2">패에 그려져 있는 바퀴의 개수에 따라 <code><span style="color:#e74c3c;">1p</span></code>, <code><span style="color:#e74c3c;">2p</span></code>, <code><span style="color:#e74c3c;">3p</span></code>, <code><span style="color:#e74c3c;">4p</span></code>, <code><span style="color:#e74c3c;">5p</span></code>, <code><span style="color:#e74c3c;">6p</span></code>, <code><span style="color:#e74c3c;">7p</span></code>, <code><span style="color:#e74c3c;">8p</span></code>, <code><span style="color:#e74c3c;">9p</span></code>로 총 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$9$</span></mjx-container>개의 종류가 있습니다.</td>
		</tr>
		<tr>
			<td><img alt="" src="https://upload.acmicpc.net/4639715a-cda5-43ec-8468-1b3b935fe1b0/-/preview/" style="vertical-align: middle; height: 3em; display: inline-block;" class="no-responsive"></td>
			<td>삭수패<sup>索數牌</sup></td>
		</tr>
		<tr>
			<td colspan="2">패에 그려져 있는 대나무의 개수에 따라 <code><span style="color:#e74c3c;">1s</span></code>, <code><span style="color:#e74c3c;">2s</span></code>, <code><span style="color:#e74c3c;">3s</span></code>, <code><span style="color:#e74c3c;">4s</span></code>, <code><span style="color:#e74c3c;">5s</span></code>, <code><span style="color:#e74c3c;">6s</span></code>, <code><span style="color:#e74c3c;">7s</span></code>, <code><span style="color:#e74c3c;">8s</span></code>, <code><span style="color:#e74c3c;">9s</span></code>로 총 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$9$</span></mjx-container>개의 종류가 있습니다.</td>
		</tr>
		<tr>
			<td><img alt="" src="https://upload.acmicpc.net/f76768b7-f471-42a5-84ca-72f413db5363/-/preview/" style="vertical-align: middle; height: 3em; display: inline-block;" class="no-responsive"></td>
			<td>자패<sup>字牌</sup></td>
		</tr>
		<tr>
			<td colspan="2">패에 쓰여 있는 글자의 종류에 따라 <code><span style="color:#e74c3c;">1z</span></code>, <code><span style="color:#e74c3c;">2z</span></code>, <code><span style="color:#e74c3c;">3z</span></code>, <code><span style="color:#e74c3c;">4z</span></code>, <code><span style="color:#e74c3c;">5z</span></code>, <code><span style="color:#e74c3c;">6z</span></code>, <code><span style="color:#e74c3c;">7z</span></code>로 총 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c37"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$7$</span></mjx-container>개의 종류가 있습니다.</td>
		</tr>
	</tbody>
</table>

<p>여러분은 마작패의 모양을 익히기 위해 마작패를 섞어 하나씩 놓아보고 있습니다. 하지만 여러분이 아직 모르고 있는 사실이 하나 있습니다. 바로 마작패들에 <strong>이변</strong>이 일어나고 있다는 것입니다.</p>

<p>마작에는 같은 종류의 패가 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c34"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$4$</span></mjx-container>장씩 존재하지만, 이변이 일어난 마작패는 종류가 바뀌기 때문에 경우에 따라서는 같은 종류의 패가 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$5$</span></mjx-container>장 이상이 되는 것도 가능합니다.</p>

<p>여러분은 마작패를 늘어놓다가 같은 마작패가 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$5$</span></mjx-container>장 이상 나왔을 때 이변을 눈치채고 해결해야 합니다. 이변을 눈치챌 수 있는 시점을 구해 주세요.</p>

### 입력 

 <p>첫 번째 줄에 늘어놓을 마작패의 개수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어집니다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c36"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>136</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(1 \le N \le 136)$</span> </mjx-container></p>

<p>두 번째 줄에 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>장의 마작패의 종류가 놓아볼 순서대로 공백으로 구분되어 주어집니다. 입력으로 주어지는 모든 마작패는 위에서 설명한 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c34"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>34</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$34$</span></mjx-container>종 중 하나입니다.</p>

### 출력 

 <p><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$i$</span></mjx-container>번째 패를 놓은 이후에 이변을 눈치챌 수 있다면 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$i$</span></mjx-container>를 출력합니다. 패를 끝까지 늘어놓아도 이변을 눈치채지 못한다면, 대신 <code><span style="color:#e74c3c;">0</span></code>을 출력합니다.</p>

