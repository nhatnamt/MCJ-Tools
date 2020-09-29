    let node = document.getElementById('input');
    node.addEventListener('keyup', (e) => {
      if (e.key == "Enter") {
        txt = node.value();
        alert('HIIIIII');
      }
      console.log(`Key "${e.key}" released  [event: keyup]`);
      console.log(txt);
      //logMessage(`Key "${e.key}" released  [event: keyup]`);
    });
  
  // Restores select box and checkbox state using the preferences
  // stored in chrome.storage.
  //document.getElementById('input').addEventListener("keyup",
  //    getName);