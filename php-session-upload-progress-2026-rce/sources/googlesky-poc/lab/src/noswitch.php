<?php
// Control endpoint: identical to index.php but WITHOUT the runtime handler
// switch. The session file is read back with the same php_serialize handler
// that wrote it => no mismatch => the injected '|' key is harmless.
class LabGadget {
    public $cmd = null;
    public function __destruct() {
        if (is_string($this->cmd) && $this->cmd !== '') {
            @shell_exec($this->cmd);
        }
    }
}

session_start();

header('Content-Type: text/plain');
echo "ok\n";
echo "session_id=" . session_id() . "\n";
echo "serialize_handler(runtime)=" . ini_get('session.serialize_handler') . "\n";
