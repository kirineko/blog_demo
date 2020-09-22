<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tag List</title>
</head>
<body>
    <h2>
        TAG: {{ tag }}
    </h2>
    <hr>
    <table border="1">
        <tr>
            <th>id</th>
            <th>标题</th>
            <th>作者</th>
            <th>发表时间</th>
        </tr>
        % for id, post in posts.items():
            <tr>
                <td>{{ id }}</td>
                <td><a href="/post/show/{{post['slug']}}">{{ post['title'] }}</a></td>
                <td>{{ post['author']}}</td>
                <td>{{ post['ctime']}}</td>
            </tr>
        % end
    </table>
</body>
</html>