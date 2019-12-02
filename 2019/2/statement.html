<article class="day-desc"><h2>--- Day 2: 1202 Program Alarm ---</h2><p>On the way to your <a href="https://en.wikipedia.org/wiki/Gravity_assist">gravity assist</a> around the Moon, your ship computer beeps angrily about a "<a href="https://www.hq.nasa.gov/alsj/a11/a11.landing.html#1023832">1202 program alarm</a>". On the radio, an Elf is already explaining how to handle the situation: "Don't worry, that's perfectly norma--" The ship computer <a href="https://en.wikipedia.org/wiki/Halt_and_Catch_Fire">bursts into flames</a>.</p>
<p>You notify the Elves that the computer's <a href="https://en.wikipedia.org/wiki/Magic_smoke">magic smoke</a> seems to have <span title="Looks like SOMEONE forgot to change the switch to 'more magic'.">escaped</span>. "That computer ran <em>Intcode</em> programs like the gravity assist program it was working on; surely there are enough spare parts up there to build a new Intcode computer!"</p>
<p>An Intcode program is a list of <a href="https://en.wikipedia.org/wiki/Integer">integers</a> separated by commas (like <code>1,0,0,3,99</code>).  To run one, start by looking at the first integer (called position <code>0</code>). Here, you will find an <em>opcode</em> - either <code>1</code>, <code>2</code>, or <code>99</code>. The opcode indicates what to do; for example, <code>99</code> means that the program is finished and should immediately halt. Encountering an unknown opcode means something went wrong.</p>
<p>Opcode <code>1</code> <em>adds</em> together numbers read from two positions and stores the result in a third position. The three integers <em>immediately after</em> the opcode tell you these three positions - the first two indicate the <em>positions</em> from which you should read the input values, and the third indicates the <em>position</em> at which the output should be stored.</p>
<p>For example, if your Intcode computer encounters <code>1,10,20,30</code>, it should read the values at positions <code>10</code> and <code>20</code>, add those values, and then overwrite the value at position <code>30</code> with their sum.</p>
<p>Opcode <code>2</code> works exactly like opcode <code>1</code>, except it <em>multiplies</em> the two inputs instead of adding them. Again, the three integers after the opcode indicate <em>where</em> the inputs and outputs are, not their values.</p>
<p>Once you're done processing an opcode, <em>move to the next one</em> by stepping forward <code>4</code> positions.</p>
<p>For example, suppose you have the following program:</p>
<pre><code>1,9,10,3,2,3,11,0,99,30,40,50</code></pre>
<p>For the purposes of illustration, here is the same program split into multiple lines:</p>
<pre><code>1,9,10,3,
2,3,11,0,
99,
30,40,50
</code></pre>
<p>The first four integers, <code>1,9,10,3</code>, are at positions <code>0</code>, <code>1</code>, <code>2</code>, and <code>3</code>. Together, they represent the first opcode (<code>1</code>, addition), the positions of the two inputs (<code>9</code> and <code>10</code>), and the position of the output (<code>3</code>).  To handle this opcode, you first need to get the values at the input positions: position <code>9</code> contains <code>30</code>, and position <code>10</code> contains <code>40</code>.  <em>Add</em> these numbers together to get <code>70</code>.  Then, store this value at the output position; here, the output position (<code>3</code>) is <em>at</em> position <code>3</code>, so it overwrites itself.  Afterward, the program looks like this:</p>
<pre><code>1,9,10,<em>70</em>,
2,3,11,0,
99,
30,40,50
</code></pre>
<p>Step forward <code>4</code> positions to reach the next opcode, <code>2</code>. This opcode works just like the previous, but it multiplies instead of adding.  The inputs are at positions <code>3</code> and <code>11</code>; these positions contain <code>70</code> and <code>50</code> respectively. Multiplying these produces <code>3500</code>; this is stored at position <code>0</code>:</p>
<pre><code><em>3500</em>,9,10,70,
2,3,11,0,
99,
30,40,50
</code></pre>
<p>Stepping forward <code>4</code> more positions arrives at opcode <code>99</code>, halting the program.</p>
<p>Here are the initial and final states of a few more small programs:</p>
<ul>
<li><code>1,0,0,0,99</code> becomes <code><em>2</em>,0,0,0,99</code> (<code>1 + 1 = 2</code>).</li>
<li><code>2,3,0,3,99</code> becomes <code>2,3,0,<em>6</em>,99</code> (<code>3 * 2 = 6</code>).</li>
<li><code>2,4,4,5,99,0</code> becomes <code>2,4,4,5,99,<em>9801</em></code> (<code>99 * 99 = 9801</code>).</li>
<li><code>1,1,1,4,99,5,6,0,99</code> becomes <code><em>30</em>,1,1,4,<em>2</em>,5,6,0,99</code>.</li>
</ul>
<p>Once you have a working computer, the first step is to restore the gravity assist program (your puzzle input) to the "1202 program alarm" state it had just before the last computer caught fire. To do this, <em>before running the program</em>, replace position <code>1</code> with the value <code>12</code> and replace position <code>2</code> with the value <code>2</code>. <em>What value is left at position <code>0</code></em> after the program halts?</p>
</article>