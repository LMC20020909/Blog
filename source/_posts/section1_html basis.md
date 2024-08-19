---
title: html basis 
updated: 2022-11-27 22:17:32
categories: [教程, font-end]
tags: [教程, font-end, 笔记, html, css]
excerpt: Consolidate the foundation of html5
index_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20221022_bg8.jpg
banner_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20221022_bg8.jpg
---

### use semantic tags(no visual effect)

```html
//文章标题部分
<header>
    //导航栏
    <nav>
    </nav>
</header>

//文章正文
<article>
</article>

//补充信息，次要信息
<aside>
</aside>

//页脚
<footer>
</footer>
```

### common tags

```html
//标题级别1-6
<h1></h1>
...
<h6></h6>

//超链接
<a href="">The text</a>
//href属性为#回到当前页面顶部
<a href="#">The text</a>
//默认在当前页面打开, target='_blank'属性表明在新页面打开
<a href="" target='_blank'>The text</a>

//图片
//src:source, alt:alternative
//the content of 'alt' attribute will be shown when the image cannot be successfully loaded
<img src="" alt="" width="" height="" />

//粗体
//out of style: bold
<b></b>
//recommended style(semantic)
<strong></strong>

//斜体
//out of style: italic
<i></i>
//recommended style: emphasize
<em></em>

//段落: paragraph
<p></p>

//有序列表
//ol: ordered list
//li: list
<ol>
    <li></li>
</ol>

//无序列表
//ul: unordered list
<ul>
    <li></li>
</ul>
```

### html entity: some special characters

https://css-tricks.com/snippets/html/glyphs/