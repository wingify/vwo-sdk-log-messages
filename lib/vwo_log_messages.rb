class VwoLogMessages
  def self.getMessage
      return {
          'debug_logs' => JSON.load(File.open(File.join(File.dirname(__FILE__), '../src/debug-messages.json'))),
          'error_logs' => JSON.load(File.open(File.join(File.dirname(__FILE__), '../src/error-messages.json'))),
          'info_logs' => JSON.load(File.open(File.join(File.dirname(__FILE__), '../src/info-messages.json'))),
          'warning_logs' => JSON.load(File.open(File.join(File.dirname(__FILE__), '../src/warning-messages.json')))
      }
  end
end
