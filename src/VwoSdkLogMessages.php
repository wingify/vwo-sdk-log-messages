<?php

namespace vwo;

class VwoSdkLogMessages {

  public static function get()
  {
    return [
      "debugLogs" => json_decode(file_get_contents(__DIR__ . "/debug-messages.json"), true),
      "infoLogs" => json_decode(file_get_contents(__DIR__ . "/info-messages.json"), true),
      "errorLogs" => json_decode(file_get_contents(__DIR__ . "/error-messages.json"), true),
      "warnLogs" => json_decode(file_get_contents(__DIR__ . "/warning-messages.json"), true)
    ];
  }
}
