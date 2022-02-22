<?php

namespace vwo;

class VwoSdkLogMessages {

  public static function get()
  {
    return [
      "debugLogs" => json_decode(file_get_contents("debug-messages.json"), true),
      "infoLogs" => json_decode(file_get_contents("info-messages.json"), true),
      "errorLogs" => json_decode(file_get_contents("error-messages.json"), true),
      "warnLogs" => json_decode(file_get_contents("warning-messages.json"), true)
    ];
  }
}
