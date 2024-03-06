const fs = require('fs');
const pdf = require('pdf-parse');
const text = [];
const dataBuffer = fs.readFileSync('ops.pdf');

pdf(dataBuffer).then(function(data) {
    for (let i = 6; i < data.numpages; i++) {
        text.push(data.text);
    }
    const say = new SpeechSynthesisUtterance(text.join(' '));
    window.speechSynthesis.speak(say);
});
