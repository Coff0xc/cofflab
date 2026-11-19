<?php
// CVE-2026-115560 lab — vulnerable application endpoint.
//
// LabGadget stands in for ANY real application/library class with a dangerous
// magic method reachable at unserialize() time (Monolog, Guzzle, PhpOption,
// ...). Object injection only needs one such class in scope.
class LabGadget {
    public $cmd = null;
    public function __destruct() {
        if (is_string($this->cmd) && $this->cmd !== '') {
            @shell_exec($this->cmd);
        }
    }
}

// Precondition #2 (advisory): the application switches the serialize handler
// at runtime with ini_set() before session_start(), while the server config
// uses php_serialize. rfc1867 (pre-RINIT) already wrote the session file with
// the server handler => format mismatch on this read.
ini_set('session.serialize_handler', 'php');
session_start();

header('Content-Type: text/plain');
echo "ok\n";
echo "session_id=" . session_id() . "\n";
echo "serialize_handler(runtime)=" . ini_get('session.serialize_handler') . "\n";
