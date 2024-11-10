# [Gold II] Japan Plotter Driver - 6677 

[문제 링크](https://www.acmicpc.net/problem/6677) 

### 성능 요약

메모리: 31120 KB, 시간: 36 ms

### 분류

구현

### 제출 일자

2024년 11월 10일 17:05:35

### 문제 설명

<p>The Japan company you are working for produce plotter devices that can draw nice pictures. To support customers who do not posses the special hardware, you were asked to write an emulation driver that simulates the work of the plotter and prints the picture on a computer screen.</p>

<p>The plotter is driven with a simple language consisting of several drawing commands:</p>

<ul>
	<li><code>POINT x y</code> -- makes a little circle at the given coordinates.</li>
	<li><code>TEXT x y txt</code> -- displays a line of text at the given coordinates.</li>
	<li><code>LINE x1 y1 x2 y2</code> -- draws a line between the specified points.</li>
	<li><code>CLEAR x1 y1 x2 y2</code> -- erases the given rectangle.</li>
	<li><code>PRINT</code> -- prints an output page and terminates the current job.</li>
</ul>

<p>The emulation driver uses few ASCII characters to represent the picture, one character being a basic unit of the coordinate system. The top-left character has coordinates (1,1). The X-axis aims to the right, the Y-axis goes down.</p>

<p>The particular commands are emulated as follows:</p>

<ul>
	<li><strong>POINT</strong>: The driver puts a lowercase letter "o" at the given coordinates.</li>
	<li><strong>TEXT</strong>: Shows a single line of text, the first character is positioned at the given coordinates and the text always goes right.</li>
	<li><strong>LINE</strong>: Simulates a straight line between two points. The line is formed by one of the following characters: dash ("-"), pipe ("|"), slash ("/"), or backslash ("\"), according to its direction.</li>
	<li><strong>CLEAR</strong>: The driver fills the appropriate rectangular area with spaces, including the bounding rows and columns.</li>
	<li><strong>PRINT</strong>: This command causes the driver to print the picture surrounded with a nice frame made of plus ("+"), minus ("-"), and pipe ("|") characters.</li>
</ul>

<p>If more objects should be drawn across a single character, the following rules apply:</p>

<ul>
	<li>If the same character is drawn several times, it is used without a change.</li>
	<li>If only pipe and minus characters are involved, they result in the plus sign ("+").</li>
	<li>If only slashes and backslashes are involved, the result is the lowercase letter "x".</li>
	<li>Otherwise, the asterisk ("*") is displayed.</li>
</ul>

<p>Before a script is given to the driver, it is checked by a special preprocessor, which rejects all invalid commands. Therefore, you may assume that all coordinates are within the range of the page. Also, with the LINE command, the two points are always different and the line is strictly either vertical, horizontal, or at the angle of 45o to the axes. There is no assumption on the relative position of the points used with the LINE and CLEAR commands. The text in the TEXT command is always composed only of uppercase letter and digits.</p>

### 입력 

 <p>The input consists of several scripts. Each script begins with a line containing two integers X and Y, separated with space, 1 <= X, Y <= 75. These numbers specify the dimensions of the page. Every other line contains exactly one of the above commands. The commands are always uppercase, command arguments are separated with one space.</p>

<p>The PRINT command is always the last command of the script. After the PRINT command, a new script begins. The input is terminated with two zeros, which are not considered to be a script.</p>

### 출력 

 <p>For each script, output the emulated picture, created as specified above. After the picture, print one blank line.</p>

<p> </p>

