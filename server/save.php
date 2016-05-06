<?php
error_reporting(E_ALL);

$id    = isset($_GET['id'])    ? $_GET['id']    : '';
$alpha = isset($_GET['alpha']) ? $_GET['alpha'] : '';
$beta  = isset($_GET['beta'])  ? $_GET['beta']  : '';
$gamma = isset($_GET['gamma']) ? $_GET['gamma'] : '';

$error = '';

// id のバリデーション
if (!preg_match('/^[a-zA-Z0-9_]{1,15}$/', $id)) {
    $error = 'id が不正です。';
} else {
    // alpha, beta, gamma が正しそうだったらファイルへ保存
    $pattern = '/^-?[0-9]+\.?[0-9]*$/';
    if (!preg_match($pattern, $alpha) || !preg_match($pattern, $beta) || !preg_match($pattern, $gamma)) {
        $error = '値が不正です。';
    } else {
        // ファイル名 "$id.json" に保存
        var_dump(dirname(__FILE__) . "/data/$id.json");
        $fp = fopen(dirname(__FILE__) . "/data/$id.json", 'w');
        var_dump($fp);
        fwrite($fp, "{ \"alpha\": $alpha, \"beta\": $beta, \"gamma\": $gamma }\n");
        fclose($fp);
    }
}

// ヘッダ送信
if ($error === '') {
    header('HTTP/1.1 200 OK');
} else {
    header('HTTP/1.1 400 Bad Request');
    echo $error;
    exit;
}
