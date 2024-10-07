import serial

# 시리얼 포트 설정
port = 'COM5'  # 사용할 COM 포트 번호
baudrate = 460800  # 장치와 일치하는 전송 속도
timeout = 2  # 타임아웃 설정 (1초)
chunk_size = 1016 # 한번에 읽어올 데이터 크기

try:
    # 시리얼 포트 열기
    ser = serial.Serial(port, baudrate, timeout=timeout)

    print(f"Connected to {port} at {baudrate} baudrate.")

    while True:
        # 시리얼 포트로부터 데이터 읽기
        if ser.in_waiting > 0:  # 읽을 데이터가 있는 경우
            # data = ser.read(ser.in_waiting).decode('utf-8', errors='ignore')  # 모든 가용 데이터를 읽어옴
            data = ser.read(chunk_size).decode('utf-8', errors='ignore')  # 과연 이걸로 1016개씩 가져올 수 있나?
            print("start")
            print(data)  # 수신된 데이터 출력

except serial.SerialException as e:
    print(f"Error opening or using serial port: {e}")

except KeyboardInterrupt:
    print("\nExiting program.")

finally:
    if ser.is_open:
        ser.close()  # 프로그램 종료 시 시리얼 포트 닫기
        print("Serial port closed.")