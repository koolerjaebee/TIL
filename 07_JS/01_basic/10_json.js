// JavaScript Object Notation: JS 의 Object 처럼 표기하는 방법
// JSON 으로 표현된 데이터의 타입은 무조건 string
const rawJson = `
    {
        "name": "Martin",
        "job": "BaekSu"
    }
`

// parsing : 구문 분석
const parseData = JSON.parse(rawJson);
// serializing : 공용어로 번역(직렬화)
const backToJSON = JSON.stringify(parseData);
