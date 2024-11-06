# Đồ án hướng HTTT về Sales

## 1.Giới thiệu
Backend đỉnh cao top 1 thế giới hơn Faker 1 xíu

## 2.Cách clone backend (IMPORTANT)
### Bước 1: Clone repo của backend về
- Mở CMD và CD vào folder cần clone backend
![clone](https://drive.google.com/file/d/1uL2QWV_cfbbnLADJXh4RDNDXtJpldGHC/view?usp=sharing)

- Gõ lệnh sau để clone repo github của backend
```
git clone https://github.com/Marky303/DA_HTTT_BE.git
```


- Sau khi clone, CD vào DA_HTTT_BE
```
cd DA_HTTT_BE
```

- Folder của backend sẽ như sau

### Bước 2: Tải các thư viện 
- Trước khi tải thư viện, trên máy phải có 
    + Python (Python 3.11+ thì càng tốt)
    + Pip ([link](https://packaging.python.org/en/latest/tutorials/installing-packages/))



- Install thư viện tạo môi trường ảo virtualenv 
```
pip install virtualenv
```



- Tạo môi trường ảo
```
virtualenv env
```
> [!WARNING]
> Sau khi tạo môi trường ảo trong folder của backend sẽ có thêm folder "env"



- Vào môi trường ảo
``` 
env\Scripts\activate
```
> [!WARNING]
> Sau khi vào môi trường ảo, CMD sẽ hiện "(env)" trước các lệnh



- Cài đặt các thư viện cần thiết bằng cách gõ lệnh sau
```
pip install -r req.txt
```
> [!WARNING]
> Cài đặt có thể mất 5-10p


### Bước 3: Chạy backend
- Trước khi chạy backend cần phải đảm bảo (nếu vừa clone xong thì bỏ qua điểm này)
    + Pull các update mới nhất từ repo
    ```
    git pull origin main
    ```

    + Đã vào môi trường ảo (quan trọng)
    ```
    env\Scripts\activate
    ```
    > [!WARNING]
    > Sau khi vào môi trường ảo, CMD sẽ hiện (env) trước các lệnh

    + Đã install các library mới nhất 
    ```
    pip install -r req.txt
    ```
    > [!WARNING]
    > Các update mới nhất từ repo có thể thêm các thư viện mới.

- Sau khi đã đảm bảo các bước trên, chạy backend bằng cách gõ lệnh
```
python manage.py runserver
```


- Nếu có thắc mắc hay bị lỗi trong quá trình cài đặt, nhắn trực tiếp với mình trên Zalo. Mình sẽ cố gắng trả lời trong thời gian ngắn nhất.




