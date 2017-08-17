# Mynews
这个项目是[Mynews](http://www.mr-zys.top)的重构。主要是前后端分离，后端flask开发，只提供oauth2和RESTful API，前端使用reactjs开发，负责页面渲染。

## 功能
* oauth2登陆
* 站点列表、订阅、取消大约、添加站点
* 新闻列表
* 站点新闻抓取，HTML和RSS订阅

## 技术栈
* Flask
* Reactjs
* Celery

## To Do List

### 2017年8月18日

- [ ] `/api/categories`的`GET`、`POST`、`PUT`接口
- [ ] `/api/categories/<int:category_id>/site`的`GET`、`POST`、`PUT`和`DELETE`接口
- [ ] `/api/news`的`GET`和`POST`接口
- [ ] `/api/sites`的`GET`、`POST`、`PUT`和`DELETE`接口
- [ ] `/api/sites/<int:site_id>/news`的`GET`、`POST`、`PUT`和`DELETE`接口

### 2017年8月20日

- [ ] 集成`Aouth2`
- [ ] 集成`Reactjs`
- [ ] 前端首页页面展示
- [ ] 数据导入
