set ns [new Simulator]
  
$ns color 1 Blue
$ns color 2 Red

set f1 [open cubic1.tr w]
set f2 [open cubic2.tr w]

set nr [open info.tr w]
$ns trace-all $nr
  
set nf [open cubic.nam w]
$ns namtrace-all $nf
  
proc finish {} {
    global ns nf nr f1 f2
    $ns flush-trace
      
    close $nf
    close $f1
    close $f2

    exec nam cubic.nam &
    exit 0
}

set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]

  
$ns duplex-link $n0 $n2 4000Mb 500ms DropTail
$ns duplex-link $n1 $n2 4000Mb 800ms DropTail
$ns duplex-link $n2 $n3 1000Mb 50ms DropTail
$ns duplex-link $n3 $n4 4000Mb 500ms DropTail
$ns duplex-link $n3 $n5 4000Mb 800ms DropTail


$ns duplex-link-op $n0 $n2 orient right-down
$ns duplex-link-op $n1 $n2 orient right-up
$ns duplex-link-op $n2 $n3 orient right
$ns duplex-link-op $n3 $n4 orient right-up
$ns duplex-link-op $n3 $n5 orient right-down


$ns queue-limit $n2 $n3 10
$ns queue-limit $n3 $n2 10


$ns duplex-link-op $n2 $n3 queuePos 0.5
$ns duplex-link-op $n3 $n2 queuePos 0.5




set tcp1 [new Agent/TCP/Linux]
$ns at 0 "$tcp1 select_ca cubic"
$tcp1 set class_ 2
$ns attach-agent $n0 $tcp1
  
set sink1 [new Agent/TCPSink/Sack1]
$ns attach-agent $n4 $sink1
$ns connect $tcp1 $sink1
$tcp1 set fid_ 1
$tcp1 set windowInit_ 8
$tcp1 set window_ 1000
$tcp1 set ttl_ 64
  
set ftp1 [new Application/FTP]
$ftp1 attach-agent $tcp1
$ftp1 set type_ FTP




set tcp2 [new Agent/TCP/Linux]
$ns at 0 "$tcp2 select_ca cubic"
$tcp2 set class_ 2
$ns attach-agent $n1 $tcp2

set sink2 [new Agent/TCPSink/Sack1]
$ns attach-agent $n5 $sink2
$ns connect $tcp2 $sink2
$tcp2 set fid_ 2
$tcp2 set windowInit_ 8
$tcp2 set window_ 1000
$tcp2 set ttl_ 64
  
set ftp2 [new Application/FTP]
$ftp2 attach-agent $tcp2
$ftp2 set type_ FTP


proc record {} {

        global tcp2 tcp1 f1 f2

        set ns [Simulator instance]

        set time 1

        set wnd1 [$tcp1 set cwnd_]
        set wnd2 [$tcp2 set cwnd_]
        set rtt1 [$tcp1 set rtt_]
        set rtt2 [$tcp2 set rtt_]
        set now [$ns now]

        puts $f1 "$now $wnd1 $rtt1"
        puts $f2 "$now $wnd2 $rtt2"

        $tcp1 set bytes_ 0
        $tcp2 set bytes_ 0

        $ns at [expr $now+$time] "record"
}


$ns at 0 "record"

$ns at 1 "$ftp1 start"
$ns at 1 "$ftp2 start"
$ns at 1000 "$ftp1 stop"
$ns at 1000 "$ftp2 stop"
  

$ns at 1000 "finish"

$ns run