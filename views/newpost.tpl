<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>发布文章</title>
</head>
<body>
    {{get('tips', '')}}
    <form action="/post/deal" method="post">
        <h3>标题</h3>
        <input type="text" name="title" id="">
        <br>
        <h3>缩略词(English ONLY)</h3>
        <input type="text" name="slug" id="">
        <br>
        <h3>正文</h3>
        <textarea name="content" id="" cols="30" rows="10"></textarea>
        <br>
        <h3>作者</h3>
        <input type="text" name="author" id="">
        <br>
        <button type="submit">发布文章</button>
    </form>
</body>
</html>