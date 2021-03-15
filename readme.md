# Wiz Open API In Python

+ Unofficial

+ [Wiz Open API](https://www.wiz.cn/wapp/pages/book/bb8f0f10-48ca-11ea-b27a-ef51fb9d4bb4)

## Usage

```python
from wiz import Wiz

if __name__ == '__main__':
    wiz = Wiz()
    r = wiz.login(userId=input('userId: '), password=input('password: '))
    print(r.json())
    r = wiz.logout()
    print(r.json())
```
