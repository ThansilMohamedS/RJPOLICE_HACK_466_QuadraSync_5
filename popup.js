document.getElementById('checkButton').addEventListener('click', function() {
  chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
    var url = tabs[0].url;
    var result = checkSafety(url);
    document.getElementById('result').innerText = result;
  });
});

function checkSafety(url) {
  // Replace this with your safety-checking logic
  var unsafeList = ["example.com", "unsafe.com"];
  if (unsafeList.includes(url)) {
    return "Unsafe!";
  } else {
    return "Safe!";
  }
}