window.addEventListener("keypress", logKey);

function logKey(e) {
    switch (e.code) {
        case 'KeyA':
          console.log('A');
          break;
        case 'KeyW':
            console.log('W');
            break;
        case 'KeyS':
          console.log('S');
          break;
        case 'KeyD':
            console.log('D');
            break;
    }
}