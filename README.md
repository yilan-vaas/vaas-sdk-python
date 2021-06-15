# vaas-sdk-python

## 概述

这是 VAAS API 的 Python 版本封装开发包，由一览科技官方提供，一般支持最新的 API 功能。

对应的 REST API 文档：<https://www.yuque.com/yilanyun/rfx7o4/oxt3td/>

## 兼容版本

+ Python 3

## 安装（建议）

```
    pip install --user vaas-sdk-python
```

如果已经安装vaas-sdk-python包，则用下面命令升级即可

```
    pip install --upgrade vaas-sdk-python
```

## 关于ACCESS_KEY/ACCESS_TOKEN

### ACCESS_KEY/ACCESS_TOKEN 注册申请流程

1.使用帐号/密码 [登录](https://yuncms.yilan.tv/admin/default/login) 控制台；

2.选择一级菜单“应用管理”->选择二级菜单“应用列表”,点击“新建应用”按钮创建应用；

3.创建过程中，请正确填写应用包名。 对于SDK，建议在“详情页地址”处填写正确的应用下载地址，以便之后进行广告配置以及运营工作。若应用暂未上架，此处可以先填写公司网址。待应用上架后请及时更新；

4.创建完成后，请将创建的应用信息截图发给对接人员，等待应用审核。一览将在3个工作日内审核完成。应用创建后分配access key和access token。

### ACCESS_KEY/ACCESS_TOKEN在sdk中的使用

- (option 1 推荐) 在代码里显示调用方法set_key/set_token，例：
  ```python
    credentials = credentials.Credentials()
    credentials.set_key('access_key')
    credentials.set_token('access_token')
  ```

- (option 2) 放在配置文件～/.vaas-sdk-python/src/vaas/config.py中，格式为：
  ```
    ACCESS_KEY = 'access_key'
    ACCESS_TOKEN = 'access_token'
  ```

## 代码样例

> 代码样例在 vaas-sdk-python 中的 example 文件夹中，[点击查看所有 example](https://github.com/yilanyun/vaas-sdk-python/tree/main/example) 。

> 以下片断来自项目代码里的文件：vaas-sdk-python 中的 example 目录下的 demo_vaas.py

```
if __name__ == '__main__':
    # 设置公共参数
    credentials = credentials.Credentials()
    credentials.set_key('access_key')
    credentials.set_token('access_token')
    credentials.set_pkgname('package_name')
    credentials.set_platform(2)
    # 设备唯一标识，客户端生成
    udid = '5459daf640bdb6a6a7e294a5f3f5f0d1'
    vaas = vaas.Vaas(udid)
    # 获取频道数据
    test_channel(vaas)
```

## 运行代码方式，在根目录下执行

python vaas-sdk-python/example/demo_vaas.py
