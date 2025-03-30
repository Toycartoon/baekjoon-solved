# [Silver I] Hotel - 29634 

[문제 링크](https://www.acmicpc.net/problem/29634) 

### 성능 요약

메모리: 34976 KB, 시간: 56 ms

### 분류

너비 우선 탐색, 깊이 우선 탐색, 플러드 필, 그래프 이론, 그래프 탐색

### 제출 일자

2025년 3월 30일 22:56:26

### 문제 설명

<p>Pavel was dreaming to become an architect since his early childhood. He often drew plans of buildings on sheets of paper, and sometimes on tables and walls. Now he has a university degree and is a famous architect.</p>

<p>Once Pavel was digging in his child drawings and found an interesting plan of the hotel floor. The floor is a rectangle with size $n \times m$ meters. On the plan, each square corresponding to a square meter of the floor was painted with either blue or red color. After thinking a little, Pavel understood that the blue color is for corridors, and the red color stands for hotel rooms. </p>

<p>Since his childhood, Pavel tries to comply with international standards. Following the standards, a hotel room must be rectangular, so it should be represented on the plan as a rectangle filled with red color. Sides of the room should be parallel to the floor boundaries. Moreover, there is always a corridor running along each side of each hotel room.</p>

<p>In order to comply with the fire safety regulations, there should be corridors at the sides of the floor. So, the first and the last rows, as well as the first and the last columns of the plan are blue.</p>

<p>Looking at his plan, Pavel wondered, what is the maximal area of a hotel room on his plan. Write a program to find this area.</p>

### 입력 

 <p>The input file contains the description of Pavel's plan.</p>

<p>The first line of the input file contain two integers $n$ and $m$ ($3 \le n, m \le 30$). The following $n$ lines contain $m$ symbols each. The symbol "<code>*</code>" corresponds to a square filled with blue color (a square meter of a corridor), and the symbol "<code>.</code>" is a red square --- a square meter of a room.</p>

### 출력 

 <p>In the first line of the output file print the area of the largest hotel room. If there are no rooms on the plan, print "<code>-1</code>".</p>

