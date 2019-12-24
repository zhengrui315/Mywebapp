const webpack = require('webpack');
const path = require('path');
const Dotenv = require('dotenv-webpack');

const config = {
    entry:  path.join(__dirname, '/static/src/index.js'),
    output: {
        path: path.join(__dirname, '/static/dist'),
        publicPath: '/',
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
      plugins: [
        new Dotenv({
          path: '.env', // load this now instead of the ones in '.env'
          safe: true, // load '.env.example' to verify the '.env' variables are all set. Can also be a string to a different file.
          systemvars: true, // load all the predefined 'process.env' variables which will trump anything local per dotenv specs.
          silent: true, // hide any errors
          defaults: false // load '.env.defaults' as the default values if empty.
        })
      ]
};

module.exports = config;