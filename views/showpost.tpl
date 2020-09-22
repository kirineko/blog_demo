<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>文章详情</title>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.min.js"></script>
    <style>
        .post-tag {
            margin-right: 20px;
        }
    </style>
</head>
<body>
ID:
<span id='post-id'>{{ post_id }}</span>

<br>

标题:

{{ post_data['title'] }}

<br>

内容:

{{ post_data['content'] }}

<br>


作者:

{{ post_data['author'] }}

<br>

发布时间:

{{ post_data['ctime'] }}

<br>

访问量:

{{ visit_times }}

<div>
    <h4>tags:</h4>
    <div id="tags-list">
        % for tag in tags:
            <a class='post-tag' href='/tag/show/{{tag}}'>{{tag}}</a>
        % end
    </div>
</div>

<div>
    <input type="text" id="tag">
    <button id="addtag">添加标签</button>
</div>

<script>
    $('#addtag').click(() => {
        let post_id = $('#post-id').text()
        let tag = $('#tag').val()
        let data = {
            'post_id' : post_id,
            'tag' : tag
        }
        $.post('/tags/add', data, (result)=>{
            $('#tags-list').empty() 
            let tags = result.tags
            for (const tag of tags) {
                $('#tags-list').append(`<a class='post-tag' href='/tag/show/${tag}'>${tag}</a>`)
            }
        })
    })
</script>
</body>
</html>