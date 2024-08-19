---
title: css basis 
updated: 2022-12-02 21:41:33
categories: [教程, font-end]
tags: [教程, font-end, 笔记, html, css]
excerpt: Consolidate the foundation of css
index_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20221022_bg9.jpg
banner_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20221022_bg9.jpg
---

## Introduce css to html file

```css
<link href="" rel="stylesheet" />
```

## Selectors

##### 通用选择器universal selectors

```css
/*重置全局的padding和margin，对全局生效*/
* {
  margin: 0;
  padding: 0;
}
```

##### 标签选择器

```css
body {
  font-family: sans-serif;
  color: #444;
  border-top: 10px solid #1098ad;
  position: relative;
}
```

##### id选择器

```css
/*id="author"*/
#author {
  font-style: italic;
  font-size: 18px;
}
```

##### class选择器

```css
/*class="container"*/
.container {
  width: 800px;
  margin: 0 auto;
}
```

### select specific tags

```css
/*nav标签中的div标签*/
nav div {

}
```

```css
/*class为select-color的标签中的div标签*/
.select-color div {
  margin-right: 0;
}
```

## priority(conflicts between selectors)

![Screenshot_20221130_204517_tv.danmaku.bili](https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps//img/Screenshot_20221130_204517_tv.danmaku.bili.jpg)

## selectors inheritance

只有与文本有关的属性才会被继承：

+ font-family
+ color
+ font-size
+ ...

其他属性如margin则不会被子元素继承

## pseudo-classes 伪类

+ 一个冒号

```css
/*the li tag which serves as the first child of its father class
作为其父类的第一个元素的li标签*/
li:first-child {
  font-weight: bold;
}
```

```css
/*the p element as the last child in article 
not the last p element in article
*/
article p:last-child {
  color: red;
}
```

```css
/*作为其父类第n个元素的li标签*/
li:nth-child(n) {
  color: red;
} 

/*其父类下面的奇数序号的li标签*/
li:nth-child(odd) {
  color: red;
}
```

### 表示状态的伪类

```css
/* 'a' tag with a href attribute */
a:link {
  color: #1098ad;
  text-decoration: none;
}

a:visited {
  color: #1098ad;
}

/*鼠标悬浮*/
a:hover {
  color: orangered;
  font-weight: bold;
  text-decoration: underline orangered;
}

/* click */
a:active {
  background-color: black;
  font-style: italic;
}
/* 顺序：LVHA */
```

## CSS box model

![Screenshot_20221201_170435_tv.danmaku.bili](https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps//img/Screenshot_20221201_170435_tv.danmaku.bili.jpg)

## 页面居中

先设定宽度，再将左右间距设为auto，浏览器自动计算margin-left和margin-right的值使两者相等。

```css
.container {
  width: 800px;
  margin: 0 auto;
}
```

## Types of boxes

### inline

+ 如标签a、strong等
+ 所占空间即其内容所占空间
+ 无法对其设置width、height、margin-top、margin-bottom属性
+ margin-left、margin-right可以正常设置

### block

+ 如标签p、h1等
+ 独占一行
+ 可以设置相应属性

### inline-block

+ 所占空间即其内容所占空间，不独占一行
+ 可以设置相应属性

```css
display: inline-block;
```

## absolute positioning 绝对定位

绝对指定该元素相对于其第一个position属性为relative的父元素的位置

```html
<div class="product">
    <div class="sale">
    </div>
</div>
```

```css
.product {
  position: relative;
}
.sale {
  position: absolute;
  top: -20px;
  left: -35px;
}
```

## Pseudo-elements

+ 两个冒号

```css
/*设置h1标签文本的首字母*/
h1::first-letter {
  font-style: normal;
  margin-right: 5px;
}
```

```css
/*设置紧邻h3标签的p标签中文本的第一行*/
h3 + p::first-line {
  color: red;
}
```
