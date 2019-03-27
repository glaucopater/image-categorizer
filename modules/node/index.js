
const nsfwjs = require('nsfwjs');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;

const dom = new JSDOM(`<!DOCTYPE html><p>Hello world<img src='./images/games.jpg'></p>`);
console.log(dom.window.document.querySelector("p").textContent); // "Hello world"
const img = dom.window.document.getElementById('img')


// Load model from my S3.
// See the section hosting the model files on your site. 

const BASE_PATH = 'https://s3.amazonaws.com/ir_public/nsfwjs/';
const path = BASE_PATH + "model.json";
nsfwjs.load(path).then(function (model) {
  model.classify(img).then(function (predictions) {
    // Classify the image
    console.log('Predictions: ', predictions)
  })
})