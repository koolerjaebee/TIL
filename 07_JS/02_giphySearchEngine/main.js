// 1. input 태그 안의 값(value)을 잡는다.
// const input = document.querySelector('#js-userinput').value;
// 2. button 에 'click' 이 일어났을 때, input 에 ENTER 키를 쳤을 때, 이벤트 리스너를 단다.
// [무엇].addEventListener([언제], [어떻게])
const button = document.querySelector('#js-go');
const inputArea = document.querySelector('#js-userinput');
const inputCountArea = document.querySelector('#js-image-count');
const resultArea = document.querySelector('#js-result-area');


button.addEventListener('click', () => {
    const inputValue = inputArea.value;
    const inputCount = inputCountArea.value;
    searchAndPush(inputValue, inputCount);
});

inputArea.addEventListener('keypress', (event) => {
    if (event.which === 13) {
        const inputValue = inputArea.value;
        const inputCount = inputCountArea.value;
        searchAndPush(inputValue, inputCount);
        // inputValue 로 Giphy API 에 요청 보내서 받기
    }
});

const searchAndPush = (keyword, number) => {
    const API_KEY = 'OoEOihlTWX2aswWN6Bfy6MoMo9hu7M5H'
    const url = `https://api.giphy.com/v1/gifs/search?api_key=${API_KEY}&q=${keyword}&limit=${number}&offset=0&rating=G&lang=en`

    const AJAX = new XMLHttpRequest(); // 요청 준비
    AJAX.open('GET', url); // 요청 세팅
    AJAX.send(); // 요청 보내기

    AJAX.addEventListener('load', (answer) => {
        const res = answer.target.response;
        const giphyData = JSON.parse(res);
        const dataSet = giphyData.data;

        resultArea.innerHTML = null;
        for (const data of dataSet) {
            pushToDOM(data.images.fixed_height.url);
        }
    });
    const pushToDOM = (imageUrl) => {
        resultArea.innerHTML += `<img src="${imageUrl}">`;
    };
}
// 3. Gipyhy API 에서 넘겨준 Data 를 index.html 에서 보여준다.
// const pushToDOM = (data) => {
//     // 요청 => 응답을 받아서.

//     // 화면에 보여준다
//     resultArea.innerHTML += data;
// };

const sendAjaxReq = () => {
    console.log('시작');
    const AJAX = new XMLHttpRequest(); // 요청 준비
    AJAX.open('GET', url); // 요청 세팅
    console.log('보낸닷!')
    AJAX.send() // 요청 보내기
    AJAX.addEventListener('load', function (answer) {
        console.log(answer);
        console.log(answer.target);
        const res = answer.target.response;
        const giphyData = JSON.parse(res);
    });
    console.log('끝')
}