# [Gold IV] Bank Queue - 11199 

[문제 링크](https://www.acmicpc.net/problem/11199) 

### 성능 요약

메모리: 35508 KB, 시간: 288 ms

### 분류

자료 구조, 그리디 알고리즘, 우선순위 큐

### 제출 일자

2025년 4월 4일 01:23:54

### 문제 설명

<p>Oliver is a manager of a bank near KTH and wants to close soon. There are many people standing in the queue wanting to put cash into their accounts after they heard that the bank increased the interest rates by 42% (from 0.01% per year to 0.0142% per year).</p>

<p>However, there are too many people and only one counter is open which can serve one person per minute. Greedy as Oliver is, he would like to select some people in the queue, so that the total amount of cash stored by these people is as big as possible and that money then can work for the bank overnight.</p>

<p>There is a problem, though. Some people don’t have the time to wait until the bank closes because they have to run somewhere else, so they have to be served before a certain time, after which they just leave. Oliver also turned off the infrared door sensor outside the bank, so that no more people can enter, because it’s already too crowded in the hall.</p>

<p>Help Oliver calculate how much cash he can get from the people currently standing in the queue before the bank closes by serving at most one person per minute.</p>

### 입력 

 <p>The first line of input contains two integers N (1 ≤ N ≤ 10 000) and T (1 ≤ T ≤ 47), the number of people in the queue and the time in minutes until Oliver closes the bank. Then follow N lines, each with 2 integers c<sub>i</sub> and t<sub>i</sub>, denoting the amount of cash in Swedish crowns person i has and the time in minutes from now after which person i leaves if not served. Note that it takes one minute to serve a person and you must begin serving a person at time ti at the latest. You can assume that 1 ≤ c<sub>i</sub> ≤ 100 000 and 0 ≤ t<sub>i</sub> < T.</p>

### 출력 

 <p>Output one line with the maximum amount of money you can get from the people in the queue before the bank closes.</p>

