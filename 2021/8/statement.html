<article class="day-desc"><h2>--- Day 8: Seven Segment Search ---</h2><p>You barely reach the safety of the cave when the whale smashes into the cave mouth, collapsing it. Sensors indicate another exit to this cave at a much greater depth, so you have no choice but to press on.</p>
<p>As your submarine slowly makes its way through the cave system, you notice that the four-digit <a href="https://en.wikipedia.org/wiki/Seven-segment_display" target="_blank">seven-segment displays</a> in your submarine are malfunctioning; <span title="Yes, just the four-digit seven-segment ones. Whole batch must have been faulty.">they must have been damaged</span> during the escape. You'll be in a lot of trouble without them, so you'd better figure out what's wrong.</p>
<p>Each digit of a seven-segment display is rendered by turning on or off any of seven segments named <code>a</code> through <code>g</code>:</p>
<pre><code>  0:      1:      2:      3:      4:
 <em>aaaa</em>    ....    <em>aaaa    aaaa</em>    ....
<em>b    c</em>  .    <em>c</em>  .    <em>c</em>  .    <em>c  b    c</em>
<em>b    c</em>  .    <em>c</em>  .    <em>c</em>  .    <em>c  b    c</em>
 ....    ....    <em>dddd    dddd    dddd</em>
<em>e    f</em>  .    <em>f  e</em>    .  .    <em>f</em>  .    <em>f</em>
<em>e    f</em>  .    <em>f  e</em>    .  .    <em>f</em>  .    <em>f</em>
 <em>gggg</em>    ....    <em>gggg    gggg</em>    ....

  5:      6:      7:      8:      9:
 <em>aaaa    aaaa    aaaa    aaaa    aaaa</em>
<em>b</em>    .  <em>b</em>    .  .    <em>c  b    c  b    c</em>
<em>b</em>    .  <em>b</em>    .  .    <em>c  b    c  b    c</em>
 <em>dddd    dddd</em>    ....    <em>dddd    dddd</em>
.    <em>f  e    f</em>  .    <em>f  e    f</em>  .    <em>f</em>
.    <em>f  e    f</em>  .    <em>f  e    f</em>  .    <em>f</em>
 <em>gggg    gggg</em>    ....    <em>gggg    gggg</em>
</code></pre>
<p>So, to render a <code>1</code>, only segments <code>c</code> and <code>f</code> would be turned on; the rest would be off. To render a <code>7</code>, only segments <code>a</code>, <code>c</code>, and <code>f</code> would be turned on.</p>
<p>The problem is that the signals which control the segments have been mixed up on each display. The submarine is still trying to display numbers by producing output on signal wires <code>a</code> through <code>g</code>, but those wires are connected to segments <em>randomly</em>. Worse, the wire/segment connections are mixed up separately for each four-digit display! (All of the digits <em>within</em> a display use the same connections, though.)</p>
<p>So, you might know that only signal wires <code>b</code> and <code>g</code> are turned on, but that doesn't mean <em>segments</em> <code>b</code> and <code>g</code> are turned on: the only digit that uses two segments is <code>1</code>, so it must mean segments <code>c</code> and <code>f</code> are meant to be on. With just that information, you still can't tell which wire (<code>b</code>/<code>g</code>) goes to which segment (<code>c</code>/<code>f</code>). For that, you'll need to collect more information.</p>
<p>For each display, you watch the changing signals for a while, make a note of <em>all ten unique signal patterns</em> you see, and then write down a single <em>four digit output value</em> (your puzzle input). Using the signal patterns, you should be able to work out which pattern corresponds to which digit.</p>
<p>For example, here is what you might see in a single entry in your notes:</p>
<pre><code>acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf</code></pre>
<p>(The entry is wrapped here to two lines so it fits; in your notes, it will all be on a single line.)</p>
<p>Each entry consists of ten <em>unique signal patterns</em>, a <code>|</code> delimiter, and finally the <em>four digit output value</em>. Within an entry, the same wire/segment connections are used (but you don't know what the connections actually are). The unique signal patterns correspond to the ten different ways the submarine tries to render a digit using the current wire/segment connections. Because <code>7</code> is the only digit that uses three segments, <code>dab</code> in the above example means that to render a <code>7</code>, signal lines <code>d</code>, <code>a</code>, and <code>b</code> are on. Because <code>4</code> is the only digit that uses four segments, <code>eafb</code> means that to render a <code>4</code>, signal lines <code>e</code>, <code>a</code>, <code>f</code>, and <code>b</code> are on.</p>
<p>Using this information, you should be able to work out which combination of signal wires corresponds to each of the ten digits. Then, you can decode the four digit output value. Unfortunately, in the above example, all of the digits in the output value (<code>cdfeb fcadb cdfeb cdbaf</code>) use five segments and are more difficult to deduce.</p>
<p>For now, <em>focus on the easy digits</em>. Consider this larger example:</p>
<pre><code>be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |
<em>fdgacbe</em> cefdb cefbgd <em>gcbe</em>
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |
fcgedb <em>cgb</em> <em>dgebacf</em> <em>gc</em>
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |
<em>cg</em> <em>cg</em> fdcagb <em>cbg</em>
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |
efabcd cedba gadfec <em>cb</em>
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |
<em>gecf</em> <em>egdcabf</em> <em>bgf</em> bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |
<em>gebdcfa</em> <em>ecba</em> <em>ca</em> <em>fadegcb</em>
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |
<em>cefg</em> dcbef <em>fcge</em> <em>gbcadfe</em>
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |
<em>ed</em> bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |
<em>gbdfcae</em> <em>bgc</em> <em>cg</em> <em>cgb</em>
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |
<em>fgae</em> cfgab <em>fg</em> bagce
</code></pre>
<p>Because the digits <code>1</code>, <code>4</code>, <code>7</code>, and <code>8</code> each use a unique number of segments, you should be able to tell which combinations of signals correspond to those digits. Counting <em>only digits in the output values</em> (the part after <code>|</code> on each line), in the above example, there are <code><em>26</em></code> instances of digits that use a unique number of segments (highlighted above).</p>
<p><em>In the output values, how many times do digits <code>1</code>, <code>4</code>, <code>7</code>, or <code>8</code> appear?</em></p>
</article>