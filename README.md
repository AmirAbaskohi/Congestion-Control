# Congestion Control
This is an experiment on differences between different congestion control algorithms. The experiment is done by tcl.

## What is TCL?
Tcl (pronounced "tickle" or as an initialism) is a high-level, general-purpose, interpreted, dynamic programming language. It was designed with the goal of being very simple but powerful.Tcl casts everything into the mold of a command, even programming constructs like variable assignment and procedure definition. Tcl supports multiple programming paradigms, including object-oriented, imperative and functional programming or procedural styles. 

## Network toplogy
Here is the network topolgy:
![image](https://user-images.githubusercontent.com/50926437/126899701-7465ef56-75e5-4ad0-8200-8f458ab59f7d.png)


* There is a data flow from node 1 to 5 and node 2 to 6
* Quese size = 10 (for routers)
* TTL = 64
* Window size at first is 8000

## Code
For each of these algorithms:
* Cubic
* Reno
* YeAH

There is `tcl` file which you can run it using:
```
tcl file.tcl
```

## Result
To see the result, after running each `tcl` file you can run different `python` scripts to visualize differences between these algorithms. There `python` scripts for these measurements:
* RTT
* Goodput
* Dropped
* CWND

*By Amirhossein Abaskohi And Arash Rasouli*
