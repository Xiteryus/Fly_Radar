# Note 

Remoove audio module 
```
sudo rmmod snd_bcm2835
```

Check if audio module is gone 
```
lsmod | grep snd
```
Slown down the GPIO when launching the code to avoid parasite
```
--led-slowdown-gpio=2
```