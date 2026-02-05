## Idk how to start this article so I’ll just say it

On my last article we built a text editor that was fast as fuck. Like genuinely snappy. Felt good. Ran great.

And then it segfaulted.
Not always. Just enough to ruin my mood.

So instead of pretending that’s fine, we’re gonna look at **valgrind**
<p align="center">
  <img width="269" height="188" alt="image" src="https://github.com/user-attachments/assets/4aee9903-b022-4921-a212-fb170e359e57" />
</p>


## What even is valgrind and why should I care

Valgrind is technically an instrumentation framework for building dynamic analysis tools.

Cool. Buzzwords. Whatever.

What that actually means is: you run your program, and Valgrind crawls inside it and watches *everything*. Every memory access. Every allocation. Every bad decision you thought the compiler wouldn’t notice.

Before we get into the damage, here’s the lineup of tools Valgrind ships with:

* **Memcheck** snitches on memory errors like invalid reads, invalid writes, leaks, and use-after-free in C/C++ programs.
* **Cachegrind** tells you why your “optimized” code is actually slow.
* **Callgrind** shows you exactly where your program wastes time, function by function.
* **Helgrind** catches data races and locking sins in multithreaded code.
* **DRD** does the same thing but differently, because sometimes Helgrind misses things.
* **Massif** watches your heap slowly balloon and judges you for it.
* **DHAT** points out memory waste you didn’t even know you had.
* **BBV** exists for computer architecture people and academics. We’ll ignore it.

ok enough yap



## the best part: you don’t have to rewrite your life

You don’t need to recompile, relink, or change your code just to use Valgrind. Which is honestly a miracle given how invasive it feels.

You just run your program *through* it.

Val wants to be used like this:

<img width="704" height="82" alt="image" src="https://github.com/user-attachments/assets/bc154592-662e-4b55-b192-bcd0ba9edf87" />

```bash
valgrind --tool=memcheck ls -l
```


The `--tool` option just tells Valgrind which flavor of suffering you want. In this case, Memcheck.


## what’s actually happening under the hood

Regardless of which tool you pick, Valgrind grabs your program **before it even starts running**. It reads all the debug info from your binary and the libraries it uses so that when something goes wrong, it can point at *actual source lines*.






## some internals before working with it

Because if you’re gonna let a tool psychoanalyze your code, you should at least know how it thinks.

Valgrind doesn’t just skim your program, it **simulates every single instruction** your program executes. Every. Single. One. That means the active tool isn’t only watching *your* code, it’s also watching everything your program pulls in: the C standard library, system libraries, graphics libraries, and whatever else got dynamically linked along .

Because of that, if you’re running an error-detection tool, Valgrind might start yelling about bugs inside system libraries like GNU libc or X11. Which is… cool information, but also not your problem. You didn’t write that code and you’re not fixing it today.

So Valgrind lets you shut it up selectively using **suppressions**. You record known, uninteresting errors into a suppressions file, and Valgrind reads that file when it starts so it can ignore those specific reports. By default, Valgrind already loads a set of suppressions based on your OS and installed libraries, so you usually don’t get spammed immediately.

If you want to write your own suppressions, there’s a helpful option:

```bash
--gen-suppressions=yes
```

This tells Valgrind to print out a ready-made suppression entry for each error it reports, which you can then copy straight into a suppressions file and move on with your life.

Valgrind also assumes you’re running on roughly the same OS and library versions it was built against. If you’re using different versions, things will mostly work, but you might see small behavioural differences.

Finally, not all Valgrind tools report the same kinds of errors. Because of that, suppressions can be scoped to specific tools, so you can say “ignore this for Memcheck but not for Helgrind” and stay precise instead of muting everything.



