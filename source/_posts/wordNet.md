---
title: WordNet使用简介
categories: [教程, NLP]
tags: [教程, NLP, WordNet]
index_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20230428_bg1.jpg
banner_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20230428_bg1.jpg
---

> WordNet is a large lexical database of English. Nouns, verbs, adjectives and adverbs are grouped into sets of cognitive synonyms (synsets), each expressing a distinct concept.

<!-- more -->

### 介绍

1. WordNet的基本元素是**synset**，是由一个或多个语义相近的单词构成的同义词组。

2. 对于一词多义的单词来说，它会出现在多个对应的synset中。

3. 单词被分为NOUN, VERB, ADJ和ADV，各自组成一个语义网络，互相没有连接。

4. synset中的元素称为**lemma**，即词根，标志着WordNet只会记录词元而不会记录其时态的变换。

对于名词来说，synset被组织成树形结构，每一个synset都有对应的上位词集 (**hypernyms**) 和下位词集 (**hyponyms**)。所有名词词集的祖先都是{entity}。

在WordNet中，每一个synset表示为**单词.词性.序号**，即用词集中的一个单词来表示这一synset，序号则代表这一synset是这一单词的第几个含义。

与之相对应，lemma表示为**单词.词性.序号.词根**，这样便可唯一表示单词的每一个含义。



### WordNet安装（Python）

#### [官网地址](https://wordnet.princeton.edu/)

在官网可以使用图形化界面在线使用和查询。

#### 安装

```bash
pip3 install nltk
```

```python
import nltk
nltk.download('wordnet')
```

```python
from nltk.corpus import wordnet as wn
```



### 常用API

#### 查看单词的所有synset

```python
>>> wn.synsets("chair")
[Synset('chair.n.01'),Synset('professorship.n.01'),Synset('president.n.04'),Synset('electric_chair.n.01'),Synset('chair.n.05'),Synset('chair.v.01'),Synset('moderate.v.01')]
```
表示单词chair出现在7个不同的synset中，即有7种不同的含义。

pos属性可以指定词性查询：

```python
>>> wn.synsets("chair", pos=wn.NOUN)
[Synset('chair.n.01'),Synset('professorship.n.01'),Synset('president.n.04'),Synset('electric_chair.n.01'),Synset('chair.n.05')]
```

调用synset的definition()可以查看词集的简要描述：

```python
>>> for synset in wn.synsets("chair"):
    	print(synset.name()+ " ------ " + synset.definition())
```

```
chair.n.01 ------ a seat for one person, with a support for the back
professorship.n.01 ------ the position of professor
president.n.04 ------ the officer who presides at the meetings of an organization
electric_chair.n.01 ------ an instrument of execution by electrocution; resembles an ordinary seat for one person
chair.n.05 ------ a particular seat in an orchestra
chair.v.01 ------ act or preside as chair, as of an academic department in a university
moderate.v.01 ------ preside over
```

调用examples()可以查看例句（例句中的单词可以是synsey中的任意一个）

```python
>>> for synset in wn.synsets("chair"):
    	print(synset.name()+ " ------ " + str(synset.examples()))
```

```
chair.n.01 ------ ['he put his coat over the back of the chair and sat down']
professorship.n.01 ------ ['he was awarded an endowed chair in economics']
president.n.04 ------ ['address your remarks to the chairperson']
electric_chair.n.01 ------ ['the murderer was sentenced to die in the chair']
chair.n.05 ------ ['he is second chair violin']
chair.v.01 ------ ['She chaired the department for many years']
moderate.v.01 ------ ['John moderated the discussion']
```

#### 查看synset中有哪些单词 (lemma)

```python
>>> for synset in wn.synsets('chair'):
    	print(synset.name()+ " ------ " + str(synset.lemmas()))
```

```
chair.n.01 ------ [Lemma('chair.n.01.chair')]
professorship.n.01 ------ [Lemma('professorship.n.01.professorship'), Lemma('professorship.n.01.chair')]
president.n.04 ------ [Lemma('president.n.04.president'), Lemma('president.n.04.chairman'), Lemma('president.n.04.chairwoman'), Lemma('president.n.04.chair'), Lemma('president.n.04.chairperson')]
electric_chair.n.01 ------ [Lemma('electric_chair.n.01.electric_chair'), Lemma('electric_chair.n.01.chair'), Lemma('electric_chair.n.01.death_chair'), Lemma('electric_chair.n.01.hot_seat')]
chair.n.05 ------ [Lemma('chair.n.05.chair')]
chair.v.01 ------ [Lemma('chair.v.01.chair'), Lemma('chair.v.01.chairman')]
moderate.v.01 ------ [Lemma('moderate.v.01.moderate'), Lemma('moderate.v.01.chair'), Lemma('moderate.v.01.lead')]
```

```python
>>> for synset in wn.synsets('chair'):
    	print(synset.name()+ " ------ " + str(synset.lemma_names()))
```

```
chair.n.01 ------ ['chair']
professorship.n.01 ------ ['professorship', 'chair']
president.n.04 ------ ['president', 'chairman', 'chairwoman', 'chair', 'chairperson']
electric_chair.n.01 ------ ['electric_chair', 'chair', 'death_chair', 'hot_seat']
chair.n.05 ------ ['chair']
chair.v.01 ------ ['chair', 'chairman']
moderate.v.01 ------ ['moderate', 'chair', 'lead']
```

#### 计算两个synset之间的similarity

计算similarity有很多不同的方法，详见[官方文档](https://www.nltk.org/howto/wordnet.html)

##### path_similarity

```python
 def path_similarity(self, other, verbose=False, simulate_root=True):
        """
        Path Distance Similarity:
        Return a score denoting how similar two word senses are, based on the
        shortest path that connects the senses in the is-a (hypernym/hypnoym)
        taxonomy. The score is in the range 0 to 1, except in those cases where
        a path cannot be found (will only be true for verbs as there are many
        distinct verb taxonomies), in which case None is returned. A score of
        1 represents identity i.e. comparing a sense with itself will return 1.
        :type other: Synset
        :param other: The ``Synset`` that this ``Synset`` is being compared to.
        :type simulate_root: bool
        :param simulate_root: The various verb taxonomies do not
            share a single root which disallows this metric from working for
            synsets that are not connected. This flag (True by default)
            creates a fake root that connects all the taxonomies. Set it
            to false to disable this behavior. For the noun taxonomy,
            there is usually a default root except for WordNet version 1.6.
            If you are using wordnet 1.6, a fake root will be added for nouns
            as well.
        :return: A score denoting the similarity of the two ``Synset`` objects,
            normally between 0 and 1. None is returned if no connecting path
            could be found. 1 is returned if a ``Synset`` is compared with
            itself.
        """

        distance = self.shortest_path_distance(
            other,
            simulate_root=simulate_root and (self._needs_root() or other._needs_root()),
        )
        if distance is None or distance < 0:
            return None
        return 1.0 / (distance + 1)

```

该函数通过两个词集距离其公共祖先的距离之和 (即源码中的 *distance*) 计算相似度，如果没有公共节点（如词性不一致），则会创建一个虚拟根节点来计算。

```python
>>> chair = wn.synset('chair.n.01')
>>> president = wn.synset('president.n.01')
>>> chair.path_similarity(president)
0.0625
```

#### 查看两个synset的最近公共祖先

```python
>>> chair.lowest_common_hypernyms(president)
[Synset('whole.n.02')]
>>> chair.lowest_common_hypernyms(president)[0].definition()
'an assemblage of parts that is regarded as a single entity'
```

#### 查看synset的上位词集和下位词集

```python
>>> for synset in wn.synsets('room'):
    	print(synset.name()+ " ------ " + str(synset.hypernyms()))
```

```
room.n.01 ------ [Synset('area.n.05')]
room.n.02 ------ [Synset('position.n.07')]
room.n.03 ------ [Synset('opportunity.n.01')]
room.n.04 ------ [Synset('gathering.n.01')]
board.v.02 ------ [Synset('populate.v.01')]
```

```python
>>> for synset in wn.synsets('room'):
    	print(synset.name()+ " ------ " + str(synset.hyponyms()))
```

```
room.n.01 ------ [Synset('anechoic_chamber.n.01'), Synset('anteroom.n.01'), Synset('back_room.n.01'), ...]
room.n.02 ------ [Synset('breathing_room.n.01'), Synset('headroom.n.01'), Synset('houseroom.n.01'), ...]
room.n.03 ------ []
room.n.04 ------ []
board.v.02 ------ []
```

#### lemma之间的关系 (synonym/antonym)

```python
>>> wn.lemma("hot.a.01.hot").antonyms()
[Lemma('cold.a.01.cold')]
```

```python
>>> wn.synonyms("chair")
[[], ['professorship'], ['chairman', 'chairperson', 'chairwoman', 'president'], ['death_chair', 'electric_chair', 'hot_seat'], [], ['chairman'], ['lead', 'moderate']]
```

可以看到同义词仅仅是单词所在的synset中除了这一个外的所有单词



### Reference

[官方文档](https://www.nltk.org/howto/wordnet.html)

[WordNet源码](https://github.com/nltk/nltk/blob/develop/nltk/corpus/reader/wordnet.py)

https://www.cnblogs.com/Xiaoyan-Li/p/13477253.html

https://www.jianshu.com/p/11628d249c1c

