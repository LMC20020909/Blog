---
title: css layout 
updated: 2022-12-08 19:11:09
categories: [教程, font-end]
tags: [教程, font-end, html, css, flex, css grid, floats]
excerpt: three kinds of css layouts——floats, flex, css grid
index_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20221022_bg10.jpg
banner_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20221022_bg10.jpg
---

## CSS布局

+ Floats
+ Flexbox
+ CSS Grid

## Floats

一种已经被Flexbox和CSS Grid淘汰了的布局方式

```css
float: left;
float: right;
```

浮动元素会从普通文档流中脱离，但浮动元素不同于`absolute positioning`，它会影响周围的元素进行环绕。让block元素无视float元素，让inline元素围绕着float元素。

![image-20221208192302026](https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps//img/image-20221208192302026.png)

### Height Collapse 高度崩塌

当父级块的所有子元素都为float元素时，我们认为父级块内没有元素，所以父级块的高度会变为零。

### Clearing Floats 清除浮动

对非浮动元素使用，使其不受周围float元素的影响

```css
clear: none | left | right | both
```

+ none：default，允许两边都可以有浮动对象
+ left：清除左边的浮动对象
+ right：清除右边的浮动对象
+ both：清除两边的浮动对象

### 清除浮动的两种方法（本质一样，写法不同）

1. 在父级块中增加一个空元素，使其清除浮动

   ```html
   <div class="clear"></div>
   ```

   ```css
   .clear {
     clear: both;
   }
   ```

2. 为父级块增加一个class，使用css伪元素为其增加一个元素清除浮动

   ```html
   <header class="main-header clearfix">
   ...
   </header>
   ```

   ```css
   .clearfix::after {
     clear: both;
     content: "";
     display: block;
   }
   ```

## Flexbox

[一篇写的很好的博客](https://link.juejin.cn/?target=https%3A%2F%2Fwww.joshwcomeau.com%2Fcss%2Finteractive-guide-to-flexbox%2F%3Fmode%3Ddark)

适用于一维布局，可以方便地实现居中

首先设置父容器（包含所有想要放在一排的元素）：

```css
display: flex;
```

接着可以针对不同需求设置不同的属性：

![image-20221208194706220](https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps//img/image-20221208194706220.png)

如图所示，左侧为父容器可以设置的属性，右侧为并排放置的元素(flex items)的属性。

### 几个常用属性

#### flex container

```css
gap: 10px;	//设置flex items之间的间距
justify-content: center;	//flex items沿主轴居中（默认水平居中）
align-items: center;	//沿交叉轴居中（默认垂直居中）
```

#### flex items

##### flex

flex会根据内容所需空间自动调整flex items的宽度，会自动分配剩余空间，所以需要`flex-grow`、`flex-shrink`、`flex-basis`三个属性进行设置。会根据flex items的`flex-grow`的比例自动伸缩，`flex-basis`用来手动指定flex items的宽度（在`flex-grow`属性不为0时不生效）。

常用`flex`属性代替写法（shorthand)

```css
/* flex-grow flex-shrink flex-basis */
flex: 0 0 100px;
```

实际上一般只用`flex`的第一个值来自动分配大小

```css
flex: 1
```

##### align-self

用来单独设定本元素的垂直对齐方式（重写align-items)

##### order

用来设置flex items出现的顺序，默认为0，数字越小越先出现

### Reference Link

[一劳永逸的搞定 flex 布局](https://juejin.cn/post/6844903474774147086)

## CSS Grid

适用于二维布局，常用于网页的整体布局，常与flex配合使用

设置父容器：

```css
display: grid;
```

![image-20221208201541149](https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps//img/image-20221208201541149.png)

### 常用属性

#### Grid Container

##### grid-template-columns

设置网格的列数及每一列的宽度

```css
grid-template-columns: 200px 200px 100px 100px;
```

通过比例指定：

```css
/* fr: fraction */
/* 两列，第一列占1/3，第二列占2/3 */
grid-template-columns: 1fr 2fr;
/* 4列，每一列宽度所占比例相同 */
grid-template-columns: repeat(4, 1fr);
```

##### grid-template-rows

设置网格的行数及每一行的宽度，与上同理，**该属性一般不用，一般仅指定列，让浏览器自动分配行**

##### gap（column-gap、row-gap）

如图

##### 四个对齐属性

###### justify-content和align-content

指定网格整体在Grid Container中的水平、垂直对齐方式

###### justify-items和align-items

指定grid items在grid cells中的对齐方式（如上图）

#### Grid items

##### grid-column和grid-row

指定该元素从哪条网格线延伸到哪条网格线

```css
/* 从第二条列网格线到第三条，即第二列 */
grid-column: 2 / 3;
/* 如果只占一列的话可以简写 */
grid-column: 2;
```

常用：

```css
/* 表示从第一条网格线一直延伸到最后 */
grid-column: 1 / -1;
```

##### justify-self和align-self

重写自身的`justify-items`和`align-items`属性
