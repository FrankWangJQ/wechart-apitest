# wechart-apitest
apitest with pytest &amp; request

从实际工作出发：编写企业微信测试用例
    Python + requests + pytest + allure

总结出测试框架必须具备的功能点

接口测试核心需求梳理（需求池）
    从感官需求到技术需求
    实现 Web 接口协议层的测试

支持网络协议 HTTP(S)
    GET/POST/PUT/HEAD/DELETE
    POST 多种类型

构造请求参数
    接口请求具备登录态
    session 保持
    接口请求参数依赖前面接口的响应
    接口响应提取
    参数关联机制

接口测试脚本支持接入 CI
    测试用例可以通过命令行运行
    命令行工具

需要统计（展现）测试用例运行数据
    收集测试用例运行数据
    将测试结果数据展示为测试报告

多个用例可以共享单个接口定义
    测试用例支持分层管理
    测试用例封装（组织形式）
    支持测试用例与数据分离
    支持数据驱动
    支持快速生成测试用例

录制用户操作请求
    Charles/Fiddler/Chrome

生成测试用例

安装包分发，支持 pip 安装

脚本描述形式
    Python 脚本

    用户故事 1：实现单个 HTTP(S) 接口的测试
概述：作为框架用户，可以对单个接口构造参数发起请求，并对响应结果进行校验，以便实现对单个接口的正确性进行测试验证。
详述
请求参数包括
method
url
headers
data
支持 HTTP(S) 协议常用请求 body 类型（POST）
JSON（application/json）
form 表单（application/x-www-form-urlencoded）
上传文件（multipart/form-data）（优先级 P2）
实现标准化的接口响应校验机制
校验项
响应状态码（status_code）
响应 header 中的指定字段
响应 Cookie 中的指定字段
响应 body 中的指定字段（响应为 JSON 格式），借助 jsonpath
响应 body 中的指定字段（响应为 text/html 格式），借助 regex 正则匹配（优先级 P2）
校验方式
eq
测试结果统计查看
结果：成功、失败
失败：失败原因
验证标准

    用户故事 2：在单个测试用例中实现复杂场景（关联性接口）的测试
    概述：作为框架用户，可以在单个测试用例中描述多个接口的请求和校验，以便实现复杂测试场景中关联性接口的测试验证。
    详述
实现测试用例的参数机制
实现测试用例层面的参数共享机制
实现测试步骤间的参数关联（接口前后依赖问题）
实现接口参数的提取
status_code
headers.XXX
body.XXX.XXX
实现用例级别的用户登录态（session 共享机制）
测试用例级别的 hook 机制
验收标准
测试步骤之间参数共享
测试步骤之间参数依赖
登录态
第一个接口带 cookie
第二个接口不带 cookie

    用户故事 3：接口测试用例支持命令行运行
概述：作为框架用户，可以在命令行中运行指定测试用例（集），以便实现将自动化测试用例接入持续集成（CI）或线上监控。
详述
指定运行单个测试用例
指定运行多个测试用例
指定运行测试用例集

    用户故事 4：测试结果的统计和展现
概述：作为框架用户，可以在运行测试用例后查看结果统计数据和测试报告，以便实现清晰查看到测试用例执行情况（成功XX，失败XX，具体失败的用例详情等）。
详述
测试结果统计数据
用例总数
成功数
失败数
请求 & 响应详情
校验详情

    用户故事 5：测试用例支持数据驱动
概述：作为框架用户，可以采用一组数据驱动测试用例的执行，以便实现测试用例和数据的解耦，覆盖更多的场景。
详述
单个参数
组合参数
用户名、密码
参数化数据类型
独立参数
关联参数（例如账户名和密码需配对使用）
参数化校验（关联校验参数与运行参数）
数据源配置方式
直接指定参数列表
指定外置数据源（CSV）
引用函数动态生成参数列表
pytest
https://docs.pytest.org/en/latest/fixture.html#parametrizing-fixtures

    用户故事 6：框架安装包的分发
概述：作为框架开发者，可以将框架分发到 PyPI 上，以便让其他用户可以通过 pip 命令安装该框架。
详述
setup.py
pypi



技术架构
命令行工具（client）
    Client - Server

技术选型
    Python

HTTP 客户端
    requests
脚本描述形式
    Python 脚本语法提示 自动补全

测试用例组织管理
    pytest

数据存储
Python 代码

初始化项目
GitHub 仓库创建

项目依赖管理
poetry + pyproject.yml

持续集成 & 测试
选择持续集成服务器
GitHub => Travis CI

构建脚本
Travis CI => .travis.yml

单元测试
单元测试依赖服务
httpbin.org

搭建 API 接口 Mock 服务（非必须）
HTTP server

代码风格检查
PEP 8
pylint

为项目添加持续集成构建检查（Travis CI）
https://travis-ci.org/

为项目添加单元测试覆盖率检查（coverage & coveralls）
http://coveralls.io/
发布

将项目制作为安装包
setup.py
poetry

分发安装包
pypi
https://pypi.org/

发布脚本
poetry publish
python setup.py upload
twine sdist/*

用户故事 0：项目工程基础设施搭建
概述：作为框架开发者，可以在每次提交代码后，在不同 Python 版本下运行单元测试，以便及时发现问题，获得高效的开发效率。
详述
自动构建，运行在不同的 Python 版本环境下
单元测试运行
单元测试覆盖率显示
验收标准
单行命令触发持续集成测试，获得测试结果和覆盖率统计