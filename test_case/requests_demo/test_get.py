import allure
import requests
#request 发生http请求

@allure.feature("get请求")
@allure.story("查询")
@allure.title("用例名1")

def test_no_params():
    r=requests.get("https://www.baidu.com/")
    print(r.text)
    pass

def test_no_params1():
    sess = requests.session()# 使用session建立连接
    r =sess. request(method="GET",url="https://www.baidu.com/")#再发生请求，无论请求多少次，连接建立
    r =sess.request(method="GET",url="https://www.baidu.com/")
    print(r.text)#text获取响应对象中，响应正文的数据

@allure.feature("get请求")
@allure.story("123")
@allure.title("用例名2")
def test_get_params():
    ke={"accountName":"xuepl123"}
    r=requests.request("GET","http://qa.yansl.com:8084/acc/getAccInfo",params=ke)
    print(r.text)

@allure.feature("get请求")
@allure.story("path")
@allure.title("用例名3")
def test_get_path():
    r=requests.request("GET","http://qa.yansl.com:8084/acc/getAllAccs/{}/{}".format(1,10))
    print(r.text)

@allure.feature("get请求")
@allure.story("下载文件")
@allure.title("用例名4")
def test_get_file(pub_data):
    with allure.step("第一步、准备测试数据"):pass
    p={"pridCode":"63803y"}
    h={"token":pub_data["token"]}
    with allure.step("第二步、发送请求"):pass
    r=requests.request("GET","http://qa.yansl.com:8084/product/downProdRepertory",params=p,headers=h)
    with allure.step("第三步、请求数据"):
        allure.attach("请求行，请求头，请求正文","请求信息",allure.attachment_type.TEXT)
    with open("xx.xls","wb") as f:
        f.write(r.content)