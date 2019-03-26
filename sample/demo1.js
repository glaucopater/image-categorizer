const mobilenet = require('@tensorflow-models/mobilenet');
const jsdom = require("jsdom");
const {
    JSDOM
} = jsdom;

const dom = new JSDOM(`<!DOCTYPE html><p>Hello world<img src='./images/games.jpg' id='image'/></p>`);
console.log(dom.window.document.querySelector("p").textContent); // "Hello world"
const img = dom.window.document.getElementById('image')

console.log(img);

// Load the model. 
//global.fetch = require('node-fetch');
const model = mobilenet.load();
 
// Classify the image.
//

model.then(function (resp) {
        console.log("model", resp);
        const predictions = resp.classify(img,10);
        console.log('Predictions: ', predictions);
    })
    .then(function (result) { 
        //console.log("result ", result);
    });
 
