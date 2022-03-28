Gem::Specification.new do |spec|
  spec.name          = 'vwo_log_messages'
  spec.version       = '0.7.5'
  spec.authors       = ['VWO']
  spec.email         = ['dev@wingify.com']

  spec.summary       = "VWO log messages for VWO FullStack testing SDKs"
  spec.description   = "VWO log messages for VWO FullStack testing SDKs"
  spec.homepage      = 'https://vwo.com/fullstack/server-side-testing/'
  spec.license       = 'Apache-2.0'

  spec.files          = Dir['lib/**/*', 'src/**/*']
  spec.require_paths = ['lib', 'src']

  spec.metadata = {
  }

  spec.required_ruby_version = '>= 2.2.10'
end
