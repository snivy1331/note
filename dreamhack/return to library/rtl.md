1. bof로 canary값 유출.
2. canary와 널 바이트 복구 + SFP 더미+ ret(스택 정렬)+ pop rdi; ret 가젯+ /bin/sh 주소+ system주소 -> system("/bin/sh")실행.