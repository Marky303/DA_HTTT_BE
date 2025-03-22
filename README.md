# Đồ án hướng HTTT về Sales

## 1.Giới thiệu
Backend đỉnh cao top 1 thế giới hơn Faker 1 xíu

## 2.Cách clone backend (IMPORTANT)
### Bước 1: Clone repo của backend về
- 1a. Mở CMD và CD vào folder cần clone backend

![changeDirectory](https://media.discordapp.net/attachments/518446875893039117/1306662826395303936/GetIntoFolder.png?ex=67377c16&is=67362a96&hm=58a864b9d3c68111f83a5165550525038dc28b281abed0efb5e432f490e84cb3&=&format=webp&quality=lossless&width=1441&height=229)

- 1b. Gõ lệnh sau để clone repo github của backend
```
git clone https://github.com/Marky303/DA_HTTT_BE.git
```
![clone](https://media.discordapp.net/attachments/518446875893039117/1306662827628691587/Cloning.png?ex=67377c16&is=67362a96&hm=e08cffb5240c19b3b450a6d02461abddeb9b12476105e570a431e20db5986497&=&format=webp&quality=lossless&width=1441&height=325)

- 1c. Sau khi clone, CD vào DA_HTTT_BE. Folder của backend sẽ như sau
```
cd DA_HTTT_BE
```
![CDAfter](https://media.discordapp.net/attachments/518446875893039117/1306662827385290782/AfterCloning.png?ex=67377c16&is=67362a96&hm=e018d236292681aa1e0bb2094dde3954697a0c1ca422cb3f8b6d473c6ebeb6ae&=&format=webp&quality=lossless&width=1156&height=566)


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
![CDAfter](https://media.discordapp.net/attachments/518446875893039117/1306662828530471004/envFolder.png?ex=67377c16&is=67362a96&hm=0249b58d27fcc1bb09e38d1723bafda0cdc904a6a6c9c447f786c920c9115d82&=&format=webp&quality=lossless&width=972&height=496)


- 2d. Vào môi trường ảo
``` 
env\Scripts\activate
```
> [!WARNING]
> Sau khi vào môi trường ảo, CMD sẽ hiện "(env)" trước các lệnh
![enterENV](https://media.discordapp.net/attachments/518446875893039117/1306662828220088322/Enterenv.png?ex=67377c16&is=67362a96&hm=8d902e2fb72ef714dff93a8a4d886b1742b664c3f5d842f45caeffac831eabeb&=&format=webp&quality=lossless&width=1345&height=130)


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
![finish](https://media.discordapp.net/attachments/518446875893039117/1306662826861006960/succeed.png?ex=67377c16&is=67362a96&hm=ce8ada2da9f0712f465683b2c4d0de45bfbffff14d002ce83ecdd0453980f2ae&=&format=webp&quality=lossless&width=1441&height=339)






