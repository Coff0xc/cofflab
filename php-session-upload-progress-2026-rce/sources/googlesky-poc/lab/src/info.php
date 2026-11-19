<?php
// Config introspection for `poc.py check`. Does NOT switch handlers: reports
// the server-level (global) values that rfc1867 will actually use pre-RINIT.
$all = ini_get_all('session');
$g = function (string $k) use ($all) { return $all[$k]['global_value'] ?? null; };
header('Content-Type: application/json');
echo json_encode([
    'php_version'                 => PHP_VERSION,
    'sapi'                        => PHP_SAPI,
    'serialize_handler_global'    => $g('session.serialize_handler'),
    'upload_progress_enabled'     => $g('session.upload_progress.enabled'),
    'upload_progress_cleanup'     => $g('session.upload_progress.cleanup'),
    'upload_progress_name'        => $g('session.upload_progress.name'),
    'upload_progress_prefix'      => $g('session.upload_progress.prefix'),
    'use_only_cookies'            => $g('session.use_only_cookies'),
    'use_strict_mode'             => $g('session.use_strict_mode'),
    'save_path'                   => $g('session.save_path'),
], JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES) . "\n";
