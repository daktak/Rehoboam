AR = 'arm-none-eabi-ar'
ARFLAGS = 'rcs'
AS = 'arm-none-eabi-gcc'
BINDIR = '/usr/local/bin'
BLOCK_MESSAGE_KEYS = []
BUILD_DIR = 'diorite'
BUILD_TYPE = 'app'
BUNDLE_BIN_DIR = 'diorite'
BUNDLE_NAME = 'Rehoboam.pbw'
CC = ['arm-none-eabi-gcc']
CCLNK_SRC_F = []
CCLNK_TGT_F = ['-o']
CC_NAME = 'gcc'
CC_SRC_F = []
CC_TGT_F = ['-c', '-o']
CC_VERSION = ('4', '7', '2')
CFLAGS = ['-std=c99', '-mcpu=cortex-m3', '-mthumb', '-ffunction-sections', '-fdata-sections', '-g', '-fPIE', '-Os', '-D_TIME_H_', '-Wall', '-Wextra', '-Werror', '-Wno-unused-parameter', '-Wno-error=unused-function', '-Wno-error=unused-variable']
CFLAGS_MACBUNDLE = ['-fPIC']
CFLAGS_cshlib = ['-fPIC']
CPPPATH_ST = '-I%s'
DEFINES = ['RELEASE', 'PBL_PLATFORM_DIORITE', 'PBL_BW', 'PBL_RECT', 'PBL_MICROPHONE', 'PBL_HEALTH', 'PBL_SMARTSTRAP', 'PBL_DISPLAY_WIDTH=144', 'PBL_DISPLAY_HEIGHT=168', 'PBL_SDK_3']
DEFINES_ST = '-D%s'
DEST_BINFMT = 'elf'
DEST_CPU = 'arm'
DEST_OS = 'linux'
INCLUDES = ['diorite']
LD = 'arm-none-eabi-ld'
LIBDIR = '/usr/local/lib'
LIBPATH_ST = '-L%s'
LIB_DIR = 'node_modules'
LIB_JSON = [{u'_location': u'/pebble-fctx-compiler', u'_spec': u'pebble-fctx-compiler@^1.2.2', u'_integrity': u'sha1-H01+OzTQIOGJB6Rn1km4wdYA0hk=', u'keywords': [u'pebble-package'], u'_from': u'pebble-fctx-compiler@^1.2.2', u'bundleDependencies': False, u'engines': {u'node': u'*'}, u'_phantomChildren': {}, u'version': u'1.2.2', u'_resolved': u'https://registry.npmjs.org/pebble-fctx-compiler/-/pebble-fctx-compiler-1.2.2.tgz', u'_inBundle': False, u'homepage': u'https://github.com/jrmobley/pebble-fctx-compiler#readme', u'bin': {u'fctx-compiler': u'./fctx-compiler.js'}, u'_requested': {u'name': u'pebble-fctx-compiler', u'escapedName': u'pebble-fctx-compiler', u'saveSpec': None, u'rawSpec': u'^1.2.2', u'raw': u'pebble-fctx-compiler@^1.2.2', u'registry': True, u'fetchSpec': u'^1.2.2', u'type': u'range'}, u'description': u'Compiles SVG resources into a binary format for the pebble-fctx library.', u'repository': {u'url': u'git+https://github.com/jrmobley/pebble-fctx-compiler.git'}, u'_requiredBy': [u'/'], u'dependencies': {u'svg-path-parser': u'1.0.1', u'colors': u'^1.1.0', u'xml2js': u'^0.4.9', u'underscore': u'^1.8.3', u'minimist': u'^1.2.0'}, u'name': u'pebble-fctx-compiler', u'license': u'MIT', u'deprecated': False, u'author': {u'name': u'JR Mobley'}, u'bugs': {u'url': u'https://github.com/jrmobley/pebble-fctx-compiler/issues'}, 'js_paths': ['node_modules/pebble-fctx-compiler/fctx-compiler.js', 'node_modules/pebble-fctx-compiler/package.json'], u'_where': u'/home/astosia/pebble-dev/pebble-sdk-4.5-linux64/rehoboam', u'_id': u'pebble-fctx-compiler@1.2.2', u'_shasum': u'1f4d7e3b34d020e18907a467d649b8c1d600d219'}, {u'_location': u'/pebble-fctx', u'_spec': u'pebble-fctx@^1.5.0', u'_integrity': u'sha1-S/D5S7CITRuE4n0+HYLHgenHwSQ=', u'keywords': [u'pebble-package'], u'_from': u'pebble-fctx@^1.5.0', u'pebble': {u'sdkVersion': u'3', u'projectType': u'package', u'targetPlatforms': [u'aplite', u'basalt', u'chalk', u'diorite', u'emery'], u'resources': {u'media': []}}, u'bundleDependencies': False, u'_phantomChildren': {}, u'version': u'1.6.2', u'_resolved': u'https://registry.npmjs.org/pebble-fctx/-/pebble-fctx-1.6.2.tgz', u'_inBundle': False, u'homepage': u'https://github.com/jrmobley/pebble-fctx#readme', u'files': [u'dist.zip'], u'_requested': {u'name': u'pebble-fctx', u'escapedName': u'pebble-fctx', u'saveSpec': None, u'rawSpec': u'^1.5.0', u'raw': u'pebble-fctx@^1.5.0', u'registry': True, u'fetchSpec': u'^1.5.0', u'type': u'range'}, u'description': u'This is a graphics library for the Pebble smart watch.', u'repository': {u'url': u'git+https://github.com/jrmobley/pebble-fctx.git', u'type': u'git'}, u'_requiredBy': [u'/'], u'dependencies': {u'pebble-utf8': u'^1.0.1'}, 'path': 'node_modules/pebble-fctx/dist', u'name': u'pebble-fctx', u'license': u'MIT', u'deprecated': False, u'author': {u'name': u'JR Mobley'}, u'bugs': {u'url': u'https://github.com/jrmobley/pebble-fctx/issues'}, u'_where': u'/home/astosia/pebble-dev/pebble-sdk-4.5-linux64/rehoboam', u'_id': u'pebble-fctx@1.6.2', u'_shasum': u'4bf0f94bb0884d1b84e27d3e1d82c781e9c7c124'}, {u'_location': u'/pebble-clay', u'_spec': u'pebble-clay@^1.0.4', u'_integrity': u'sha1-/fkvD9x3CpecBodOqiRXzC52I0Q=', u'keywords': [u'pebble', u'config', u'configuration', u'pebble-package'], u'devDependencies': {u'chai': u'^3.4.1', u'mocha': u'^2.3.4', u'through': u'^2.3.8', u'gulp-inline': u'0.0.15', u'karma-source-map-support': u'^1.1.0', u'deepcopy': u'^0.6.1', u'eslint-plugin-standard': u'^1.3.1', u'stringify': u'^3.2.0', u'gulp-insert': u'^0.5.0', u'gulp': u'^3.9.0', u'gulp-htmlmin': u'^1.3.0', u'deamdify': u'^0.2.0', u'bourbon': u'^4.2.6', u'eslint-config-pebble': u'^1.2.0', u'eslint': u'^1.5.1', u'karma-coverage': u'^0.5.3', u'watchify': u'^3.7.0', u'require-from-string': u'^1.1.0', u'gulp-sourcemaps': u'^1.6.0', u'karma-mocha': u'^0.2.1', u'sinon': u'^1.17.3', u'joi': u'^6.10.1', u'browserify': u'^13.0.0', u'sassify': u'^0.9.1', u'gulp-autoprefixer': u'^3.1.0', u'karma-mocha-reporter': u'^1.1.5', u'autoprefixer': u'^6.3.1', u'browserify-istanbul': u'^0.2.1', u'karma-threshold-reporter': u'^0.1.15', u'gulp-sass': u'^2.1.1', u'vinyl-source-stream': u'^1.1.0', u'gulp-uglify': u'^1.5.2', u'karma-chrome-launcher': u'^0.2.2', u'vinyl-buffer': u'^1.0.0', u'del': u'^2.0.2', u'karma': u'^0.13.19', u'karma-browserify': u'^5.0.1', u'tosource': u'^1.0.0', u'postcss': u'^5.0.14'}, u'_from': u'pebble-clay@^1.0.4', u'pebble': {u'sdkVersion': u'3', u'capabilities': [u'configurable'], u'projectType': u'package', u'targetPlatforms': [u'aplite', u'basalt', u'chalk', u'diorite', u'emery'], u'resources': {u'media': []}}, u'bundleDependencies': False, u'_phantomChildren': {}, u'version': u'1.0.4', u'_resolved': u'https://registry.npmjs.org/pebble-clay/-/pebble-clay-1.0.4.tgz', u'_inBundle': False, u'homepage': u'https://github.com/pebble/clay#readme', u'_requested': {u'name': u'pebble-clay', u'escapedName': u'pebble-clay', u'saveSpec': None, u'rawSpec': u'^1.0.4', u'raw': u'pebble-clay@^1.0.4', u'registry': True, u'fetchSpec': u'^1.0.4', u'type': u'range'}, u'description': u'Pebble Config Framework', u'repository': {u'url': u'git+https://github.com/pebble/clay.git', u'type': u'git'}, u'_requiredBy': [u'/'], u'dependencies': {}, u'scripts': {u'pebble-publish': u'npm run pebble-clean && npm run build && pebble build && pebble package publish && npm run pebble-clean', u'test-travis': u'gulp && ./node_modules/.bin/karma start ./test/karma.conf.js --single-run --browsers chromeTravisCI && ./node_modules/.bin/eslint ./', u'pebble-build': u'npm run build && pebble build', u'test-debug': u'(export DEBUG=true && ./node_modules/.bin/gulp && ./node_modules/.bin/karma start ./test/karma.conf.js --no-single-run)', u'lint': u'eslint ./', u'dev': u'gulp dev', u'build': u'gulp', u'test': u'gulp && ./node_modules/.bin/karma start ./test/karma.conf.js --single-run', u'pebble-clean': u'rm -rf tmp src/js/index.js && pebble clean'}, 'path': 'node_modules/pebble-clay/dist', u'name': u'pebble-clay', u'license': u'MIT', u'deprecated': False, u'author': {u'name': u'Pebble Technology'}, u'bugs': {u'url': u'https://github.com/pebble/clay/issues'}, 'js_paths': ['node_modules/pebble-clay/dist/js/index.js'], u'_where': u'/home/astosia/pebble-dev/pebble-sdk-4.5-linux64/rehoboam', u'_id': u'pebble-clay@1.0.4', u'_shasum': u'fdf92f0fdc770a979c06874eaa2457cc2e762344'}, {u'_location': u'/svg-path-parser', u'_spec': u'svg-path-parser@1.0.1', u'_integrity': u'sha1-Pln15dcNL8DXwX98xUe8PD+qwVc=', u'keywords': [u'svg', u'path', u'd', u'attribute', u'parser', u'lines', u'drawing'], u'devDependencies': {u'pegjs': u'~0.7.0'}, u'_from': u'svg-path-parser@1.0.1', u'bundleDependencies': False, u'_phantomChildren': {}, u'version': u'1.0.1', u'_resolved': u'https://registry.npmjs.org/svg-path-parser/-/svg-path-parser-1.0.1.tgz', u'main': u'index.js', u'homepage': u'https://github.com/hughsk/svg-path-parser#readme', u'_requested': {u'name': u'svg-path-parser', u'escapedName': u'svg-path-parser', u'saveSpec': None, u'rawSpec': u'1.0.1', u'raw': u'svg-path-parser@1.0.1', u'registry': True, u'fetchSpec': u'1.0.1', u'type': u'version'}, u'description': u"A parser for SVG's path syntax", u'repository': {u'url': u'git://github.com/hughsk/svg-path-parser.git', u'type': u'git'}, u'_requiredBy': [u'/pebble-fctx-compiler'], u'dependencies': {}, u'scripts': {u'prepublish': u'pegjs grammar.peg parser.js'}, u'_inBundle': False, u'name': u'svg-path-parser', u'deprecated': False, u'bugs': {u'url': u'https://github.com/hughsk/svg-path-parser/issues'}, 'js_paths': ['node_modules/svg-path-parser/index.js', 'node_modules/svg-path-parser/package.json', 'node_modules/svg-path-parser/parser.js'], u'_where': u'/home/astosia/pebble-dev/pebble-sdk-4.5-linux64/rehoboam/node_modules/pebble-fctx-compiler', u'_id': u'svg-path-parser@1.0.1', u'_shasum': u'3e59f5e5d70d2fc0d7c17f7cc547bc3c3faac157'}, {u'_location': u'/colors', u'contributors': [{u'url': u'https://github.com/DABH', u'name': u'DABH'}], u'_spec': u'colors@^1.1.0', u'_integrity': u'sha512-a+UqTh4kgZg/SlGvfbzDHpgRu7AAQOmmqRHJnxhRZICKFUT91brVhNNt58CMWU9PsBbv3PDCZUHbVxuDiH2mtA==', u'keywords': [u'ansi', u'terminal', u'colors'], u'devDependencies': {u'eslint': u'^5.2.0', u'eslint-config-google': u'^0.11.0'}, u'_from': u'colors@^1.1.0', u'bundleDependencies': False, u'engines': {u'node': u'>=0.1.90'}, u'_phantomChildren': {}, u'version': u'1.4.0', u'_resolved': u'https://registry.npmjs.org/colors/-/colors-1.4.0.tgz', u'_inBundle': False, u'homepage': u'https://github.com/Marak/colors.js', u'files': [u'examples', u'lib', u'LICENSE', u'safe.js', u'themes', u'index.d.ts', u'safe.d.ts'], u'_requested': {u'name': u'colors', u'escapedName': u'colors', u'saveSpec': None, u'rawSpec': u'^1.1.0', u'raw': u'colors@^1.1.0', u'registry': True, u'fetchSpec': u'^1.1.0', u'type': u'range'}, u'description': u'get colors in your node.js console', u'repository': {u'url': u'git+ssh://git@github.com/Marak/colors.js.git', u'type': u'git'}, u'_requiredBy': [u'/pebble-fctx-compiler'], u'scripts': {u'test': u'node tests/basic-test.js && node tests/safe-test.js', u'lint': u'eslint . --fix'}, u'main': u'lib/index.js', u'name': u'colors', u'license': u'MIT', u'deprecated': False, u'author': {u'name': u'Marak Squires'}, u'bugs': {u'url': u'https://github.com/Marak/colors.js/issues'}, 'js_paths': ['node_modules/colors/examples/normal-usage.js', 'node_modules/colors/examples/safe-string.js', 'node_modules/colors/lib/colors.js', 'node_modules/colors/lib/custom/trap.js', 'node_modules/colors/lib/custom/zalgo.js', 'node_modules/colors/lib/extendStringPrototype.js', 'node_modules/colors/lib/index.js', 'node_modules/colors/lib/maps/america.js', 'node_modules/colors/lib/maps/rainbow.js', 'node_modules/colors/lib/maps/random.js', 'node_modules/colors/lib/maps/zebra.js', 'node_modules/colors/lib/styles.js', 'node_modules/colors/lib/system/has-flag.js', 'node_modules/colors/lib/system/supports-colors.js', 'node_modules/colors/package.json', 'node_modules/colors/safe.js', 'node_modules/colors/themes/generic-logging.js'], u'_where': u'/home/astosia/pebble-dev/pebble-sdk-4.5-linux64/rehoboam/node_modules/pebble-fctx-compiler', u'_id': u'colors@1.4.0', u'_shasum': u'c50491479d4c1bdaed2c9ced32cf7c7dc2360f78'}, {u'_location': u'/xml2js', u'contributors': [{u'url': u'https://github.com/maqr', u'name': u'maqr', u'email': u'maqr.lollerskates@gmail.com'}, {u'url': u'http://benweaver.com/', u'name': u'Ben Weaver'}, {u'url': u'https://github.com/jaekwon', u'name': u'Jae Kwon'}, {u'name': u'Jim Robert'}, {u'url': u'http://www.saltwaterc.eu/', u'name': u'\u0218tefan Rusu'}, {u'url': u'http://cartercole.com/', u'name': u'Carter Cole', u'email': u'carter.cole@cartercole.com'}, {u'url': u'http://www.kurtraschke.com/', u'name': u'Kurt Raschke', u'email': u'kurt@kurtraschke.com'}, {u'url': u'https://github.com/Contra', u'name': u'Contra', u'email': u'contra@australia.edu'}, {u'url': u'https://github.com/mdiniz', u'name': u'Marcelo Diniz', u'email': u'marudiniz@gmail.com'}, {u'url': u'https://github.com/mhart', u'name': u'Michael Hart'}, {u'url': u'http://zacharyscott.net/', u'name': u'Zachary Scott', u'email': u'zachary@zacharyscott.net'}, {u'url': u'https://github.com/raoulmillais', u'name': u'Raoul Millais'}, {u'url': u'http://www.salsitasoft.com/', u'name': u'Salsita Software'}, {u'url': u'http://www.emotive.com/', u'name': u'Mike Schilling', u'email': u'mike@emotive.com'}, {u'url': u'http://weibo.com/shyvo', u'name': u'Jackson Tian', u'email': u'shyvo1987@gmail.com'}, {u'url': u'https://github.com/Sitin', u'name': u'Mikhail Zyatin', u'email': u'mikhail.zyatin@gmail.com'}, {u'url': u'https://github.com/christav', u'name': u'Chris Tavares', u'email': u'ctavares@microsoft.com'}, {u'url': u'http://f2e.us/', u'name': u'Frank Xu', u'email': u'yyfrankyy@gmail.com'}, {u'url': u'http://www.bitstorm.it/', u'name': u"Guido D'Albore", u'email': u'guido@bitstorm.it'}, {u'url': u'http://jacksenechal.com/', u'name': u'Jack Senechal'}, {u'url': u'https://github.com/hoelzl', u'name': u'Matthias H\xf6lzl', u'email': u'tc@xantira.com'}, {u'url': u'http://www.creynders.be/', u'name': u'Camille Reynders', u'email': u'info@creynders.be'}, {u'url': u'https://github.com/tsgautier', u'name': u'Taylor Gautier'}, {u'url': u'https://github.com/toddrbryan', u'name': u'Todd Bryan'}, {u'url': u'http://leoreavidar.com/', u'name': u'Leore Avidar', u'email': u'leore.avidar@gmail.com'}, {u'url': u'http://www.actionshrimp.com/', u'name': u'Dave Aitken', u'email': u'dave.aitken@gmail.com'}, {u'name': u'Shaney Orrowe', u'email': u'shaney.orrowe@practiceweb.co.uk'}, {u'name': u'Candle', u'email': u'candle@candle.me.uk'}, {u'url': u'http://jes.st', u'name': u'Jess Telford', u'email': u'hi@jes.st'}, {u'url': u'http://compton.nu/', u'name': u'Tom Hughes', u'email': u'<tom@compton.nu'}, {u'url': u'http://rocha.la/', u'name': u'Piotr Rochala'}, {u'url': u'https://github.com/michaelavila', u'name': u'Michael Avila'}, {u'url': u'https://github.com/ryedin', u'name': u'Ryan Gahl'}, {u'url': u'https://github.com/elaberge', u'name': u'Eric Laberge', u'email': u'e.laberge@gmail.com'}, {u'url': u'https://twitter.com/benjamincoe', u'name': u'Benjamin E. Coe', u'email': u'ben@npmjs.com'}, {u'url': u'https://github.com/cressie176', u'name': u'Stephen Cresswell'}, {u'url': u'http://www.hacksrus.net/', u'name': u'Pascal Ehlert', u'email': u'pascal@hacksrus.net'}, {u'url': u'http://fiznool.com/', u'name': u'Tom Spencer', u'email': u'fiznool@gmail.com'}, {u'url': u'https://github.com/tflanagan', u'name': u'Tristian Flanagan', u'email': u'tflanagan@datacollaborative.com'}, {u'url': u'https://github.com/TimJohns', u'name': u'Tim Johns', u'email': u'timjohns@yahoo.com'}, {u'url': u'https://github.com/TrySound', u'name': u'Bogdan Chadkin', u'email': u'trysound@yandex.ru'}, {u'url': u'http://codesleuth.co.uk/', u'name': u'David Wood', u'email': u'david.p.wood@gmail.com'}, {u'url': u'https://github.com/nmaquet', u'name': u'Nicolas Maquet'}, {u'url': u'http://lovell.info/', u'name': u'Lovell Fuller'}, {u'url': u'https://github.com/d3adc0d3', u'name': u'd3adc0d3'}], u'_spec': u'xml2js@^0.4.9', u'_integrity': u'sha512-ySPiMjM0+pLDftHgXY4By0uswI3SPKLDw/i3UXbnO8M/p28zqexCUoPmQFrYD+/1BzhGJSs2i1ERWKJAtiLrug==', u'keywords': [u'xml', u'json'], u'devDependencies': {u'coffee-script': u'>=1.10.0', u'coveralls': u'^3.0.1', u'diff': u'>=1.0.8', u'nyc': u'>=2.2.1', u'docco': u'>=0.6.2', u'zap': u'>=0.2.9'}, u'_from': u'xml2js@^0.4.9', u'bundleDependencies': False, u'engines': {u'node': u'>=4.0.0'}, u'_phantomChildren': {}, u'version': u'0.4.23', u'_resolved': u'https://registry.npmjs.org/xml2js/-/xml2js-0.4.23.tgz', u'_inBundle': False, u'homepage': u'https://github.com/Leonidas-from-XIV/node-xml2js', u'files': [u'lib'], u'_requested': {u'name': u'xml2js', u'escapedName': u'xml2js', u'saveSpec': None, u'rawSpec': u'^0.4.9', u'raw': u'xml2js@^0.4.9', u'registry': True, u'fetchSpec': u'^0.4.9', u'type': u'range'}, u'description': u'Simple XML to JavaScript object converter.', u'repository': {u'url': u'git+https://github.com/Leonidas-from-XIV/node-xml2js.git', u'type': u'git'}, u'_requiredBy': [u'/pebble-fctx-compiler'], u'dependencies': {u'sax': u'>=0.6.0', u'xmlbuilder': u'~11.0.0'}, u'scripts': {u'test': u'zap', u'doc': u'cake doc', u'coveralls': u'nyc npm test && nyc report --reporter=text-lcov | coveralls', u'build': u'cake build', u'coverage': u'nyc npm test && nyc report'}, u'main': u'./lib/xml2js', u'name': u'xml2js', u'license': u'MIT', u'deprecated': False, u'directories': {u'lib': u'./lib'}, u'author': {u'url': u'https://xivilization.net', u'name': u'Marek Kubica', u'email': u'marek@xivilization.net'}, u'bugs': {u'url': u'https://github.com/Leonidas-from-XIV/node-xml2js/issues'}, 'js_paths': ['node_modules/xml2js/lib/bom.js', 'node_modules/xml2js/lib/builder.js', 'node_modules/xml2js/lib/defaults.js', 'node_modules/xml2js/lib/parser.js', 'node_modules/xml2js/lib/processors.js', 'node_modules/xml2js/lib/xml2js.js', 'node_modules/xml2js/package.json'], u'_where': u'/home/astosia/pebble-dev/pebble-sdk-4.5-linux64/rehoboam/node_modules/pebble-fctx-compiler', u'_id': u'xml2js@0.4.23', u'_shasum': u'a0c69516752421eb2ac758ee4d4ccf58843eac66'}, {u'_location': u'/underscore', u'_spec': u'underscore@^1.8.3', u'module': u'modules/index-all.js', u'_integrity': u'sha512-N4P+Q/BuyuEKFJ43B9gYuOj4TQUHXX+j2FqguVOpjkssLUUrnJofCcBccJSCoeturDoZU6GorDTHSvUDlSQbTg==', u'keywords': [u'util', u'functional', u'server', u'client', u'browser'], u'devDependencies': {u'nyc': u'^2.1.3', u'karma-sauce-launcher': u'^1.2.0', u'coveralls': u'^2.11.2', u'qunit': u'^2.6.0', u'pretty-bytes-cli': u'^1.0.0', u'rollup': u'^0.59.4', u'gzip-size-cli': u'^1.0.0', u'docco': u'*', u'qunit-cli': u'~0.2.0', u'eslint': u'^6.8.0', u'karma-qunit': u'~2.0.1', u'husky': u'^4.2.3', u'uglify-js': u'3.3.21', u'eslint-plugin-import': u'^2.20.1', u'karma': u'^0.13.13'}, u'_from': u'underscore@^1.8.3', u'bundleDependencies': False, u'_phantomChildren': {}, u'version': u'1.10.2', u'_resolved': u'https://registry.npmjs.org/underscore/-/underscore-1.10.2.tgz', u'_inBundle': False, u'homepage': u'https://underscorejs.org', u'files': [u'underscore.js', u'underscore.js.map', u'underscore-min.js', u'underscore-min.js.map', u'modules/'], u'_requested': {u'name': u'underscore', u'escapedName': u'underscore', u'saveSpec': None, u'rawSpec': u'^1.8.3', u'raw': u'underscore@^1.8.3', u'registry': True, u'fetchSpec': u'^1.8.3', u'type': u'range'}, u'description': u"JavaScript's functional programming helper library.", u'repository': {u'url': u'git://github.com/jashkenas/underscore.git', u'type': u'git'}, u'_requiredBy': [u'/pebble-fctx-compiler'], u'scripts': {u'test-node': u'npm run prepare-tests && qunit-cli test/*.js', u'prepublishOnly': u'npm run build && npm run doc', u'coveralls': u'nyc npm run test-node && nyc report --reporter=text-lcov | coveralls', u'weight': u'npm run bundle && npm run minify | gzip-size | pretty-bytes', u'test-browser': u'npm run prepare-tests && npm i karma-phantomjs-launcher && karma start', u'doc': u'cd docs && rollup -c && docco -o . underscore.js', u'lint': u'eslint modules/*.js test/*.js', u'bundle': u'rollup --config && eslint underscore.js', u'prepare-tests': u'npm run bundle && npm run bundle-treeshake', u'build': u'npm run bundle && npm run minify -- --source-map content=underscore.js.map --source-map-url " " -o underscore-min.js', u'coverage': u'nyc npm run test-node && nyc report', u'test': u'npm run lint && npm run test-node', u'minify': u'uglifyjs underscore.js -c "evaluate=false" --comments "/    .*/" -m', u'bundle-treeshake': u'cd test-treeshake && npx rollup@latest --config'}, u'main': u'underscore.js', u'name': u'underscore', u'license': u'MIT', u'deprecated': False, u'author': {u'name': u'Jeremy Ashkenas', u'email': u'jeremy@documentcloud.org'}, u'bugs': {u'url': u'https://github.com/jashkenas/underscore/issues'}, 'js_paths': ['node_modules/underscore/modules/index-all.js', 'node_modules/underscore/modules/index-default.js', 'node_modules/underscore/modules/index.js', 'node_modules/underscore/package.json', 'node_modules/underscore/underscore-min.js', 'node_modules/underscore/underscore.js'], u'_where': u'/home/astosia/pebble-dev/pebble-sdk-4.5-linux64/rehoboam/node_modules/pebble-fctx-compiler', u'husky': {u'hooks': {u'pre-commit': u'npm run bundle && git add underscore.js underscore.js.map', u'post-commit': u'git reset underscore.js underscore.js.map'}}, u'_id': u'underscore@1.10.2', u'_shasum': u'73d6aa3668f3188e4adb0f1943bd12cfd7efaaaf'}, {u'_location': u'/minimist', u'_spec': u'minimist@^1.2.0', u'testling': {u'files': u'test/*.js', u'browsers': [u'ie/6..latest', u'ff/5', u'firefox/latest', u'chrome/10', u'chrome/latest', u'safari/5.1', u'safari/latest', u'opera/12']}, u'_integrity': u'sha512-FM9nNUYrRBAELZQT3xeZQ7fmMOBg6nWNmJKTcgsJeaLstP/UODVpGsr5OhXhhXg6f+qtJ8uiZ+PUxkDWcgIXLw==', u'keywords': [u'argv', u'getopt', u'parser', u'optimist'], u'devDependencies': {u'covert': u'^1.0.0', u'tap': u'~0.4.0', u'tape': u'^3.5.0'}, u'_from': u'minimist@^1.2.0', u'bundleDependencies': False, u'_phantomChildren': {}, u'version': u'1.2.5', u'_resolved': u'https://registry.npmjs.org/minimist/-/minimist-1.2.5.tgz', u'main': u'index.js', u'homepage': u'https://github.com/substack/minimist', u'_requested': {u'name': u'minimist', u'escapedName': u'minimist', u'saveSpec': None, u'rawSpec': u'^1.2.0', u'raw': u'minimist@^1.2.0', u'registry': True, u'fetchSpec': u'^1.2.0', u'type': u'range'}, u'description': u'parse argument options', u'repository': {u'url': u'git://github.com/substack/minimist.git', u'type': u'git'}, u'_requiredBy': [u'/pebble-fctx-compiler'], u'scripts': {u'test': u'tap test/*.js', u'coverage': u'covert test/*.js'}, u'_inBundle': False, u'name': u'minimist', u'license': u'MIT', u'deprecated': False, u'author': {u'url': u'http://substack.net', u'name': u'James Halliday', u'email': u'mail@substack.net'}, u'bugs': {u'url': u'https://github.com/substack/minimist/issues'}, 'js_paths': ['node_modules/minimist/example/parse.js', 'node_modules/minimist/index.js', 'node_modules/minimist/package.json', 'node_modules/minimist/test/all_bool.js', 'node_modules/minimist/test/bool.js', 'node_modules/minimist/test/dash.js', 'node_modules/minimist/test/default_bool.js', 'node_modules/minimist/test/dotted.js', 'node_modules/minimist/test/kv_short.js', 'node_modules/minimist/test/long.js', 'node_modules/minimist/test/num.js', 'node_modules/minimist/test/parse.js', 'node_modules/minimist/test/parse_modified.js', 'node_modules/minimist/test/proto.js', 'node_modules/minimist/test/short.js', 'node_modules/minimist/test/stop_early.js', 'node_modules/minimist/test/unknown.js', 'node_modules/minimist/test/whitespace.js'], u'_where': u'/home/astosia/pebble-dev/pebble-sdk-4.5-linux64/rehoboam/node_modules/pebble-fctx-compiler', u'_id': u'minimist@1.2.5', u'_shasum': u'67d66014b66a6a8aaa0c083c5fd58df4e4e97602'}, {u'_location': u'/pebble-utf8', u'_spec': u'pebble-utf8@^1.0.1', u'_integrity': u'sha1-oEmi5tCE1td31pA50SfH6QHRuEc=', u'keywords': [u'pebble-package'], u'_from': u'pebble-utf8@^1.0.1', u'pebble': {u'sdkVersion': u'3', u'projectType': u'package', u'targetPlatforms': [u'aplite', u'basalt', u'chalk', u'diorite', u'emery'], u'resources': {u'media': []}}, u'bundleDependencies': False, u'_phantomChildren': {}, u'version': u'1.0.1', u'_resolved': u'https://registry.npmjs.org/pebble-utf8/-/pebble-utf8-1.0.1.tgz', u'_inBundle': False, u'homepage': u'https://github.com/jrmobley/pebble-utf8#readme', u'files': [u'dist.zip'], u'_requested': {u'name': u'pebble-utf8', u'escapedName': u'pebble-utf8', u'saveSpec': None, u'rawSpec': u'^1.0.1', u'raw': u'pebble-utf8@^1.0.1', u'registry': True, u'fetchSpec': u'^1.0.1', u'type': u'range'}, u'description': u'Functions for working with UTF-8 strings.', u'repository': {u'url': u'git+https://github.com/jrmobley/pebble-utf8.git', u'type': u'git'}, u'_requiredBy': [u'/pebble-fctx'], u'dependencies': {}, 'path': 'node_modules/pebble-utf8/dist', u'name': u'pebble-utf8', u'license': u'MIT', u'deprecated': False, u'author': {u'name': u'JR Mobley'}, u'bugs': {u'url': u'https://github.com/jrmobley/pebble-utf8/issues'}, u'_where': u'/home/astosia/pebble-dev/pebble-sdk-4.5-linux64/rehoboam/node_modules/pebble-fctx', u'_id': u'pebble-utf8@1.0.1', u'_shasum': u'a049a2e6d084d6d777d69039d127c7e901d1b847'}, {u'_location': u'/sax', u'_spec': u'sax@>=0.6.0', u'_integrity': u'sha512-NqVDv9TpANUjFm0N8uM5GxL36UgKi9/atZw+x7YFnQ8ckwFGKrl4xX4yWtrey3UJm5nP1kUbnYgLopqWNSRhWw==', u'devDependencies': {u'tap': u'^10.5.1', u'standard': u'^8.6.0'}, u'_from': u'sax@>=0.6.0', u'bundleDependencies': False, u'_phantomChildren': {}, u'version': u'1.2.4', u'_resolved': u'https://registry.npmjs.org/sax/-/sax-1.2.4.tgz', u'main': u'lib/sax.js', u'homepage': u'https://github.com/isaacs/sax-js#readme', u'files': [u'lib/sax.js', u'LICENSE', u'README.md'], u'_requested': {u'name': u'sax', u'escapedName': u'sax', u'saveSpec': None, u'rawSpec': u'>=0.6.0', u'raw': u'sax@>=0.6.0', u'registry': True, u'fetchSpec': u'>=0.6.0', u'type': u'range'}, u'description': u'An evented streaming XML parser in JavaScript', u'repository': {u'url': u'git://github.com/isaacs/sax-js.git', u'type': u'git'}, u'_requiredBy': [u'/xml2js'], u'scripts': {u'postpublish': u'git push origin --all; git push origin --tags', u'postversion': u'npm publish', u'preversion': u'npm test', u'test': u'tap test/*.js --cov -j4', u'posttest': u'standard -F test/*.js lib/*.js'}, u'_inBundle': False, u'name': u'sax', u'license': u'ISC', u'deprecated': False, u'author': {u'url': u'http://blog.izs.me/', u'name': u'Isaac Z. Schlueter', u'email': u'i@izs.me'}, u'bugs': {u'url': u'https://github.com/isaacs/sax-js/issues'}, 'js_paths': ['node_modules/sax/lib/sax.js', 'node_modules/sax/package.json'], u'_where': u'/home/astosia/pebble-dev/pebble-sdk-4.5-linux64/rehoboam/node_modules/xml2js', u'_id': u'sax@1.2.4', u'_shasum': u'2816234e2378bddc4e5354fab5caa895df7100d9'}, {u'_location': u'/xmlbuilder', u'contributors': [], u'_spec': u'xmlbuilder@~11.0.0', u'typings': u'./typings/index.d.ts', u'_integrity': u'sha512-fDlsI/kFEx7gLvbecc0/ohLG50fugQp8ryHzMTuW9vSa1GJ0XYWKnhsUx7oie3G98+r56aTQIUB4kht42R3JvA==', u'keywords': [u'xml', u'xmlbuilder'], u'devDependencies': {u'xpath': u'*', u'coveralls': u'*', u'istanbul': u'*', u'mocha': u'*', u'coffeescript': u'1.*', u'coffee-coverage': u'2.*'}, u'_from': u'xmlbuilder@~11.0.0', u'bundleDependencies': False, u'engines': {u'node': u'>=4.0'}, u'_phantomChildren': {}, u'version': u'11.0.1', u'_resolved': u'https://registry.npmjs.org/xmlbuilder/-/xmlbuilder-11.0.1.tgz', u'_inBundle': False, u'homepage': u'http://github.com/oozcitak/xmlbuilder-js', u'_requested': {u'name': u'xmlbuilder', u'escapedName': u'xmlbuilder', u'saveSpec': None, u'rawSpec': u'~11.0.0', u'raw': u'xmlbuilder@~11.0.0', u'registry': True, u'fetchSpec': u'~11.0.0', u'type': u'range'}, u'description': u'An XML builder for node.js', u'repository': {u'url': u'git://github.com/oozcitak/xmlbuilder-js.git', u'type': u'git'}, u'_requiredBy': [u'/xml2js'], u'dependencies': {}, u'scripts': {u'postpublish': u'rm -rf lib', u'test': u'mocha "test/**/*.coffee" && istanbul report text lcov', u'prepublishOnly': u'coffee -co lib src'}, u'main': u'./lib/index', u'name': u'xmlbuilder', u'license': u'MIT', u'deprecated': False, u'author': {u'name': u'Ozgur Ozcitak', u'email': u'oozcitak@gmail.com'}, u'bugs': {u'url': u'http://github.com/oozcitak/xmlbuilder-js/issues'}, 'js_paths': ['node_modules/xmlbuilder/lib/Derivation.js', 'node_modules/xmlbuilder/lib/DocumentPosition.js', 'node_modules/xmlbuilder/lib/NodeType.js', 'node_modules/xmlbuilder/lib/OperationType.js', 'node_modules/xmlbuilder/lib/Utility.js', 'node_modules/xmlbuilder/lib/WriterState.js', 'node_modules/xmlbuilder/lib/XMLAttribute.js', 'node_modules/xmlbuilder/lib/XMLCData.js', 'node_modules/xmlbuilder/lib/XMLCharacterData.js', 'node_modules/xmlbuilder/lib/XMLComment.js', 'node_modules/xmlbuilder/lib/XMLDOMConfiguration.js', 'node_modules/xmlbuilder/lib/XMLDOMErrorHandler.js', 'node_modules/xmlbuilder/lib/XMLDOMImplementation.js', 'node_modules/xmlbuilder/lib/XMLDOMStringList.js', 'node_modules/xmlbuilder/lib/XMLDTDAttList.js', 'node_modules/xmlbuilder/lib/XMLDTDElement.js', 'node_modules/xmlbuilder/lib/XMLDTDEntity.js', 'node_modules/xmlbuilder/lib/XMLDTDNotation.js', 'node_modules/xmlbuilder/lib/XMLDeclaration.js', 'node_modules/xmlbuilder/lib/XMLDocType.js', 'node_modules/xmlbuilder/lib/XMLDocument.js', 'node_modules/xmlbuilder/lib/XMLDocumentCB.js', 'node_modules/xmlbuilder/lib/XMLDocumentFragment.js', 'node_modules/xmlbuilder/lib/XMLDummy.js', 'node_modules/xmlbuilder/lib/XMLElement.js', 'node_modules/xmlbuilder/lib/XMLNamedNodeMap.js', 'node_modules/xmlbuilder/lib/XMLNode.js', 'node_modules/xmlbuilder/lib/XMLNodeFilter.js', 'node_modules/xmlbuilder/lib/XMLNodeList.js', 'node_modules/xmlbuilder/lib/XMLProcessingInstruction.js', 'node_modules/xmlbuilder/lib/XMLRaw.js', 'node_modules/xmlbuilder/lib/XMLStreamWriter.js', 'node_modules/xmlbuilder/lib/XMLStringWriter.js', 'node_modules/xmlbuilder/lib/XMLStringifier.js', 'node_modules/xmlbuilder/lib/XMLText.js', 'node_modules/xmlbuilder/lib/XMLTypeInfo.js', 'node_modules/xmlbuilder/lib/XMLUserDataHandler.js', 'node_modules/xmlbuilder/lib/XMLWriterBase.js', 'node_modules/xmlbuilder/lib/index.js', 'node_modules/xmlbuilder/package.json'], u'_where': u'/home/astosia/pebble-dev/pebble-sdk-4.5-linux64/rehoboam/node_modules/xml2js', u'_id': u'xmlbuilder@11.0.1', u'_shasum': u'be9bae1c8a046e76b31127726347d0ad7002beb3'}]
LIB_RESOURCES_JSON = {u'xml2js': {}, u'pebble-clay': [], u'minimist': {}, u'svg-path-parser': {}, u'pebble-fctx-compiler': {}, u'xmlbuilder': {}, u'colors': {}, u'sax': {}, u'underscore': {}, u'pebble-utf8': [], u'pebble-fctx': []}
LIB_ST = '-l%s'
LINKFLAGS = ['-mcpu=cortex-m3', '-mthumb', '-Wl,--gc-sections', '-Wl,--warn-common', '-fPIE', '-Os']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_cshlib = ['-shared']
LINKFLAGS_cstlib = ['-Wl,-Bstatic']
LINK_CC = ['arm-none-eabi-gcc']
MESSAGE_KEYS = {u'Text1ColorN': 10005, u'MinColorN': 10025, u'MinColor': 10024, u'Invert': 10045, u'Text2ColorN': 10007, u'Text5ColorN': 10041, u'WeatherWind': 10026, u'Text2Color': 10006, u'Back1Color': 10000, u'Text3ColorN': 10030, u'Text6ColorN': 10059, u'HourSunset': 10013, u'Text1Color': 10004, u'WeatherCond': 10010, u'UpSlider': 10015, u'FrameColorN': 10009, u'IconFore': 10032, u'FrameColor': 10008, u'WEATHER_SUNSET_KEY': 10028, u'EmailPMKEY': 10020, u'PINPMKEY': 10021, u'NightTheme': 10016, u'SideColor1': 10054, u'SideColor2': 10056, u'HourSunrise': 10012, u'Text5Color': 10040, u'SideColor1N': 10055, u'FrameColor1': 10050, u'Text3Color': 10029, u'Text4Color': 10036, u'NameLocation': 10014, u'Rotate': 10044, u'WindIconAve': 10039, u'FrameColor2N': 10053, u'IconNow': 10031, u'RightLeft': 10043, u'APIKEY_User': 10017, u'Text6Color': 10058, u'TempFore': 10033, u'Back1ColorN': 10001, u'TempForeLow': 10035, u'FrameColor2': 10051, u'HourColor': 10022, u'WeatherUnit': 10018, u'Back2ColorN': 10003, u'MoonPhase': 10048, u'Freetext': 10047, u'WindFore': 10034, u'WEATHER_SUNRISE_KEY': 10049, u'SideColor2N': 10057, u'bluetoothvibe': 10027, u'WindUnit': 10042, u'FrameColor1N': 10052, u'Text4ColorN': 10037, u'WeatherTemp': 10011, u'Back2Color': 10002, u'WeatherProv': 10019, u'WindIconNow': 10038, u'HourColorN': 10023, u'InvertNight': 10046}
MESSAGE_KEYS_DEFINITION = '/home/astosia/pebble-dev/pebble-sdk-4.5-linux64/Rehoboam/build/src/message_keys.auto.c'
MESSAGE_KEYS_HEADER = '/home/astosia/pebble-dev/pebble-sdk-4.5-linux64/Rehoboam/build/include/message_keys.auto.h'
MESSAGE_KEYS_JSON = '/home/astosia/pebble-dev/pebble-sdk-4.5-linux64/Rehoboam/build/js/message_keys.json'
NODE_PATH = '/home/astosia/.pebble-sdk/SDKs/current/node_modules'
PEBBLE_SDK_COMMON = '/home/astosia/.pebble-sdk/SDKs/current/sdk-core/pebble/common'
PEBBLE_SDK_PLATFORM = '/home/astosia/.pebble-sdk/SDKs/current/sdk-core/pebble/diorite'
PEBBLE_SDK_ROOT = '/home/astosia/.pebble-sdk/SDKs/current/sdk-core/pebble'
PLATFORM = {'TAGS': ['diorite', 'bw', 'rect', 'mic', 'strap', 'health', '144w', '168h'], 'MAX_FONT_GLYPH_SIZE': 256, 'ADDITIONAL_TEXT_LINES_FOR_PEBBLE_H': [], 'MAX_APP_BINARY_SIZE': 65536, 'MAX_RESOURCES_SIZE': 1048576, 'MAX_APP_MEMORY_SIZE': 65536, 'MAX_WORKER_MEMORY_SIZE': 10240, 'NAME': 'diorite', 'BUNDLE_BIN_DIR': 'diorite', 'BUILD_DIR': 'diorite', 'MAX_RESOURCES_SIZE_APPSTORE': 262144, 'DEFINES': ['PBL_PLATFORM_DIORITE', 'PBL_BW', 'PBL_RECT', 'PBL_MICROPHONE', 'PBL_HEALTH', 'PBL_SMARTSTRAP', 'PBL_DISPLAY_WIDTH=144', 'PBL_DISPLAY_HEIGHT=168']}
PLATFORM_NAME = 'diorite'
PREFIX = '/usr/local'
PROJECT_INFO = {'appKeys': {u'Text1ColorN': 10005, u'MinColorN': 10025, u'MinColor': 10024, u'Invert': 10045, u'Text2ColorN': 10007, u'Text5ColorN': 10041, u'WeatherWind': 10026, u'Text2Color': 10006, u'Back1Color': 10000, u'Text3ColorN': 10030, u'Text6ColorN': 10059, u'HourSunset': 10013, u'Text1Color': 10004, u'WeatherCond': 10010, u'UpSlider': 10015, u'FrameColorN': 10009, u'IconFore': 10032, u'FrameColor': 10008, u'WEATHER_SUNSET_KEY': 10028, u'EmailPMKEY': 10020, u'PINPMKEY': 10021, u'NightTheme': 10016, u'SideColor1': 10054, u'SideColor2': 10056, u'HourSunrise': 10012, u'Text5Color': 10040, u'SideColor1N': 10055, u'FrameColor1': 10050, u'Text3Color': 10029, u'Text4Color': 10036, u'NameLocation': 10014, u'Rotate': 10044, u'WindIconAve': 10039, u'FrameColor2N': 10053, u'IconNow': 10031, u'RightLeft': 10043, u'APIKEY_User': 10017, u'Text6Color': 10058, u'TempFore': 10033, u'Back1ColorN': 10001, u'TempForeLow': 10035, u'FrameColor2': 10051, u'HourColor': 10022, u'WeatherUnit': 10018, u'Back2ColorN': 10003, u'MoonPhase': 10048, u'Freetext': 10047, u'WindFore': 10034, u'WEATHER_SUNRISE_KEY': 10049, u'SideColor2N': 10057, u'bluetoothvibe': 10027, u'WindUnit': 10042, u'FrameColor1N': 10052, u'Text4ColorN': 10037, u'WeatherTemp': 10011, u'Back2Color': 10002, u'WeatherProv': 10019, u'WindIconNow': 10038, u'HourColorN': 10023, u'InvertNight': 10046}, u'sdkVersion': u'3', u'projectType': u'native', u'uuid': u'ae893b61-48b6-46c0-af3b-134cc9bc8c68', u'messageKeys': {u'Text1ColorN': 10005, u'MinColorN': 10025, u'MinColor': 10024, u'Invert': 10045, u'Text2ColorN': 10007, u'Text5ColorN': 10041, u'WeatherWind': 10026, u'Text2Color': 10006, u'Back1Color': 10000, u'Text3ColorN': 10030, u'Text6ColorN': 10059, u'HourSunset': 10013, u'Text1Color': 10004, u'WeatherCond': 10010, u'UpSlider': 10015, u'FrameColorN': 10009, u'IconFore': 10032, u'FrameColor': 10008, u'WEATHER_SUNSET_KEY': 10028, u'EmailPMKEY': 10020, u'PINPMKEY': 10021, u'NightTheme': 10016, u'SideColor1': 10054, u'SideColor2': 10056, u'HourSunrise': 10012, u'Text5Color': 10040, u'SideColor1N': 10055, u'FrameColor1': 10050, u'Text3Color': 10029, u'Text4Color': 10036, u'NameLocation': 10014, u'Rotate': 10044, u'WindIconAve': 10039, u'FrameColor2N': 10053, u'IconNow': 10031, u'RightLeft': 10043, u'APIKEY_User': 10017, u'Text6Color': 10058, u'TempFore': 10033, u'Back1ColorN': 10001, u'TempForeLow': 10035, u'FrameColor2': 10051, u'HourColor': 10022, u'WeatherUnit': 10018, u'Back2ColorN': 10003, u'MoonPhase': 10048, u'Freetext': 10047, u'WindFore': 10034, u'WEATHER_SUNRISE_KEY': 10049, u'SideColor2N': 10057, u'bluetoothvibe': 10027, u'WindUnit': 10042, u'FrameColor1N': 10052, u'Text4ColorN': 10037, u'WeatherTemp': 10011, u'Back2Color': 10002, u'WeatherProv': 10019, u'WindIconNow': 10038, u'HourColorN': 10023, u'InvertNight': 10046}, 'companyName': u'astosia', u'enableMultiJS': True, u'targetPlatforms': [u'aplite', u'basalt', u'chalk', u'diorite'], u'capabilities': [u'location', u'configurable', u'health'], 'versionLabel': u'1.0', 'longName': u'Rehoboam', u'displayName': u'Rehoboam', 'shortName': u'Rehoboam', u'watchapp': {u'watchface': True}, u'resources': {u'media': [{u'type': u'png', u'name': u'IMAGE_BACKGROUND', u'file': u'images/Background5.png'}, {u'type': u'png', u'name': u'IMAGE_BACKGROUNDINV', u'file': u'images/Backgroundinverted5.png'}, {u'targetPlatforms': None, u'type': u'font', u'name': u'FONT_DRIPICONS_18', u'file': u'fonts/Dripicons'}, {u'targetPlatforms': None, u'type': u'font', u'name': u'FONT_DRIPICONS_16', u'file': u'fonts/Dripicons'}, {u'targetPlatforms': None, u'type': u'font', u'name': u'FONT_WEATHERICONS_20', u'file': u'fonts/Weathericons'}, {u'targetPlatforms': None, u'type': u'font', u'name': u'FONT_WEATHERICONS_16', u'file': u'fonts/Weathericons'}, {u'targetPlatforms': None, u'type': u'font', u'name': u'FONT_WEATHERICONS_12', u'file': u'fonts/Weathericons'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'IMAGE_SUNSET_ICON2', u'file': u'images/Sunset2'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'IMAGE_SUNSET_ICON', u'file': u'images/sunset'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'IMAGE_BT_ICON', u'file': u'images/bt-icon'}, {u'targetPlatforms': None, u'type': u'raw', u'name': u'FONT_STEELFISH', u'file': u'data/STEELFISH BIG'}, {u'targetPlatforms': None, u'type': u'raw', u'name': u'OPENSANSCON_FFONT', u'file': u'data/Open sans ffont'}, {u'targetPlatforms': None, u'type': u'raw', u'name': u'FONT_DINBOLD', u'file': u'data/DINPro-Bold'}, {u'targetPlatforms': None, u'type': u'raw', u'name': u'FONT_DINCONBOLD', u'file': u'data/DINPro-CondensedMedium'}]}, 'name': u'Rehoboam'}
REQUESTED_PLATFORMS = [u'aplite', u'basalt', u'chalk', u'diorite']
RESOURCES_JSON = [{u'type': u'png', u'name': u'IMAGE_BACKGROUND', u'file': u'images/Background5.png'}, {u'type': u'png', u'name': u'IMAGE_BACKGROUNDINV', u'file': u'images/Backgroundinverted5.png'}, {u'targetPlatforms': None, u'type': u'font', u'name': u'FONT_DRIPICONS_18', u'file': u'fonts/Dripicons'}, {u'targetPlatforms': None, u'type': u'font', u'name': u'FONT_DRIPICONS_16', u'file': u'fonts/Dripicons'}, {u'targetPlatforms': None, u'type': u'font', u'name': u'FONT_WEATHERICONS_20', u'file': u'fonts/Weathericons'}, {u'targetPlatforms': None, u'type': u'font', u'name': u'FONT_WEATHERICONS_16', u'file': u'fonts/Weathericons'}, {u'targetPlatforms': None, u'type': u'font', u'name': u'FONT_WEATHERICONS_12', u'file': u'fonts/Weathericons'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'IMAGE_SUNSET_ICON2', u'file': u'images/Sunset2'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'IMAGE_SUNSET_ICON', u'file': u'images/sunset'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'IMAGE_BT_ICON', u'file': u'images/bt-icon'}, {u'targetPlatforms': None, u'type': u'raw', u'name': u'FONT_STEELFISH', u'file': u'data/STEELFISH BIG'}, {u'targetPlatforms': None, u'type': u'raw', u'name': u'OPENSANSCON_FFONT', u'file': u'data/Open sans ffont'}, {u'targetPlatforms': None, u'type': u'raw', u'name': u'FONT_DINBOLD', u'file': u'data/DINPro-Bold'}, {u'targetPlatforms': None, u'type': u'raw', u'name': u'FONT_DINCONBOLD', u'file': u'data/DINPro-CondensedMedium'}]
RPATH_ST = '-Wl,-rpath,%s'
SANDBOX = False
SDK_VERSION_MAJOR = 5
SDK_VERSION_MINOR = 86
SHLIB_MARKER = None
SIZE = 'arm-none-eabi-size'
SONAME_ST = '-Wl,-h,%s'
STLIBPATH_ST = '-L%s'
STLIB_MARKER = None
STLIB_ST = '-l%s'
SUPPORTED_PLATFORMS = ['aplite', 'chalk', 'emery', 'basalt', 'diorite']
TARGET_PLATFORMS = ['diorite', 'chalk', 'basalt', 'aplite']
TIMESTAMP = 1590059864
USE_GROUPS = True
VERBOSE = 0
WEBPACK = '/home/astosia/.pebble-sdk/SDKs/current/node_modules/.bin/webpack'
cprogram_PATTERN = '%s'
cshlib_PATTERN = 'lib%s.so'
cstlib_PATTERN = 'lib%s.a'
macbundle_PATTERN = '%s.bundle'
