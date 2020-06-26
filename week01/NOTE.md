学习笔记
世界你好
照虎画猫总算弄完了，基础不好，好多步骤都想不明白
movies = Selector(response=response).xpath("//dd")[:10] 这条语句为啥非要用Select(response=response),这是选择器吧，response.xpath这也是选择器，用这也能找到想要的东西，为啥还要多一步select()这个？？？？？？？看了半天好像唯一的有点就是，这个select可以自动编译html或xml，是这个用途吗？
