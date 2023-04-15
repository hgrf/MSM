module.exports = {
  'env': {
    'browser': true,
    'es2021': true,
  },
  'extends': 'google',
  'overrides': [
  ],
  'parserOptions': {
    'ecmaVersion': 'latest',
    'sourceType': 'module',
  },
  'rules': {
    'require-jsdoc': 0,
    'max-len': [
      'error',
      {
        "code": 100,
      }
    ]
  },
  'ignorePatterns': [
    'src/api/**',
    'src/jquery-plugins/jquery.jeditable.js',
    'src/typeahead/bloodhound.js',
    'src/typeahead/typeahead.bundle.js',
  ],
};
