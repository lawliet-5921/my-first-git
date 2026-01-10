import torch
import time

# 1. GPU가 있는지 확인
if torch.cuda.is_available():
    # 2. 거대한 랜덤 숫자를 만들어서 GPU 메모리에 강제로 집어넣음 (메모리 점유)
    # 'cuda'라는 말이 들어가야 진짜 GPU를 쓰는 겁니다.
    data = torch.randn(10000, 10000).to('cuda') 
    
    print("GPU에 데이터를 올렸습니다! 지금 gpustat을 확인해보세요.")
    print("10초 동안 대기합니다... (이때 gpustat에 뜹니다)")
    
    # 3. gpustat이 볼 수 있게 10초 동안 멈춰있기
    time.sleep(10)
    
    print("실험 끝! 메모리를 비웁니다.")
else:
    print("어라? GPU를 찾을 수 없습니다.")



print("프롬프트 종료")