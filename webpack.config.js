const webpack = require('webpack');
const path = require('path');

const config = {
    entry:  path.join(__dirname, '/static/src/index.js'),
    output: {
        path: path.join(__dirname, '/static/dist'),
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
            },
            {
                test: /\.css$/,
                use: ['style-loader','css-loader']
            },
        ]
    },
};

module.exports = config;