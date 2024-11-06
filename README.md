# Đồ án hướng HTTT về Sales

## 1.Giới thiệu
Backend đỉnh cao top 1 thế giới hơn Faker 1 xíu

## 2.Cách clone backend (IMPORTANT)
### Bước 1: Clone repo của backend về
- 1a. Mở CMD và CD vào folder cần clone backend

![changeDirectory](https://media.discordapp.net/attachments/556788092023865355/1303642926622052414/GetIntoFolder.png?ex=672c7f96&is=672b2e16&hm=0bee57e5c271b0be202d4fe363232b52fa8fcdea2ab96cc15f244ab54f04254d&=&format=webp&quality=lossless&width=1441&height=229)

- 1b. Gõ lệnh sau để clone repo github của backend
```
git clone https://github.com/Marky303/DA_HTTT_BE.git
```
![clone](https://media.discordapp.net/attachments/556788092023865355/1303642927834337341/Cloning.png?ex=672c7f96&is=672b2e16&hm=fe98319cda9fb407866bae1413304612e4fe0d788c757682d6de48c9dae879cf&=&format=webp&quality=lossless&width=1441&height=325)

- 1c. Sau khi clone, CD vào DA_HTTT_BE. Folder của backend sẽ như sau
```
cd DA_HTTT_BE
```
![CDAfter](https://media.discordapp.net/attachments/556788092023865355/1303642927431680010/AfterCloning.png?ex=672c7f96&is=672b2e16&hm=69b00d96138f3ae00da16ff5d19c02700ea135c3629a3231e6583347d696e32a&=&format=webp&quality=lossless&width=1156&height=566)


### Bước 2: Tải các thư viện 
- 2a. Trước khi tải thư viện, trên máy phải có 
    + Python (Python 3.11+ thì càng tốt)
    + Pip ([link](https://packaging.python.org/en/latest/tutorials/installing-packages/))


- 2b. Install thư viện tạo môi trường ảo virtualenv 
```
pip install virtualenv
```

- 2c. Tạo môi trường ảo
```
virtualenv env
```
> [!WARNING]
> Sau khi tạo môi trường ảo trong folder của backend sẽ có thêm folder "env"
![CDAfter](https://media.discordapp.net/attachments/556788092023865355/1303642926282182717/envFolder.png?ex=672c7f96&is=672b2e16&hm=4e29c82718553c1daf59d800ecdb88b685f9d5fea0d8b50c87629ffec9ba3e0b&=&format=webp&quality=lossless&width=972&height=496)


- 2d. Vào môi trường ảo
``` 
env\Scripts\activate
```
> [!WARNING]
> Sau khi vào môi trường ảo, CMD sẽ hiện "(env)" trước các lệnh
![enterENV](https://media.discordapp.net/attachments/556788092023865355/1303642925984518185/Enterenv.png?ex=672c7f96&is=672b2e16&hm=c66970b6a8f0512aa9855da539dcf228d3a8386f01b239427342b25d2de78ed7&=&format=webp&quality=lossless&width=1345&height=130)


- 2e. Cài đặt các thư viện cần thiết bằng cách gõ lệnh sau
```
pip install -r req.txt
```
> [!WARNING]
> Cài đặt có thể mất 5-10p


### Bước 3: Chạy backend
- 3a. Trước khi chạy backend cần phải đảm bảo (nếu vừa clone xong thì bỏ qua điểm này)
    + Thứ nhất: Pull các update mới nhất từ repo
    ```
    git pull origin main
    ```
    > Lấy các cập nhật mới nhất từ repo

    + Thứ hai: Đã vào môi trường ảo (quan trọng)
    ```
    env\Scripts\activate
    ```
    > Sau khi vào môi trường ảo, CMD sẽ hiện (env) trước các lệnh

    + Cuối cùng: Đã install các library mới nhất 
    ```
    pip install -r req.txt
    ```
    > Cài các library mới nhất vì repo có thể thêm các thư viện mới.

- 3b. Sau khi đã đảm bảo các bước trên, chạy backend bằng cách gõ lệnh
```
python manage.py runserver
```
![finish](https://media.discordapp.net/attachments/556788092023865355/1303642927100071966/succeed.png?ex=672c7f96&is=672b2e16&hm=599227d7bc096ef0ff78f8bd176d13fb1a46161b7cb393a30e28ceeab1e832a5&=&format=webp&quality=lossless&width=1441&height=339)


## 3.Lưu ý (IMPORTANT)
- Nếu có thắc mắc hay bị lỗi trong quá trình cài đặt, nhắn trực tiếp với mình trên Zalo. Mình sẽ cố gắng trả lời trong thời gian ngắn nhất.




