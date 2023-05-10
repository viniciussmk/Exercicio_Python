<?php

$usuario = $_POST["usuario"] ?? null;
$senha = $_POST["senha"] ?? null;
$nomeArquivo = $_POST["nome_arquivo"] ?? null;

if (!$usuario || !$senha || !$nomeArquivo) {
    echo "Por favor, preencha todos os campos corretamente.";
    exit;
}

// Verifica se o arquivo de usuários já existe
if (!file_exists("usuarios/" . $nomeArquivo . ".txt")) {
    // Cria o arquivo de usuários se ele não existir
    file_put_contents("usuarios/" . $nomeArquivo . ".txt", "");
}

// Verifica se o usuário já existe
$usuarios = file("usuarios/" . $nomeArquivo . ".txt", FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
foreach ($usuarios as $usuarioExistente) {
    $usuarioExistente = explode(":", $usuarioExistente);
    if ($usuarioExistente[0] === $usuario) {
        echo "usuario_exist";
        exit;
    }
}

// Cadastra o usuário
$usuarioParaSalvar = $usuario . ":" . $senha . "\n";
if (file_put_contents("usuarios/" . $nomeArquivo . ".txt", $usuarioParaSalvar, FILE_APPEND)) {
    echo "sucesso";
} else {
    echo "Erro ao cadastrar usuário.";
}
