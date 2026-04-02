#!/usr/bin/node

document.addEventListener('DOMContentLoaded', function () {
  const translateBtn = document.getElementById('btn_translate');
  const languageCode = document.getElementById('language_code');
  const helloDiv = document.getElementById('hello');

  translateBtn.addEventListener('click', function () {
    const lang = languageCode.value;
    if (lang === '') {
      helloDiv.textContent = 'Please select a language';
      return;
    }

    fetch(`https://hellosalut.stefanbohacek.com/?lang=${lang}`)
      .then(response => response.json())
      .then(data => {
        helloDiv.textContent = data.hello;
      })
      .catch(error => {
        console.error('Error:', error);
        helloDiv.textContent = 'Error fetching translation';
      });
  });
});
