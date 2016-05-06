<?php
$id = isset($_GET['id']) ? $_GET['id'] : '';

$error = '';

// id のバリデーション
if (!preg_match('/^[a-zA-Z0-9_]{1,15}$/', $id)) {
    $error = 'id が不正です。';
}

// ヘッダ送信
if ($error === '') {
    header('HTTP/1.1 200 OK');
} else {
    header('HTTP/1.1 400 Bad Request');
    echo $error;
    exit;
}

?><!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Raspberry Pi Driving</title>

<script src="https://code.jquery.com/jquery-1.12.3.min.js"></script>
<script>
// デバイスの回転を取得する
var alpha, beta, gamma;
window.addEventListener('deviceorientation', function(event) {
    alpha = event.alpha;
    beta = event.beta;
    gamma = event.gamma;
    $('#alpha').text(alpha);
    $('#beta').text(beta);
    $('#gamma').text(gamma);
}, false);
// 500 ms (= 0.5 sec) ごとにサーバに送り返す
setInterval(function() {
    $.ajax({
        url: './save?id=<?php echo $id; ?>&alpha=' + alpha + '&beta=' + beta + '&gamma=' + gamma
    });
}, 500);
</script>

    </head>
    <body>
        alpha=<span id="alpha"></span><br>
        beta=<span id="beta"></span><br>
        gamma=<span id="gamma"></span><br>
    </body>
</html>
