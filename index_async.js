async function img_up() {
    y = 0;
    let myPromise = new Promise(function (resolve) {
        while (y < 50) {
            y++;
            setTimeout(function () {
                resolve(soma(y));
            }, 100);
        }
    });
    console.log(await myPromise);
}


function soma(y) {
    y++;
    // if (y > -286) {
    //     y = await - 1000;
    // };
}


img_up();