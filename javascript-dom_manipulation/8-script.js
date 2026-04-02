#!/usr/bin/node

fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
  .then(response => response.json())
  .then(data => {
    document.getElementById('hello').textContent = data.hello;
  });
