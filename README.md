### 随申办核酸结果批量查询并保存
#### 第一步 安装依赖
```
pip install requirements.txt
```
* pyautogui==0.9.53
* win32con==0.2.0
* pyperclip==1.8.2
* Pillow==6.2.0
* win32con



#### 第二步，打开随申办查询位置
![image](https://user-images.githubusercontent.com/101266608/197402895-e579e30e-a76c-435b-8aad-29f19fe5f716.png)

#### 第三步，创建身份信息文本
同级目录下创建 name_id.txt,里面是姓名和身份证。
例：

张三310123456789101112

李四310123456789101113

王五六310123456789101113

#### 第四步  运行，并保存图片
![image](https://user-images.githubusercontent.com/101266608/197403079-fbfe42e9-d62b-4767-84b4-2ce1a01dabc6.png)

