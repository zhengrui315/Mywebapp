const webpack = require('webpack');
const path = require('path');

const config = {
    entry:  __dirname + '/src/js/index.js',
    output: {
        path: path.join(__dirname, '/src/dist'),
        filename: 'bundle.js'
    },
    resolve: {
        extensions: ['.js', '.jsx', '.css']
    },
    module: {
        rules: [
            {
              test: /\.(js|jsx)$/,
              exclude: /node_modules/,
              loader: 'babel-loader'
            }
        ]
    },
};

module.exports = config;